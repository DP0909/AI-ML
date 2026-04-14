from fastapi import APIRouter

router = APIRouter()

@router.post("/rag/index-document")
def index_document():
    return {"msg": "Document indexed"}

@router.post("/rag/search")
def search(query: str):
    return {"results": f"Results for {query}"}