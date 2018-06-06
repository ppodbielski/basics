def name(arg):
    return "Name: {}".format(arg)

print(name("Pawel"))

def deco(function):
    def wrapper(arg):
        return "Dekorator + {}".format(function(arg))
    return wrapper

name = deco(name)
print(name("Pawel"))


@deco
def name(arg):
    return "Name: {}".format(arg)

print(name("Pawel"))


def inna_funkcja():
    print("inna funkcja")
print(inna_funkcja())

def dekorator(obj):
    return inna_funkcja


@dekorator
def funkcja():
    print("hello")

funkcja()

def frac(arg):
    r = 1
    for i in range(1,arg+1):
        r =i
    return r
print(frac(10))