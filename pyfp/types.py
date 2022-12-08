from typing import Any, Union
import warnings


class Immutable:
    def __setattr__(self, name: str, value: Any) -> None:
        warnings.warn('Attribute setting has no effect on Immutable objects.')

    def __getattribute__(self, name: str) -> Any:
        warnings.warn('Immutable objects have no attributes.')


class String(str):
    def __init__(self, text: str) -> None:
        super().__init__()


class Numeral():
    def __init__(self,num: Union[int,float]):
        self.num = num
        


if __name__ == '__main__':
    a = String('dsfs')
    b = String('sdf')
    print(a + b)
    print(a.upper())

    a= Numeral(3)
    a.test = 2
    print(a.test)
