a = int(input('輸入係數 a : '))
b = int(input('輸入係數 b : '))
c = int(input('輸入係數 c : '))


x1 = (-b + (b**2 - 4 * a * c)**(1/2)) / (2 * a)
x2 = (-b - (b**2 - 4 * a * c)**(1/2)) / (2 * a)

print('方程式的根為 : x1 =',x1,end='')
print(', x2 =',x2)