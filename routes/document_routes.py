from fastapi import APIRouter, UploadFile

router = APIRouter()

documents = []

@router.post("/documents/upload")
def upload_document(file: UploadFile, title: str):
    content = file.file.read()

    with open(file.filename, "wb") as f:
        f.write(content)

    documents.append({"title": title, "filename": file.filename})
    return {"msg": "Document uploaded"}

@router.get("/documents")
def get_documents():
    return documents

@router.delete("/documents/{doc_id}")
def delete_document(doc_id: int):
    return {"msg": "Deleted"}