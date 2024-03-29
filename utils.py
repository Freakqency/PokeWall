import secrets
import pokebase as pb
import requests
import os


def generate_secret(length: int) -> str:
    """
    param: API Key length:int
    return secret key base64 encoded
    """
    return str(secrets.token_urlsafe(length))


def validate_mail(email: str) -> bool:
    """
    param: email: str - user email
    return: True if valid email else False
    """
    return True


def send_mail(email: str, key: str) -> bool:
    """
    param1: email(str): receivers email address
    param2: key(str): api key
    return: status(bool): True(success) | False(failure)
    """
    return True


def get_pokemon_spirte(name: str) -> bool:
    """
    param: pokemon name: str
    return: True if success else False
    """
    pokemon = pb.pokemon(name)
    if not hasattr(pokemon, "id"):
        return False
    img_data = requests.get(pb.SpriteResource("pokemon", pokemon.id).url).content
    with open(f"{os.getenv('DATA_DIR')}/spirtes/{name}.png", "wb") as handler:
        handler.write(img_data)
    return True
