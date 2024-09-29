n = int(input("Введите номер камня от 3 до 20: "))
sum = str()
password = str()
print("Номер на камне: ", n)

def get_dividers ():
    dividers = list() #пустой список
    for div in range(2, n // 2): #деление
        if div in dividers:
            break
        if n % div == 0 :
            dividers.append(div)
            dividers.append(n // div)

    if 2 in dividers:
        del dividers[0]
    dividers = sorted(dividers)
    dividers.append(n)
    return dividers
print("Делители: ", get_dividers())

for i in range(1, n):
    for div in get_dividers():
        if i < div // 2+1 and i != div-i:
            sum += f"{i}+{div - i} "
            password += f"{i}{div - i}"
print("Суммы пар: ", sum)
print("Пароль: ", password)


