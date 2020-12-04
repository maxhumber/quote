from subprocess import run

from quote import quote


def test_quote_1():
    search = "Bitcoin Billionaires"
    result = quote(search, limit=5)
    one = result[0]
    assert (
        one["author"] == "Ben Mezrich" and one["book"] and isinstance(one["quote"], str)
    )


def test_quote_2():
    search = "blake crouch"
    result = quote(search, limit=5)
    one = result[0]
    assert (
        one["author"] == "Blake Crouch"
        and one["book"]
        and isinstance(one["quote"], str)
    )


def test_cli():
    output = run("quote shakespeare", shell=True, capture_output=True).stderr.decode(
        "utf-8"
    )
    text = output.replace("\x1b[32m", "").replace("\x1b[0m\n", "")
    assert isinstance(text, str)
