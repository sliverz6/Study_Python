def make_pizza(size, *toppings):
    """만들려는 피자를 요약합니다"""
    print('\nMaking a ' + str(size) + 
        '-inch pizza with the following topping:')
    for topping in toppings:
        print('-' + topping)

    