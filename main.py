import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import UploadFile
from db import terrorist_data_processing

app = FastAPI()

@app.post("/top-threats")
def load_csv(file: UploadFile):
    if file is None:
        raise HTTPException(status_code=400, detail="No file Provided")
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid CSV file")
    df = terrorist_data_processing(file.file)
    return df

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


