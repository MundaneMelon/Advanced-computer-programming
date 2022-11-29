from desserts import *

def main():
    candy = Candy('Hersheys', 3, 100)
    print(candy.calculate_cost())
    print(candy.calculate_tax())

main()