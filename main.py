from dronekit import connect, VehicleMode, LocationGlobalRelative
import hareketler.alanTara as alanTarama
import hareketler.genelHareketler as genelHareketler
import insanTespit.insanTespit as insanTespit
import threading
import test
import time

def connectToVehicle():
	iha = connect('127.0.0.1:14550', wait_ready=True) # 127.0.0.1:14550 -> değiştirilecek
	return iha

# def komutDinle(iha):
# 	# Listen for `STATUSTEXT` messages
# 	@iha.on_message('STATUSTEXT')
# 	def handle_statustext_message(self, name, message):
#     	text = message.text
#     	if text.startswith("commandGCS:"):
#         	print("Received command:", text)
# 			print("2")
#     # Wait for messages
#     while True:
#         time.sleep(1)

# def komutDinle2(iha):
# 	@iha.on_message('STATUSTEXT')
# 	def handle_statustext_messages(self,name,message):
# 		text = message.text
# 		if text.startswith("commandGCS:"):
# 			print("Received Command:", text)
# 			if("alanTaraKare" in text):
# 				alanTaramaThread.start()
# 				tespitThread.start()
# 			elif("yuvarlakTara" in text):
# 				alan

# ihaya bağlan
iha = connectToVehicle()

genelHareketler.takeoff(15,iha)

alanTaramaThread = threading.Thread(target=alanTarama.alanTaraKare,args=(20,iha)) # kare -> çevre, yuvarlak -> çap veya yarıçap
tespitThread = threading.Thread(target=insanTespit.main,args=iha)


#kontrolThread
#testThread = threading.Thread(target=test.hareketiKesVeGeriGit,args=(iha,))




# konumu tanımla
konum = iha.location.global_relative_frame # -> güncel konum

# konuma git
genelHareketler.konumaGit(iha,konum)

# alanı taramaya başla.
alanTaramaThread.start()
tespitThread.start()

#time.sleep(3)
#testThread.start()

################ Yer istasyonu iletişim
yerIstasyonuThread = threading.Thread(target=komutDinle, args=iha)
yerIstasyonuThread.start()






