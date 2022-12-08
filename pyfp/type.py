from typing import Any, Union
import warnings
from .interface import val

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class Immutable:
    def __setattr__(self, name: str, value: Any) -> None:
        warnings.warn('Attribute setting has no effect on Immutable objects.')

    def __getattribute__(self, name: str) -> Any:
        warnings.warn('Immutable objects have no attributes.')


class String(str):
    def __init__(self, text: str) -> None:
        super().__init__()


class Numeral():
    def __init__(self, num: Union[int, float]):
        super().__init__()
        self.__data__ = dict(num = num)


    def __getattr__(self, item):
        return self.__data__[item]

    
    def __setattr__(self, key, value):
        if key != '__data__':
            raise TypeError(f'{self.__class__} has no attribute {key}.')
        try:
            self.__data__
        except:
            super(Numeral, self).__setattr__(key,value)
            return
        raise TypeError('Cannot reassign.')

    def __value__(self):
        return self.num

    #
    # def __getattribute__(self, item):
    #     print(item)
    #     if item == 'num':
    #         return self.__data__['num']
    #     else:
    #         raise AttributeError(f'{self.__class__} has no attributes {item}.')

    # def __setattr__(self, key, value):
    #     if key == '__data__':
    #         super(Numeral, self).__setattr__(key,value)
    #     else:
    #         raise AttributeError('Cannot reassign values.')
    # def __str__(self):
    #     return str(self.__data__['num'])
    #
    # def __repr__(self):
    #     return str(self.__data__['num'])
    #
    # def __value__(self):
    #     return self.__data__['num']


    # def __eq__(self, o: object) -> bool:
    #     print("I'm equal to him")
    #     return 1
    #
    # def __ne__(self, value):
    #     print("I'm not equal to him")
    #     return 1
    #
    # def __le__(self, value):
    #     print("I'm less equal to him")
    #     return 1
    #
    # def __ge__(self, value):
    #     print("i'm greater equal to him")
    #     return 1
    #
    # def __lt__(self, value):
    #     print("I'm less than him")
    #     return 1
    #
    # def __gt__(self, value):
    #     print("I'm greater than him")
    #     return 1










