def harf_notu_hesapla():
    vize_notu = float(input("Vize notunu giriniz     :"))
    final_notu = float(input("Final notunu giriniz    :"))

    ortalama = (vize_notu * 0.4) + (final_notu * 0.6)

    if ortalama >= 85:
        harf_notu = "AA"
    elif ortalama >= 80:
        harf_notu = "BA"
    elif ortalama >= 75:
        harf_notu = "BB"
    elif ortalama >= 70:
        harf_notu = "BC"
    elif ortalama >= 65:
        harf_notu = "CC"
    elif ortalama >= 60:
        harf_notu = "CD"
    else:
        harf_notu = "FF"

    print("Ortalama:", ortalama)
    print("Harf Notu:", harf_notu)

harf_notu_hesapla()
