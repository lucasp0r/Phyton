from collections import namedtuple
import functools


Blah=namedtuple('Blah', 'bar foo')


OutroBlah = Blah

blah = Blah('Bar', 'Foo')

print(blah.bar)
print(blah.foo)



def decorator(fcn):
    def interna(*args, **kwargs):
        print('Vou Executar fcn')
        resutaldo = fcn(*args, **kwargs)
        print('Terminei de executar fcn')
        return resutaldo

    return functools.update_wrapper(interna, fcn)


# f = decorator(f)
@decorator
def f():
    return 'Função Decorada'



print(f())
print(f)
print(type(Blah))
print(type(OutroBlah))
print(OutroBlah is Blah)
