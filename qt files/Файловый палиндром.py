def palindrome():
    with open('input.dat', mode='rb') as fi:
        data = fi.read()
        n = int(len(data) / 2)
        print(data[: n])
        print(data[-1 : n : -1])
        print(data)
        reverse_data = data[::-1]
        fi.close()
        if data == reverse_data :
            return True
        return False


print(palindrome())
