from fastapi import FastAPI
from routes import auth_routes, document_routes, rag_routes

app = FastAPI(title="Financial Document Management API")

# Include all routes
app.include_router(auth_routes.router)
app.include_router(document_routes.router)
app.include_router(rag_routes.router)

@app.get("/")
def home():
    return {"message": "API is running successfully"}