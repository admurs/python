ogrenciler=["darth vader","obi wan","darth maul"]

def ogrenciListele():
     print("Öğrenci Listesi:")
     for ogrenci in ogrenciler:
        print(ogrenci) 

def ogrenciEkle():
    isim=input("Öğrenci adı: ")
    soyIsim=input("Öğrenci soyadı: ")
    ogrenciler.append(isim+" "+soyIsim)
    print(isim+" "+soyIsim+" eklendi")
    ogrenciListele()

def ogrenciSilme():
    isim=input("Silinecek öğrenci adı: ")
    soyIsim=input("Silinecek öğrenci soyadı: ")    
    for ogrenci in ogrenciler:
        if(ogrenci==isim+" "+soyIsim):
            ogrenciler.remove(isim+" "+soyIsim)
            print(ogrenci+" silindi")
            if(len(ogrenciler)==0):
                print("Liste Boş")
            else:
                ogrenciListele()
            break
        else:
            print(isim+" "+soyIsim+" listede bulunmamaktadır")
            ogrenciListele()
            break
           
def cokluOgrenciEkle():
    i=1
    while True:
        isim=input(str(i)+" Öğrenci adı: ")
        soyIsim=input(str(i)+" Öğrenci soyadı: ")
        ogrenciler.append(isim+" "+soyIsim)
        i+=1
        while True: 
            karar=input("Öğrenci eklemeye devam edecekmisiniz(E/H): ")
            if(karar!="E")and(karar!="e")and(karar!="H")and(karar!="h"):
                print("Hatalı Seçim")
                continue
            else:
                break
        if(karar=="E")or(karar=="e"):
            continue
        elif(karar=="H")or(karar=="h"):
            break                          
    ogrenciListele()    

def ogrenciNumara():
    isim=input("Öğrenci adı: ")
    soyIsim=input("Öğrenci soyadı: ")
    for i in range(len(ogrenciler)):
        if(ogrenciler[i]==isim+" "+soyIsim): 
            numara=i
            break
    print(isim+" "+soyIsim+f" numarası: {numara+1}")

def cokluOgrenciSilme():
    mevcut=False    
    ogrenciListele()
    while True:
        isim=input("Silinecek öğrenci adı: ")
        soyIsim=input("Silinecek öğrenci soyadı: ")
        for ogrenci in ogrenciler:
            if(ogrenci==isim+" "+soyIsim):
                mevcut=True
        if(mevcut):
            ogrenciler.remove(isim+" "+soyIsim)
            print(isim+" "+soyIsim+" silindi")
        elif(mevcut==False):
            print("Öğrenci yok")
        while True:
            karar=input("Öğrenci silmeye devam edecekmisiniz(E/H): ")
            if(karar!="E")and(karar!="e")and(karar!="H")and(karar!="h"):
                print("Hatalı Seçim")
                continue
            else:
                break
        if(karar=="E")or(karar=="e"):
            if(len(ogrenciler)==0):
                print("Liste Boş")
                break
            else:
                continue             
        elif(karar=="H")or(karar=="h"):
            ogrenciListele() 
            break     

# ogrenciEkle()
# ogrenciSilme()
# cokluOgrenciEkle()
# ogrenciNumara()
# cokluOgrenciSilme()
print("1-)Öğrenci Ekleme\n2-)Öğrenci Silme\n3-)Coklu Öğrenci Ekleme\n4-)Öğrenci Numarası Öğrenme\n5-)Çoklu Öğrenci silme")
islem=int(input("Hangi İşlemi Yapmak İstiyorsunuz: "))
if(islem==1):
    ogrenciEkle()
elif(islem==2):
    ogrenciSilme()
elif(islem==3):
    cokluOgrenciEkle()
elif(islem==4):
    ogrenciNumara()
elif(islem==5):
    cokluOgrenciSilme()
else:
    print("Hatalı seçim. Yeniden başlatın.")
