m = int(input('輸入三位數字 : '))
a = m // 100
b = (m % 100) // 10
c = m % 10

a,c = c,a

print('結果 :',a * 100 + b * 10 + c)