import environs
from dataclasses import dataclass


@dataclass
class Config:
    token: str
    URL_API_AFISHA: str
    URL_API_SHOWS: str
    THEATRE_NAME: list
    ROOM_NAME: list

def get_config(path_to_env):
    env=environs.Env()
    env.read_env(path=path_to_env)
    return Config(token=env('BOT_TOKEN'), URL_API_AFISHA=env('URL_API_AFISHA'), URL_API_SHOWS=env('URL_API_SHOWS'), THEATRE_NAME=env('THEATRE_NAME'), ROOM_NAME=env('ROOM_NAME'))