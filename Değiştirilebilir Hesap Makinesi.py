import time
def sum(a, b):
    return (a + b)

a = int(input('Sayı Giriniz:'))
b = int(input('Sayı Giriniz:'))

print(f'{a}+{b}={sum(a, b)}')
time.sleep(1)
print('Hesap Makinesini Denediğiniz İçin Teşekkür Ederiz!')
time.sleep(4)