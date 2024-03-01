#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print("Pilihan:")
print("1. FPB")
print("2. KPK")
print("3. Other")

while True:
    choice = int(input("Masukkan pilihan anda (1/2/3): "))

    if choice == 1:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        print("Hasil FPB dari", a, "dan", b, "adalah", gcd(a, b))
        break

    elif choice == 2:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        print("Hasil KPK dari", a, "dan", b, "adalah", lcm(a, b))
        break

    elif choice == 3:
        print("Program dihentikan.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")


# In[ ]:




