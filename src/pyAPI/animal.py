import requests


class ServiceError(Exception):
    pass


class Animal:
    def __init__(self, img: str = None, fact: str = None):
        self.img = img
        self.image = img
        self.fact = fact


def dog(service: str = "dog.ceo"):
    if service == "dog.ceo":
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        return Animal(r.json()["message"])
    if service in ["no-api-key", "noapikey"]:
        r = requests.get("https://no-api-key.com/api/v2/animals/dog")
        return Animal(r.json()["image"], r.json()["fact"])
    if service in ["random.dog", "randdog"]:
        r = requests.get("https://random.dog/woof.json")
        return Animal(r.json()["url"])
    raise ServiceError(f"Unexpected Service: '{service}'")

def cat(service: str = "cataas"):
    if service == "cataas":
        return Animal("https://cataas.com/cat")
    if service == "catapi":
        r = requests.get("https://thatcopy.pw/catapi/rest/")
        return Animal(r.json()["url"])
    if service in ["no-api-key", "noapikey"]:
        r = requests.get("https://no-api-key.com/api/v2/animals/cat")
        return Animal(r.json()["image"], r.json()["fact"])