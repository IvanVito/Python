import random
def start():
    num_slave = int(input("Choose your desteny:")) 
    num_master = random.randint(1, 100)
    print('Welcome to the dungeon, slave')
    return num_slave, num_master

def is_valid(num):
    if 0 < num < 101 and num == int(num):
        return True
    else:
        return False
    
def main_body(num_slave, num_master):
    quantity_tries = 1
    max_n = 100
    min_n = 1
    
    while is_valid(num_slave) == False:
        print("Stick finger in your A$$")
        num_slave = int(input("Choose your desteny right:"))

    if is_valid(num_slave) == True:
        print("That's good number")
        
    while num_slave != num_master:
        quantity_tries += 1
        
        if num_slave < num_master and quantity_tries != 2:
            if num_slave >= min_n and max_n >= num_slave:
                min_n = num_slave             
            print("Take up, slave")
            print("Choose your desteny in range:", min_n, '-', max_n)

        if quantity_tries != 2 and num_slave > num_master:
            if num_slave >= min_n and max_n >= num_slave:
                max_n = num_slave            
            print("Take down, daun")
            print("Choose your desteny in range:", min_n, '-', max_n)
            
        flag = False
        while flag == False:   
            if quantity_tries == 2 and num_slave < num_master:
                print('Take up, slave. Choose number from  of the range',
                      num_slave, '- 100')
                min_n = num_slave
                num_slave = int(input())
                while not (101 > num_slave > min_n):
                    print('Choose number from  of the range', min_n, '- 100')
                    num_slave = int(input())
                flag = True
            elif quantity_tries == 2 and num_slave > num_master:
                print('Take down, daun. Choose number from  of the range',
                      '1 -', num_slave)
                max_n = num_slave
                num_slave = int(input())
                while not (1 < num_slave < max_n):
                    print('Choose number from  of the range', '1 -', max_n)
                    num_slave = int(input())
                flag = True
            else:
                num_slave = int(input())
                if min_n < num_slave < max_n:
                    flag = True
                else:
                    print('Choose number from  of the range', min_n, '-', max_n)
                
    return print("You've  become   master, congratulation!", '\n', 'Quantity of tries =', quantity_tries)

def end():
    print('Do you want to play again ? (Y or N)')
    again = input()
    while again != 'Y' and again != 'N':
        again = input('Just "Y" or "N" :')
    return again
    
a, b = start()
is_valid(a)
main_body(a, b)

while end() == 'Y':
    a, b = start()
    is_valid(a)
    main_body(a, b)
else:
    print('Good Game. See you soon')
      





