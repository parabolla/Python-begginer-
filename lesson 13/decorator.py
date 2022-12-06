def decorat(func):
    def wrap(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("stop")

    return wrap


@decorat
def calc(a, b):
    print(a + b)


calc(10, 16)
