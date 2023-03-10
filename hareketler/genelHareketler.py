from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
import time
from pymavlink import mavutil
import math

# constants
BUYUK_ADIM = 0.00009 # 10 metre
KUCUK_ADIM = 0.000045 # 5 metre

HAREKET_SABITI = 0.00001 # 1.1 metre

def velocity(velocity_x, velocity_y,yaw_rate,velocity_z, iha):
	msg = iha.message_factory.set_position_target_local_ned_encode(0, 0, 0, mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 0b0000011111000111, 0, 0, 0, velocity_x, velocity_y, velocity_z, 0, 0, 0, 0, math.radians(yaw_rate))
    

def velocity2(velocity_x, velocity_y,yaw_rate,velocity_z, iha):
    # maksimum 3 saniye
    msg = iha.message_factory.set_position_target_local_ned_encode(0, 0, 0, mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 0b0000011111000111, 0, 0, 0, velocity_x, velocity_y, velocity_z, 0, 0, 0, 0, math.radians(yaw_rate))
    iha.send_mavlink(msg)

def konumaGit(iha,konum):
    iha.simple_goto(konum)

def dur(iha):
    iha.mode.name("BRAKE") # ? ? 
def eveDon(iha):
    iha.mode.name("RTL")

def ileri(iha):
    velocity2(5,0,0,0,iha)
    time.sleep(2)
def geri(iha):
    velocity2(0,-5,0,0,iha)
    time.sleep(2)

def saga(iha):
    velocity2(0,5,0,0,iha)
    time.sleep(2)
def sola(iha):
    velocity2(0,-5,0,0,iha)
    time.sleep(2)

def yukari(iha):
    velocity2(0,0,0,-2,iha)
    time.sleep(2)

def asagi(iha):
    velocity2(0,0,0,2,iha)
    time.sleep(2)



def don(iha):
    velocity(0,0,60,0,iha)
    time.sleep(2)