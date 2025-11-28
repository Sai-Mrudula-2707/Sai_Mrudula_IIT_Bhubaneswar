import os
import io
import requests
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import google.generativeai as genai
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



os.environ["GEMINI_API_KEY"] = "AIzaSyBqbReMumEKnZtZ-NWs017IFVxw59o5Sg8"  
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


 
app = FastAPI(title="Bill Extractor API - Gemini + OCR")



def extract_text(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)



def llm_parse(text: str):
    prompt = f"""
    Extract bill items from this bill text and return format:

    {{
      "items": [
        {{"name": "...", "qty": number, "price": number}}
      ],
      "total_items": number
    }}

    Text: {text}
    """

    result = model.generate_content(prompt)
    return result.text



@app.post("/extract-bill-data")
async def extract_bill_data(file: UploadFile = File(...)):

    try:
        image_bytes = await file.read()
        img = Image.open(io.BytesIO(image_bytes))

       
        extracted_text = extract_text(img)

        
        parsed_output = llm_parse(extracted_text)

        return JSONResponse(
            {
                "is_success": True,
                "extracted_data": parsed_output
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/")
def home():
    return {"message": "Bill Extraction API is running!"}
