import sys
import os
sys.path.append(os.path.abspath('..'))

import pytest
import Shortener



@pytest.fixture
def preparation():
    pass

@pytest.mark.parametrize("a, b, result",
                        [(5,5,10),
                        (3,5,8),
                        (-1, 1, 0)])
def test_testMe_True(a, b, result):
    assert Shortener.testMe(a, b) == result