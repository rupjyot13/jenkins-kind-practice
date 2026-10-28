
from app import add, is_healthy


def test_add():
    assert add(2, 3) == 5


def test_is_healthy_success():
    assert is_healthy(200) is True


def test_is_healthy_failure():
    assert is_healthy(500) is False
