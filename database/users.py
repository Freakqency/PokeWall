from re import U
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import Query

from . import core


class User(BaseModel):
    email: str
    name: str
    key: str
    pokemon: str
    url: str
    is_active: bool


class UserUpdate(BaseModel):
    key: str
    name: str
    pokemon: str
    url: str


def add_user(user: User, session: Session) -> User:
    session.add(user)
    session.commit()
    return user


def get_user(email: str, session: Session) -> User | None:
    return session.query(core.User).get(email)


def get_user_by_key(key: str, session: Session) -> User | None:
    return session.query(core.User).filter_by(key=key).one()


def update_user(db_user: User, user: UserUpdate, session: Session) -> None:
    db_user.name = user.name
    db_user.url = user.url
    db_user.pokemon = user.pokemon
    db_user.is_active = True
    session.commit()


def get_active_number_of_users(session: Session) -> int:
    return session.query(core.User).filter_by(is_active=True).count()


def get_active_users(session: Session) -> Query(User):
    return session.query(core.User).filter_by(is_active=True)
