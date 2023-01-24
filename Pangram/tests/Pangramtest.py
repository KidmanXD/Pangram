import pytest
from Pangram.src.Pangramcode import *


@pytest.mark.test1
def test_pangram_failure():
    res = pangram("ff")
    assert res == False


@pytest.mark.test2
def test_pangram_success():
    res = pangram("The quick brown fox jumps over the lazy dog.")
    assert res == True


if __name__ == '__main__':
    pytest.main()
