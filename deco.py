"""
def say_hello(name):
    return "Hello {}".format(name)


def wrap(func):
    return "Hello Python {}".format(func)

print(say_hello('pawel'))

print(wrap(say_hello('michal')))
"""

def get_name(name):
    return "Funkcja Bazowa {}".format(name)

def decorate(func):
    def f_wraper(jakis_arg):
        return "Wrapper {}".format(func(jakis_arg))
    return f_wraper

my_get_text = decorate(get_name)
print(my_get_text)
print(my_get_text("Dupa"))


get_name = decorate(get_name)
print(get_name("Mama"))
