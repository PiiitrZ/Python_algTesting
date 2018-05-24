

#List Comprehension (list s podminkou):
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#pouze sude:
b = [x for x in a if x % 2 == 0]

#prvni a posledni:
d = [a[0], a[len(a)-1]]

print(b)
print(d)

#vykresleni trojuhelniku
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" "),         #carka na konci rusi prechod na novy radek!
    for j in range(2 * i - 1):
        print("*"),
    print
