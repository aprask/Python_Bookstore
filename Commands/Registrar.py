from Commands import Enter
from Commands.User import Client


class Registrar:
    order_total: float
    enter: Enter
    customer_line = []
    line_total: int
    client: Client
