from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
import time
from pymavlink import mavutil
import math

# constants
BUYUK_ADIM = 0.00009 # 10 metre
KUCUK_ADIM = 0.000045 # 5 metre

HAREKET_SABITI = 0.00001 # 1.1 metre


def velocity(velocity_x, velocity_y,yaw_rate,velocity_z, iha):
    # maksimum 3 saniye
    msg = iha.message_factory.set_position_target_local_ned_encode(0, 0, 0, mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 0b0000011111000111, 0, 0, 0, velocity_x, velocity_y, velocity_z, 0, 0, 0, 0, math.radians(yaw_rate))
    iha.send_mavlink(msg)

def konumaGit(iha,konum):
    iha.simple_goto(konum)

def takeoff(altitude,iha):

    iha.mode = VehicleMode("GUIDED")

    iha.armed = True

    while iha.armed is not True:
        print("Vehicle is arming...")
        time.sleep(0.5)
    

    iha.simple_takeoff(altitude)

    while iha.location.global_relative_frame.alt < altitude * 0.9:
        print("Altitude is %s" % iha.location.global_relative_frame.alt)
        time.sleep(1)        
    
    time.sleep(1)

def dur(iha):
    iha.mode=VehicleMode("BRAKE") # ? ? 
def eveDon(iha):
    iha.mode=VehicleMode("RTL") # değiştirilebilir

def ileri(iha):
    velocity(5,0,0,0,iha)
    time.sleep(2)
def geri(iha):
    velocity(-5,0,0,0,iha)
    time.sleep(2)

def saga(iha):
    velocity(0,5,0,0,iha)
    time.sleep(2)
def sola(iha):
    velocity(0,-5,0,0,iha)
    time.sleep(2)

def yukari(iha):
    velocity(0,0,0,-2,iha)
    time.sleep(2)

def asagi(iha):
    velocity(0,0,0,2,iha)
    time.sleep(2)

def don(iha):
    velocity(0,0,60,0,iha)
    time.sleep(2)