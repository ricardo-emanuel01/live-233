from typer import Typer, Option, Exit, Context
from rich import print

app = Typer()

__version__ = "0.0.1a0"

def version(arg):
    if arg:
        print(f"Current version on your computer is: {__version__}")
        raise Exit(code=0)
    
@app.callback(invoke_without_command=True)
def callcaback(
    ctx: Context,
    version: bool = Option(
        False,
        '--version', '-v', '--versao',
        callback=version,
        is_eager=True,
        is_flag=True,
        case_sensitive=False
    )
):
    if ctx.invoked_subcommand:
        return
    print(
        'Use os seguintes comandos [b]Mariana[/] ou [b]Ricardo[/]'
    )

@app.command(name="Mariana")
def command_a():
    print("Command A")

@app.command(name="Ricardo", help="Comando Ricardo!")
def command_b(nome: str):
    print("Command B")

@app.command()
def command_c():
    print("Command C")

app()
