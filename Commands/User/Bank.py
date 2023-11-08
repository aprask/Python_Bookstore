from Commands.Enter import Enter
from Commands.Registrar import Registrar
from Commands.User.Client import Client


class Bank:
    registrar: Registrar
    client: Client
    enter: Enter
    banks = []

    def __init__(self, enter_store, user_client):
        # While