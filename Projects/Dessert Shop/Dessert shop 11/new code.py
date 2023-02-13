import desserts
import freeze
import combine
import payment

def main():
    user_input = input(
        '''
Would you like to make another order? [y/n]
'''
    )
    if (str(user_input) == 'y'):
        main()


main()

