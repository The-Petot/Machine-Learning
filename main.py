import base64
import vertexai
import json
from vertexai.generative_models import GenerativeModel, SafetySetting, Part
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": " Question Generator API UP & RUNNING!"}


class GenerateRequest(BaseModel):
    text: str

@app.post("/generate")
async def multiturn_generate_content(request: GenerateRequest):
    if not request.text:
        return JSONResponse(content={"error": "text not provided"}, status_code=400)

    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION")
    model_name = os.getenv("AI_MODEL")
    instructions = os.getenv("SYSTEM_INSTRUCTION")
    if not all([project_id, location, model_name, instructions]):
        return JSONResponse(content={"error": "Environment variables not set correctly"}, status_code=500)

    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(
        model_name=model_name,
        system_instruction=[instructions]
    )
    chat = model.start_chat()
    response = chat.send_message(
        request.text,
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    
    raw_response = response.candidates[0].content.parts[0].text
    
    json_str = raw_response.strip()
    if json_str.startswith('```json'):
        json_str = json_str[7:] 
    if json_str.endswith('```'):
        json_str = json_str[:-3]
    
    try:
        parsed_json = json.loads(json_str)
        return JSONResponse(
            content=parsed_json,
            media_type="application/json"
        )
    except json.JSONDecodeError as e:
        return JSONResponse(
            content={"error": "Failed to parse JSON response", "details": str(e)},
            status_code=500
        )

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

if __name__ == '__main__':
    app.run()
