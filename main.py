from sys import exit
from time import ctime

def get_number_input(prompt):
    value = None
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value
        except KeyboardInterrupt:
            exit()

        except ValueError as e:
            print('invalid input!')
            print(ctime(),e, file=ERROR_FILE)

def main():
    while True:
        client_name = input('what is the customer\'s name?: ')
        if not client_name:
            break

        while True:
            product_name = input('what is the product name?: ')
            if not product_name:
                break
            product_qty = get_number_input(f'How many {product_name} purchased?: ')
            product_price = get_number_input(f'How much is {product_name}?: ')
            

if __name__ == '__main__':
    
    #SUPERGLOBALS
    ERROR_FILE = open('error_log.txt','a')

    #the main code
    main()
    
    #close file
    ERROR_FILE.close()
    
