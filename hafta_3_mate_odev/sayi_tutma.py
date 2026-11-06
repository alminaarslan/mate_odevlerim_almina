import random
tuttugum_sayi = random.randint(1, 100)
while True:
    tahmin = int(input("Tahmininizi giriniz: "))

    if tahmin < tuttugum_sayi:
        print("Yukarı çık")
    
    elif tahmin > tuttugum_sayi:
        print("Aşağı in")
    
    else:
        print("Tahmin doğru ")
        break
