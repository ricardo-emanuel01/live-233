from typer import run
# Rich is used to get a prettier print
from rich import print
from enum import Enum

# Testing how --help changes with the type of input
class Ops(Enum):
    a = 'a'
    b = 'b'
    c = 'c'

"""
O typer organiza os argumentos posicionais como argumentos 
do CLI e os nomeados como flag opcionais
"""
def hello(name: str = None):
    print(f"Hello, [b][red]{name}[/][/b]! How are you?")

run(hello)