import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer
import tensorflow as tf
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time

load_dotenv()

app = FastAPI()

# Load the model and tokenizer
model_path = "./summarization_model"
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

class SummarizeRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": " Question Generator API UP & RUNNING!"}


@app.post("/summarize")
async def summarize_content(request: SummarizeRequest):
    
    if not request.text:
        return JSONResponse(content={"error": "Text not provided"}, status_code=400)

    start_time = time.time()
    
    inputs = tokenizer(request.text, return_tensors="tf", max_length=4020, truncation=True, padding="max_length")
    summary_ids = model.generate(inputs["input_ids"], num_beams=4, max_length=100, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    processing_time = time.time() - start_time
    
    return JSONResponse(
        content={
            "summary": summary,
            "processing_time_seconds": round(processing_time, 2)
        }, 
        media_type="application/json"
    )

if __name__ == '__main__':
    app.run()