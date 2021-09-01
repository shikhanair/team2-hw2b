import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/py')

from example import add

''' Test add function '''
def test_add():
    assert add(1, 2) == 3