def nazwa_funkcji(parametr_1, parametr_2, parametr_3=10): #sygnatura funkcji
    """
    to jest docstring funkcji

    """
    print(parametr_1 + parametr_2 + parametr_3)
    # tu jestem w funkcji (zawsze po dwukropku rób wcięcie)
    return "Hello"

# tu już nie jestem w funkcji, mogę ją wywołać
nazwa_funkcji(1, 2, 3)
nazwa_funkcji(10, 20)

