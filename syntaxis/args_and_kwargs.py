def test(*args, **kwargs):
    print(f'kwargs: {kwargs}')
    print(f'args: {args}')


a = {'1': '1', '2':'2'}
test(2, 3, [4,2], {'3':'3'}, *a, **a)