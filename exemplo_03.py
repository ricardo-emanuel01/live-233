from typer import Argument, run
from rich import print
import os

"""
By using the Argument class to define the parameters 
of a function, you specify that those parameters 
represent command-line arguments. This allows Typer to 
correctly handle the arguments and provide the expected behavior 
when the Typer application is executed from the command line.

If you don't use Argument to define a parameter and instead assign 
it a default value, Typer will interpret it as a flag or an optional 
argument rather than a required command-line argument.

But one can use Argument and set an optinal argument, but it still
an argument and don't become a flag
"""
def hello(
        name: str = Argument(..., metavar="Name", help="Your first name"),
        email: str = Argument(..., metavar="E-mail"),
        password: str = Argument(..., metavar="Password", envvar="SENHA")
):
    print(f"{name=}, {email=}, {password=}")

run(hello)