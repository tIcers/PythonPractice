"""In simple terms, the idea of scope can be described by 3 general rules:

Name assignments will create or change local names by default.
Name references search (at most) four scopes, these are:
local
enclosing functions
global
built-in
Names declared in global and nonlocal statements map assigned names to enclosing module and function scopes.
The statement in #2 above can be defined by the LEGB rule.

LEGB Rule:

L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,..."""

name = 'this is a global variable'


def greet():
    name = 'Atsuki'

    def hello():
        # name = 'i am local'
        print('hello ' + name)

    hello()


greet()

x = 50


def func(x):
    print(f'X is {x}')

    x = 200
    print(f'I just locally changed x to {x}')


func(x)
