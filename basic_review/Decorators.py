def hello(name='Atsuki'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

    if name =="Atski":
        return greet()
    else:
        return welcome()

def hello2():
    return 'Hi Mii!'

def other(func):
    print('Other code would go here')
    print(func())

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()