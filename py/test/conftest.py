import pytest

from board import Board

@pytest.fixture
def empty_board():
    yield Board()