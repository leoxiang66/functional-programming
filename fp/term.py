x = 'x'
y = 'y'
z = 'z'

a = 0

inc = lambda x: x + 1

true = lambda x, y : x
false = lambda x, y : y
if_ =  lambda z,x,y: z(x,y)

fst = lambda p: p(true)
snd = lambda p: p(false)
pair = lambda x,y : lambda z: z(x,y)

def n_temp (n, f, x):
    tmp = x
    for i in range(n):
        tmp  = f(tmp)
    return tmp

n_ = lambda n : lambda f: lambda x: n_temp(n,f,x)


succ= lambda n: lambda f,x : f(n_temp(n, f, x))

add= lambda m,n: lambda f,x: n_temp(m, f, n_temp(n, f, x))

iszero= lambda n: n_temp(n, lambda x: false, true)


if __name__ == '__main__':
    print(fst(pair(x,y)))

    print(if_(false, x, y))

    print(succ(3)(inc,a) == 4)

    print(add(3,2)(inc,a) == 5)

    print(iszero(0)(1,2))

