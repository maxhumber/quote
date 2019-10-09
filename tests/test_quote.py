from subprocess import run
from quote import quote


def test_quote():
    search = "blake crouch"
    result = quote(search, limit=5)
    one = result[0]
    assert one["author"] == "Blake Crouch"
    assert one["book"]
    assert isinstance(one["quote"], str)


def test_cli():
    output = run("quote shakespeare", shell=True, capture_output=True)
    text = (
        output.stderr.decode("utf-8").replace("\x1b[31m", "").replace("\x1b[0m\n", "")
    )
    assert isinstance(text, str)
