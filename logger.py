


def myDecorator(func):
    def wrapper(a, b=1, *args, **kwargs):
        print(f'Calling testFunc({a, b, args}), {kwargs})')
        func(a, b, *args, **kwargs)
        print(f'Finished testFunc: {a+b}')
    return wrapper



@myDecorator
def testFunc(a, b=1, *args, **kwargs):
    print(f'argument a: {a}')
    print(f'argument b: {b}')
    print(f'argument args: {args}')
    print(f'argument kwargs: {kwargs}')

    return a + b

testFunc(2, 3, 4, 5, c=6, d=7)
testFunc(2, c=5, d=6)
testFunc(10)

# def testFunc(2, 3, 4, 5, c=6, d=7):
#     print(myDecorator(func))
# def testFunc(2, c=5, d=6):
#     print(myDecorator(func))
# def testFunc(10):
#     print(myDecorator(func))

# Output should be:
# Calling testFunc((2, 3, 4, 5), {'c': 6, 'd': 7})
# argument a: 2
# argument b: 3
# argument args: 4,5
# argument kwargs: c: 6, d: 7
# Finished testFunc(5)

# Calling testFunc((2,), {'c': 5, 'd': 6})
# argument a: 2
# argument b: 1
# argument args: ()
# argument kwargs: c: 5, d: 6
# Finished testFunc(3)

# Calling testFunc((10,), {})
# argument a: 10
# argument b: 1
# argument args: ()
# argument kwargs: {}

# Finished f(11)
