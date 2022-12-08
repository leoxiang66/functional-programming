from env import *
import pyfp
from pyfp.interface import val


a= pyfp.Numeral(3)
b = pyfp.Numeral(4)
li1 = pyfp.List([1, 2, 3, 4])
li2 = pyfp.List([2, 3, 4, 5])


def test_elementwise_add():
    tmp = []
    for i in range(len(li1)):
        tmp.append(li1[i] + li2[i])
    result = pyfp.List(tmp)
    assert result[0] == li1[0] + li2[0]


def test_add():
    c = a + b
    assert val(a) + val(b) == val(c)

def test_mul():
    c = a * b
    assert  val(a) * val(b) == val(c)