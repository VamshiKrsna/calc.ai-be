# backend/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from analyze_input import analyze_image

app = FastAPI(title="Canvas Analyzer API")

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],  # Replace "*" with your frontend URL for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-image")
async def analyze_image_endpoint(file: UploadFile = File(...)):
    """
    Endpoint to receive an image file, analyze it, and return the results.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    try:
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert("RGB")  # Ensure image is in RGB format

        dict_of_vars = {"x": 2, "y": 5}  # Example variables

        results = analyze_image(image, dict_of_vars)

        return {"results": results}

    except Exception as e:
        print(f"Error processing the image: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Canvas Analyzer API"}