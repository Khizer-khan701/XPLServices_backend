from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_voice():
    return {"message": "Voice route working!"}