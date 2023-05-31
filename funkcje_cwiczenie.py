a = input("Podaj argument 1: ")
b = input("Podaj argument 2: ")
input3 = input("Podaj dzialanie +-*/: ")

a = int(a)
b = int(b)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

if input3 == "+":
    print(add(a, b))
elif input3 == "-":
    print(sub(a, b))
elif input3 == "*":
    print(mult(a, b))
elif input3 == "/":
    print(div(a, b))
else:
    print("Nie ma takiego dzialania")

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2 and sys.argv[1] == 'test':

        assert add(0, 0) == 0
        assert sub(8, 1) == 7
        assert mult(5, 5) == 25
        assert div(24, 4) == 6

    print("OK")
elif len(sys.argv) == 1:
    main()
else:
    print("Niepoprawne wywołanie skryptu. Wpisz 'test'")
