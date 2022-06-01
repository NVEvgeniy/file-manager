# Банковский счет

def actions_with_account():
    my_account = 0
    purchase_all = {}

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')



        choice = input('Выберите пункт меню: ')
        if choice == '1':
            account = int(input('Введите сумму, на которую вы бы хотели пополнить счет: '))
            my_account += account
            print(f'На вашем счете: {my_account}')

        elif choice == '2':
            my_purchase = int(input('Введите сумму покупки: '))
            if my_account >= my_purchase:
                purchase = input('Введите название покупки: ')
                purchase_all[purchase] = my_purchase
                my_account -= my_purchase
            elif my_account < my_purchase:
                print('На вашем счете недостаточно средств')
            print(f'На вашем счете доступно: {my_account}')

        elif choice == '3':
            for key, value in purchase_all.items():
                print(f'{key} - {value}')

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню: ')

actions_with_account()