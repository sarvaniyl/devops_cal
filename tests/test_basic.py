import pytest
from app.commands.basic import AddCommand, SubtractCommand

def test_add():
    add = AddCommand()
    assert add.execute(2, 3) == 5

def test_subtract():
    subtract = SubtractCommand()
    assert subtract.execute(10, 5) == 5
