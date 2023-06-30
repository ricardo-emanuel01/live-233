from typer import run
from rich import print

"""
O typer organiza os argumentos posicionais como argumentos 
do CLI e os nomeados como flag opcionais
"""
def hello(
    name: str,
    email: str,
    password: str = "batatatata"
):
    print(f"{name=}, {email=}, {password=}")

run(hello)