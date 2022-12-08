from env import *
import fun2py
from fun2py.interface import val


a= fun2py.Numeral(3)
b = fun2py.Numeral(4)
li1 = fun2py.List([1, 2, 3, 4])
li2 = fun2py.List([2, 3, 4, 5])


def test_elementwise_add():
    tmp = []
    for i in range(len(li1)):
        tmp.append(li1[i] + li2[i])
    result = fun2py.List(tmp)
    assert result[0] == li1[0] + li2[0]


def test_add():
    c = a + b
    assert val(a) + val(b) == val(c)

def test_mul():
    c = a * b
    assert  val(a) * val(b) == val(c)