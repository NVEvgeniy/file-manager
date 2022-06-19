# Банковский счет
import os
import pickle

def actions_with_account():
    FILE_ACCOUNT = 'account_pickle.data'
    FILE_PURCHASE = 'my_purchase_pickle.data'

    account = 0
    my_purchase = {}

    if os.path.exists(FILE_ACCOUNT):
        with open(FILE_ACCOUNT, 'rb') as f:
            account = pickle.load(f)
    if os.path.exists(FILE_PURCHASE):
        with open(FILE_PURCHASE, 'rb') as f:
            my_purchase = pickle.load(f)


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')


        choice = input('Выберите пункт меню: ')
        if choice == '1':
            #
            amount = int(input('Введите сумму, на которую вы бы хотели пополнить счет: '))
            account += amount
            print(f'На вашем счете: {account}')
            with open(FILE_ACCOUNT, 'wb') as f:
                pickle.dump(account, f)

        elif choice == '2':
            print(f'На вашем счете {account}')
            price = int(input('Введите сумму покупки: '))
            if account >= price:
                purchase = str(input('Введите название покупки: '))
                my_purchase[purchase] = price
                account -= price
                with open(FILE_ACCOUNT, 'wb') as f:
                    pickle.dump(account, f)
                with open(FILE_PURCHASE, 'wb') as f:
                    pickle.dump(my_purchase, f)

            elif account < price:
                print('На вашем счете недостаточно средств')
            print(f'На вашем счете доступно: {account}')

        elif choice == '3':
            for key, value in my_purchase.items():
                print(f'{key} - {value}')
            with open(FILE_PURCHASE, 'wb') as f:
                pickle.dump(my_purchase, f)

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню: ')

actions_with_account()