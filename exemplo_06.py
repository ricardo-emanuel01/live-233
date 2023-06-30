from typer import Typer
from typer.testing import CliRunner

app = Typer()
test_runner = CliRunner()

@app.command()
def olar(name: str):
    print(f"Olar {name}")

def test():
    response = test_runner.invoke(app, ["Ricardo"])
    assert response.stdout == "Olar Ricardo\n", response.stdout

test()