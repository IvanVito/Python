import random
def start():
    num_slave = input("Choose your desteny in range 1...100: ")
    while num_slave.isdigit() == False or not (0 < int(num_slave) < 101):
        num_slave = input("Choose your right in range 1...100: ")
    num_slave = int(num_slave)
    print("That's good number")
    num_master = random.randint(1, 100)
    print('Welcome to the dungeon, slave')
    return num_slave, num_master

def main_body(num_slave, num_master):
    quantity_tries = 1
    max_n = 100
    min_n = 1

    while num_slave != num_master:
        quantity_tries += 1
        
        if num_slave < num_master and quantity_tries != 2:
            if num_slave >= min_n and max_n >= num_slave:
                min_n = num_slave             
            print('Take up, slave.', end = '')

        if quantity_tries != 2 and num_slave > num_master:
            if num_slave >= min_n and max_n >= num_slave:
                max_n = num_slave            
            print('Take down, dawn.', end='')
            
          
        if quantity_tries == 2 and num_slave < num_master:
            min_n = num_slave
            while str(num_slave).isdigit() == False or not (101 > int(num_slave) > min_n):
                print('Take up, slave.Choose number in the range', min_n, '- 100')
                num_slave = input()
            num_slave = int(num_slave)

        elif quantity_tries == 2 and num_slave > num_master:
            max_n = num_slave
            while str(num_slave).isdigit() == False or not (1 < int(num_slave) < max_n):
                print('Take down, daun.Choose number in the range', '1 -', max_n)
                num_slave = input()
            num_slave = int(num_slave)
        else:
            while str(num_slave).isdigit() == False or not(min_n < int(num_slave) < max_n):
                print('Choose number in the range', min_n, '-', max_n)
                num_slave = input()
            num_slave = int(num_slave)
    return print("You've  become   master, congratulation!", '\n', 'Quantity of tries =', quantity_tries)

def end():
    print('Do you want to play again ? (Y or N)')
    again = input()
    while again != 'Y' and again != 'N':
        again = input('Just "Y" or "N" :')
    return again

main_body(*start())

while end() == 'Y':
    main_body(*start())
else:
    print('Good Game. See you soon')
      





