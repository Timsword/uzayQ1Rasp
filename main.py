from dronekit import connect
import hareketler.alanTara as alanTarama
import hareketler.genelHareketler as genelHareketler

#import insanTespit.insanTespit as insanTespit
import threading
import test
import time

def connectToVehicle():
	iha = connect('127.0.0.1:14550', wait_ready=True)
	return iha

# ihaya bağlan
iha = connectToVehicle()

genelHareketler.takeoff(15,iha)

alanTaramaThread = threading.Thread(target=alanTarama.alanTaraKare,args=(20,iha)) # kare -> çevre, yuvarlak -> çap veya yarıçap
#tespitThread = threading.Thread(target=insanTespit.main,args=iha)

testThread = threading.Thread(target=test.hareketiKesVeGeriGit,args=(iha,))




# konumu tanımla
konum = iha.location.global_relative_frame # -> güncel konum

# konuma git
genelHareketler.konumaGit(iha,konum)

# alanı taramaya başla.
alanTaramaThread.start()
#tespitThread.start()
time.sleep(3)
testThread.start()





