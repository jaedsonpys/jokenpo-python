from random import choice
from time import sleep

options = ['Pedra', 'Papel', 'Tesoura']


def random_choice():
    return choice(options)


def get_result(cmp: str, user: str):
    print('=-' * 5)
    print(f'Computador: {cmp} X Você: {user}')

    if cmp == user:
        print('\033[1;34mEmpate!\033[m')
    elif cmp == 'Papel' and user == 'Pedra':
        print('\033[1;31mVocê perdeu!\033[m')
    elif cmp == 'Pedra' and user == 'Papel':
        print('\033[1;32mVocê venceu!\033[m')
    elif cmp == 'Pedra' and user == 'Tesoura':
        print('\033[1;31mVocê perdeu!\033[m')
    elif cmp == 'Tesoura' and user == 'Pedra':
        print('\033[1;32mVocê venceu!\033[m')
    elif cmp == 'Tesoura' and user == 'Papel':
        print('\033[1;31mVocê perdeu\033[m')
    elif cmp == 'Papel' and user == 'Tesoura':
        print('\033[1;32mVocê venceu!\033[m')


def menu():
    print('-='*5)
    print('Jokenpô')
    print('-='*5)

    print('[ 1 ] Pedra')
    print('[ 2 ] Papel')
    print('[ 3 ] Tesoura')
    print('[ 4 ] Sair\n')

    while True:
        user_option = input('Sua escolha: ').strip()

        if user_option.isnumeric():
            user_option = int(user_option)
            
            if not user_option <= 4:
                print('\033[31mOpção inexistente\033[m')
                continue

            if user_option == 4:
                print('-=' * 5)
                print('Bye!')

                sleep(1)
                exit(0)

            computer_choise = random_choice()

            if user_option == 1:
                get_result(computer_choise, 'Pedra')
            elif user_option == 2:
                get_result(computer_choise, 'Papel')
            elif user_option == 3:
                get_result(computer_choise, 'Tesoura')

            sleep(1)
            menu()
        else:
            print('\033[31mSua opção precisa ser um número.\033[m')
            continue


menu()
