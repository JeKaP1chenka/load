from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

# Загрузка файла на сервер
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename, "status": "File uploaded successfully"}

# Выгрузка файла с сервера
@app.get("/download/{file_name}")
async def download_file(file_name: str):
    return FileResponse(file_name)
