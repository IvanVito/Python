from math import pow
def start():
    Num = input('Введите число, которое хотите перевести: ')
    num = list(Num)
    num_start = int(input('Из какой системы счисления: '))
    num_end = int(input('В какую систему счисления: '))
    return Num, num, num_start, num_end

def to_10(num, num_start):
    count = 0
    num_10 = 0
    for i in range(- 1, - len(num) - 1, - 1):
        if num[i].isalpha():
            num[i] = int(num[i], num_start)
        num_10 += int(num[i]) * int(pow(num_start, count))
        count += 1
    return int(num_10)

def from_10(num, num_end):
    To_10 = []
    while num >= num_end:
        remains = num % num_end
        num //= num_end
        if remains > 9:
            remains = hex(remains)[2::].upper()
        To_10.append(str(remains))
        if num < num_end:
            To_10.append(str(num))
    num_other = ''.join(To_10[::-1])
    return num_other

again = 'да'
while again == 'да':
    Num, num, num_start, num_end = start()
    print('Число', Num, 'из', num_start, 'системы счисления в',
      num_end, 'будет', from_10(to_10(num, num_start), num_end))
    again = input('Перевести еще одно число ?').lower()
