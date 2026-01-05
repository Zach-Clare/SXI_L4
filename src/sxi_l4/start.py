from cyclopts import run

def foo(loops: int):
    for i in range(loops):
        print(i)

run(foo)