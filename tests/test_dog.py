import pytest
from files.dog import Dog

class TestTestDog:

    def test_dog(self):
        dog = Dog()
        assert dog.get_age() == 4
