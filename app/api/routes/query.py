from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag import retrieve_context
from app.services.llm import ask_all_llms

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    context: str
    answers: dict

@router.post("/ask")
async def ask(request: QueryRequest):
    try:
 
        context = retrieve_context(request.question)

        if not context:
            context = "No relevant context found."

        answers = await ask_all_llms(context, request.question)

        return QueryResponse(
            question=request.question,
            context=context,
            answers=answers
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))