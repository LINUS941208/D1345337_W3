m = int(input('請輸入一個五位數 :'))
a = m // 10000
b = (m % 10000) // 1000
c = (m % 1000) // 100
d = (m % 100) // 10
e = m % 10
print('結果 :')
print(a)
print(b)
print(c)
print(d)
print(e)