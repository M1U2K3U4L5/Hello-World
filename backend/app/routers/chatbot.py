from fastapi import APIRouter

from app.schemas import ChatRequest, ChatResponse
from app.services.chatbot import answer_investment_question

router = APIRouter(prefix="/chatbot", tags=["chatbot"])


@router.post("/ask", response_model=ChatResponse)
def ask(payload: ChatRequest):
    return ChatResponse(
        answer=answer_investment_question(payload.question),
        disclaimer="This response is educational and not financial advice.",
    )
