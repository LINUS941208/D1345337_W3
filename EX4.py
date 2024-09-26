m = int(input('請輸入一個三位數 : '))
a = m // 100
b = (m % 100) // 10
c = m % 10

print('每位數字的總和 :',a + b + c)