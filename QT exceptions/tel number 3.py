def check_number(num):
    try:
        if '--' in num or num[0] == '-' or num[-1] == '-':
            raise ValueError("неверный формат")
        num = ''.join(num.split(' '))
        num = ''.join(num.split('-'))
        if num[0] != '8' and num[0] != '+':
            raise ValueError("неверный формат")
        if num[0] == '8':
            num = "+7" + num[1:]
        x = num.find('(')
        y = num.find(')')
        if x + y != -2:
            if x > -1 and y > -1:
                num = num[:x] + num[x + 1:]
                num = num[:y - 1] + num[y:]
                # num = num[:x] + num[x + 1:y] + num[y + 1:]

                if num.find('(') >= 0 or num.find(')') >= 0:
                    raise ValueError("неверный формат")
            raise ValueError("неверный формат")

        print(num)
        print(len(num))
        if len(num) == 12:
            return num

        raise ValueError("неверное количество цифр")

    except ValueError as e:
        return e


phone_number = input()
print(check_number(phone_number))