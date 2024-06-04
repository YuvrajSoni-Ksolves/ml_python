first_name = "yuvraj"
last_name = "soni"
print(first_name.isdigit())
print(True and False)
a = []
print(type(a))

for i in 'yuvraj':
    a.append(i)
print(a[-2:-5:-1])
print(a[1:])
b = (i for i in "yuvraj")
a.append([x for x in b])
print(a)

a.extend(b)
a.extend(['y', 'u'])

print(a)
print(a.count('y'))
print("hello")
print(a*2)
print(min(a))
print(max(a))
print("hello")
