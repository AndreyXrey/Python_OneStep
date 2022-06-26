def total(a=5, *numbers, **phonebook):
    print("a", a)

    # подход ко всем элементам кортежа
    for single_item in numbers:
        print("single_item", single_item)

    # подход по всем элементам словаря
    for first_part, second_psrt, in phonebook.items():
        print(first_part, second_psrt)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=8789))
