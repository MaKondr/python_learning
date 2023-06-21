def foo(a=1, b=2, *, no_name=None):
    print(f"no_name: {no_name}, {a}:{b}")


a = 10
b = 20
foo(a, b, no_name='YES')
foo(no_name='NO')
foo()
