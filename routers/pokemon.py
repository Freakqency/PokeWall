from fastapi import APIRouter, Depends, HTTPException
from database import users, core
from sqlalchemy.orm import Session
from utils import get_pokemon_spirte

router = APIRouter()


# TODO: Rate Limit this api
@router.post("/api/v1/pokemon")
def add_pokemon(
    user: users.UserUpdate, db: Session = Depends(core.get_db)
) -> dict[str, str]:
    db_user = users.get_user_by_key(user.key, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Invalid API Key or Email")
    if db_user.is_active:
        raise HTTPException(status_code=404, detail="API key already used")
    if not get_pokemon_spirte(user.pokemon):
        raise HTTPException(status_code=404, detail="Invalid Pokemon Name")
    users.update_user(
        db_user=db_user,
        user=user,
        session=db,
    )
    return {"added pokemon": user.pokemon}
