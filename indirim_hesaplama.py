def indirim_hesapla():
    urun_fiyati = float(input('ürünün fiyatini giriniz    :'))
    indirim_yuzdesi = float(input('indirim yüzdesini giriniz    :'))

    indirim_tutari= urun_fiyati * indirim_yuzdesi /100
    indirimli_fiyat = urun_fiyati - indirim_tutari

    print('indirim tutari   :' , indirim_tutari)
    print('indirimli fiyat      :' , indirimli_fiyat)
indirim_hesapla()