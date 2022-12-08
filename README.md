# functional-programming
1. `pip install fun2py`
2. 
    ```python
    import fun2py
    from fun2py.interface import val
    from fun2py.IO import read_input

    if __name__ == '__main__':
        li1 = fun2py.List([1, 2, 3, 4])
        li2 = fun2py.List([2, 3, 4, 5])

        def elementwise_add(li1,li2):
            tmp = []
            for i in range(len(li1)):
                tmp.append(li1[i] + li2[i])
            return fun2py.List(tmp)

        print(elementwise_add(li1,li2))

    ```
