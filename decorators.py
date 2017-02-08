#how to decorate your output
def decor(func):
    def wrap():
        print("************************")
        func()
        print("************************")
    return wrap
def print_text():
    print("I am decorated bruh")
decorated= decor(print_text)
decorated()

