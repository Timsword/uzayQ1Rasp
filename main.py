
import baglanti.baglan as baglanti
import hareketler.alanTara as alanTarama
import hareketler.genelHareketler as genelHareketler

import insanTespit.insanTespit as tespit
import threading



alanTaramaThread = threading.Thread(target=alanTarama.alanTaraKare,args=20) # kare -> çevre, yuvarlak -> çap veya yarıçap
tespitThread = 2 #threading.Thread(target=func,args=)


# ihaya bağlan
iha = baglanti.connectToVehicle()

# konumu tanımla
konum = iha.location.global_relative_frame # -> güncel konum

# konuma git
genelHareketler.konumaGit(iha,konum)

# alanı taramaya başla.
alanTaramaThread.start()
tespitThread.start()





