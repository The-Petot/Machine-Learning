import base64
import vertexai
import json
from vertexai.generative_models import GenerativeModel, SafetySetting, Part
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": " Question Generator API UP & RUNNING!"}


@app.get("/generate")
async def multiturn_generate_content(RequestContext: str):
    vertexai.init(project="colab-441716", location="asia-southeast1")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
        system_instruction=[instructions]
    )
    chat = model.start_chat()
    response = chat.send_message(
        RequestContext,
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
        # Return formatted JSON response
        return JSONResponse(
            content=parsed_json,
            media_type="application/json"
        )
    except json.JSONDecodeError as e:
        return JSONResponse(
            content={"error": "Failed to parse JSON response", "details": str(e)},
            status_code=500
        )

instructions = """Anda adalah agen AI yang bertugas membuat 5 pertanyaan berbasis pilihan ganda (multiple-choice question) berdasarkan materi atau konteks yang diberikan oleh pengguna. Respons Anda harus terstruktur dalam format JSON dengan elemen-elemen berikut: 1. **question**: Pertanyaan yang relevan dengan materi atau konteks. 2. **options**: Sebuah array berisi empat opsi jawaban yang unik (A, B, C, dan D), dengan satu jawaban yang benar. 3. **correct_answer**: Huruf yang menunjukkan jawaban yang benar (A, B, C, atau D). 4. **explanation**: Penjelasan singkat mengapa jawaban tersebut benar. Contoh format JSON: ```json { \"question\": \"Apa itu machine learning?\", \"options\": [ \"A. Proses mengkodekan logika ke dalam perangkat lunak secara manual\", \"B. Penggunaan data untuk melatih model agar dapat membuat prediksi atau keputusan\", \"C. Sistem yang hanya mengandalkan aturan yang telah ditentukan sebelumnya\", \"D. Teknologi untuk menyimpan data dalam basis data\" ], \"correct_answer\": \"B\", \"explanation\": \"Machine learning adalah pendekatan di mana sistem menggunakan data untuk melatih model agar dapat memprediksi atau membuat keputusan tanpa diprogram secara eksplisit.\" }"""

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
