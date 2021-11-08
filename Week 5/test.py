from PythonDebuggerTools.logger import Debug, Log


D = Debug()
add_log = Log()
add_log.DEBUG = False

@D.logger(important_params=['n'])
def add_two(n):
    return n + 2

@D.logger()
def add(x, y):
    add_log.log("Test statement")
    print(locals())
    x = 1
    print(locals())
    return add_two(x) + add_two(y)

def main():
    add(4, 5)

if __name__ == "__main__":
    main()