import datetime

gun = int(input("Sınav günü "))
ay = int(input("Sınav ayı "))
yil = int(input("Sınav yılı "))
saat = int(input("Sınav saatini giriniz: "))

sinav = datetime.datetime(yil, ay, gun, saat)
simdi = datetime.datetime.now()

kalan = sinav - simdi

print("vizelere kalan zaman   : ", kalan.days ,"gün", kalan.seconds // 3600 , "saat")
## kalan.seconds sadece günden artakalan saniyeleri hesaplıyor  
## .total_seconds() bu bütün saniyeleri veriyor



