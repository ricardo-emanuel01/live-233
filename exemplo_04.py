from typer import Argument, Option, Exit, run
from rich import print

__version__ = "0.0.1a0"

def version(arg):
    if arg:
        print(f"The system version is: {__version__}")
        raise Exit(code=0)

def validate_name(name: str):
    if name.lower() == "ricardo":
        return name
    raise Exit(code=1)


# Case sensitive does not work as expected!
def hello(
        name: str = Argument(
                ..., 
                help="Your first name",
                callback=validate_name,
        ),
        email: str = Argument(..., metavar="<e-mail>@gmail.com"),
        password: str = Option(
            ..., 
            prompt=True, 
            hide_input=True,
            confirmation_prompt=True
        ),
        usedB4: bool = Option(..., prompt=True),
        version: bool = Option(
            False,
            '--version', '-v', '--versao',
            callback=version,
            is_eager=True,
            is_flag=True
        )
):
    print(f"{name=}, {email=}, {password=}")

run(hello)
