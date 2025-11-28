

This project extracts structured billing information (service name, quantity, price) from medical bills using OCR + Google Gemini 1.5 Flash.

✔ Upload a medical bill image  
✔ Extract itemized charges  
✔ Returns clean JSON response  
✔ Token usage + success status included  


| Component | Technology |
|----------|------------|
| Backend API | FastAPI |
| OCR | Tesseract |
| LLM | Google Gemini 2.5 Flash |
| Hosting (Local) | Uvicorn |



```bash
git clone <your-repo-url>
cd hackrx-bill-extraction
pip install -r requirements.txt

