import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import tensorflow as tf
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time
from google.cloud import pubsub_v1

load_dotenv()

app = FastAPI()

# Load the model and tokenizer
model_path = "./summarization_model"
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

class SummarizeRequest(BaseModel):
    text: str
    taskId: str

@app.get("/")
async def root():
    return {"message": " Question Generator API UP & RUNNING!"}


@app.post("/summarize")
async def summarize_content(request: SummarizeRequest):
    
    if not request.text:
        return JSONResponse(content={"error": "Text not provided"}, status_code=400)
    if not request.taskId:
        return JSONResponse(content={"error": "TaskId not provided"}, status_code=400)
    
    topic = os.getenv("PUBSUB_TOPIC")
    project_id = os.getenv("PROJECT_ID")
    if not all([topic, project_id]):
        return JSONResponse(
            content={"error": "Environment variables not set correctly"},
            status_code=500,
        )
    
    publisher = pubsub_v1.PublisherClient()
    topic_name = publisher.topic_path(project_id, topic)

    start_time = time.time()
    
    inputs = tokenizer(request.text, return_tensors="tf", max_length=4020, truncation=True, padding="max_length")
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=100, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    processing_time = time.time() - start_time
    
    # Publish the result to Pub/Sub
    message = {
        "taskId": request.taskId,
        "taskType": "summary",
        "summary": summary,
        "processing_time": processing_time
    }
    message = json.dumps(message)
    message_bytes = message.encode("utf-8")
    publisher.publish(topic_name, data=message_bytes)

    return JSONResponse(
        content={
            "summary": summary,
            "processing_time_seconds": round(processing_time, 2)
        }, 
        media_type="application/json"
    )

if __name__ == '__main__':
    app.run()