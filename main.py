from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from PIL import Image
import io
from apps.calc.utils import analyze_image 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Server is running"}

@app.post("/calculate/analyze-image")
async def analyze_image_endpoint(file: UploadFile = File(...)):
    print(f"Received file: {file.filename}, Content Type: {file.content_type}")

    contents = await file.read()
    print(f"File contents length: {len(contents)} bytes")  

    img = Image.open(io.BytesIO(contents))

    results = analyze_image(img, dict_of_vars={})  # Pass any variables if needed

    return JSONResponse(content=results)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)