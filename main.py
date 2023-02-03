from dronekit import connect
import hareketler.alanTara as alanTarama
import hareketler.genelHareketler as genelHareketler

import insanTespit.insanTespit as insanTespit
import threading
import test

def connectToVehicle():
	iha = connect('/dev/serial0', baud=921600, wait_ready=True,heartbeat_timeout=30)
	return iha

# ihaya bağlan
iha = connectToVehicle()

alanTaramaThread = threading.Thread(target=alanTarama.alanTaraKare,args=20) # kare -> çevre, yuvarlak -> çap veya yarıçap
#tespitThread = threading.Thread(target=insanTespit.main,args=iha)

testThread = threading.Thread(target=test,args=iha)




# konumu tanımla
konum = iha.location.global_relative_frame # -> güncel konum

# konuma git
genelHareketler.konumaGit(iha,konum)

# alanı taramaya başla.
alanTaramaThread.start()
#tespitThread.start()
testThread.start()





