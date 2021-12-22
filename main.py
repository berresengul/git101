#GDSC

#opencv ye giriş, frame yapısı ve bazı cv2 nesnelerini kullanmak
import cv2

print(cv2.__version__) #işletim sistemine indirilen opencv nin versiyonunu yazdırma

img= cv2.imread('lena.jpg', -1) #resmi okuma (name,flag) 1: renkli, 0:grayscale, -1: olduğu gibi. jpg ismini yanlış yazsak da hata almayız.


print(img) #resimdeki pixelleri matrix olarak yazdırma
cv2.imshow("image", img) #resmi göstermek
cv2.waitKey(5000) #parantez içi kadar bekle. 0 yazarsan kapanmaz
cv2.destroyAllWindows() #açık olan tüm pencereleri kapatmak
cv2.imwrite('Lena_write.png',img)#resmi içe yazdırma (img nin kopyasını oluşturduk)
"""
#-----------------------------------------------

#eğer esc ye basılırsa tüm pencereleri kaydetmede kapatan kod, s ye basılırsa yeni şekilde kaydeden kod

import cv2

img= cv2.imread('lena.jpg', -1) #resmi okuma (name,flag) 1: renkli, 0:grayscale, -1: olduğu gibi. jpg ismini yanlış yazsak da hata almayız.
k = cv2.waitKey(0)  #basılan tuşu ASCII yaptı
if k==27: #ESC nin ASCII kodu
    cv2.destroyAllWindows()
elif k == ord ('s'): #ord(keyname) içine yazılanın ASCII temsilini döndürür
    cv2.imwrite('lena_write.png',img)
    cv2.destroyAllWindows()

#--------------------------------------------------

#1- Doğrudan kameradan alınan frame i q tuşuna basarak kapatmak
# Videodan alınan frame i siyah beyaz renk aralığında almak ve aynı şekilde q tuşuna basarak kapatmak

import cv2

cap= cv2.VideoCapture (0) #Varsayılan kameradan canlı görüntü almak için varsayılan olarak 0 yazdık.
                         #Belirli bir dosyadan almak istiyorsan dosya adını yazıoruz.

while (True): #sürekli olarak frame i yakalamak için while döngüsü oluşturuyoruz (sürekli çalışacağı için ture)
    ret, frame = cap.read() #ret frame mevcutsa true değerini döndüren bir boole değişkenidir. frame available ise read method true döndürür. frame e kaydeder.

    gray = cv2.cvtColor (frame,cv2.COLOR_RGB2GRAY) #resmin renklerini dönüştürmek için kullanılır
                                                   #cv2.cvtColor (renk aralığı değişmesi istenen resim, renk skalasını dönüştürme kodu)

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #çerçeve genişliğini yazdırma
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #çerçeve yüksekliğini yazdırma

    cv2.imshow('resmin ismi', gray) #frame yazılırsa kameran okuduğumuzu, gray yazılırsa dönüştürdüğümüzü gösterir

    if cv2.waitKey(1) & 0xFF == ord('q'): #milisaniyede bir (anlık) değer almak istediğimiz için waitKey in içine 1 yazdık.
        break

cap.release() #video yakalamayı etkinleştirme
cv2.destroyAllWindows()

#----------------------------------------

#VideoCapture ın içine olmayan bir değer/dosya adı yazdığımızda False değerini döndürür.

import cv2

cap= cv2.VideoCapture ('berre.avi') #bulunmayan bir dosya adı yazdık.

print(cap.isOpened())
while (cap.isOpened()): #True yerine .isOpened de kullanabiliriz. Burda dosyamız path bulunmadığı/doğru olmdığı için False döndürmektedir.
    ret, frame = cap.read()

    gray = cv2.cvtColor (frame,cv2.COLOR_RGB2GRAY)

    cv2.imshow('resmin ismi', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#----------------------------------------------------

#videoyu kaydetme
import cv2

cap= cv2.VideoCapture (0)
forcc = cv2.VideoWriter_fourcc(*'XVID') #('X','V','I','D') şeklinde de yazılabilir. 4 baytlık veri formatlarını tanımlamak için varsayılan satır.
out= cv2.VideoWriter('output.avi',forcc, 20.0, (640,480))    #videoyu yazdırma etme ('dosya adı', fourcc,fps, çerçeve genişliği)

while (True):
    ret, frame = cap.read()
    if ret == True:

        out.write(frame) #orijinal versiyonunu yazdırdığımız için videoyu gri de yazdırsak orijinal şekilde kaydedecek.
        gray = cv2.cvtColor (frame,cv2.COLOR_RGB2GRAY)

        cv2.imshow('resmin ismi', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release() #video yakalamayı etkinleştirme
out.release() #dışa aktırmayı etkinleştirme
cv2.destroyAllWindows()

#----------------------------------------------------
#resim üstüne şekil çizme ve yazı yazma

import numpy as np
import cv2

img = np.zeros([512,512,3], np.uint8) #yalnızca sıfır içeren Numpy dizileri oluşturduk
                                      # yükseklik, genişlik, renk sayısı (1(gray) ya da 3 (BGR)), veri tipi

#img = cv2.imread('lena.jpg', -1)
img = cv2.line(img, (0,0), (255,255), (5,125,50), 5) #çizgi oluşturma .line(resim, başlangıç koordinat, bitiş koordinat, renk (B,G,R), kalınlık)
img = cv2.arrowedLine(img, (0,50), (50,255), (125,20,200), 5) #ışın çizme
img = cv2.rectangle (img, (384,0), (510,128 ),(0,0,255), 3) # kare oluşturma .rectangle(resmin ismi, sol üst koordinat, sağ alt koordinat, kalınlık)
                                                            # - değer yazılırsa iç dolgusu o renge döner


img = cv2.circle (img, (447,63), 63, (0,255,50), -1) # .circle (resim, merkez koordinat, yarıçap, renk, kalınlık)


#Gülen yüz çizme çalışmam :)
img = cv2.ellipse (img,(256,256),(100,80),60,360,0,(255, 255, 255), 2, cv2.LINE_AA) #elips çizmek
                                #.ellipse (resim, merkez, axes, açı,başlangıç açısı, bitiş açısı, renk,kalınlık, line tipi)
img = cv2.circle (img, (240,240), 10, (255,120,100), -1) # .circle
img = cv2.circle (img, (300,230), 10, (255,120,100), -1)
img = cv2.ellipse (img,(256,256),(50,40),60,60,0,(0, 0, 255), 2, cv2.LINE_AA) #elips çizmek


font = cv2.FONT_ITALIC #font seçip atadık
img = cv2.putText(img, 'METUrone', (10,500), font, 2, (255,255,255), 2, cv2.LINE_4 )
                #.putText(resim, yazı, başlangıç koordinatı, font, boyut, renk, kalınlık, çizgi tipi)

print(img)
cv2.imshow("image", img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
cv2.imwrite('Lena_write.png',img)

#--------------------------

#video ekranının boyutunu değiştirme, kameradan alınan canlı videoya yazı, şekil ve zaman ekleme

from cv2 import cv2
import datetime

cap= cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1000) # 3 genişlik parametresini temsil ediyor
cap.set(4, 720) # 4 yükseklik parametresini temsil ediyor

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()): #veya true
    ret, frame = cap.read()

    if ret== True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4)) #yükseklik ve genişliği yazdıracağımız bir metin oluşturduk
        dateT = str(datetime.datetime.now()) #şimdiki tarihi ve zamanı yazdırmak için stringe çevirdik
        frame = cv2.putText(frame, dateT, (10,400), font, 1, #dateT yerine text yazarsak yükseklik&genişlik gösteriyor
                            (0,255,255), 3, cv2.LINE_AA)
        frame = cv2.ellipse(frame, (256, 390), (300, 60), 0, 360, 0, (255, 255, 255), 2, cv2.LINE_AA) #ifadeyi elips içine alma
        cv2.imshow('resmin ismi', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

#------------------------------------------

#mouse events sonraki ödevde gelecek
"""
