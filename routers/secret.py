from typing import Annotated
from fastapi import APIRouter, Form, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi import Depends
from database import core, users
from utils import generate_secret, send_mail
from dotenv import load_dotenv
import os


router = APIRouter()

load_dotenv()


# TODO: Rate Limit this API
# TODO: Implement Captcha
@router.post("/api/v1/secret")
def secret(
    email: Annotated[str, Form()], db: Session = Depends(core.get_db)
) -> dict[str, users.User]:
    # TODO: validate mail
    if users.get_user(email=email, session=db):
        raise HTTPException(status_code=404, detail="API Key Already Sent")
    key = generate_secret(int(os.getenv("API_KEY_LENGTH")))
    # TODO: send mail
    # FIXME: fix return value
    return {
        "added": users.add_user(
            core.User(
                email=email, key=key, name="", url="", pokemon="", is_active=False
            ),
            session=db,
        )
    }
