from dronekit import connect

def connectToVehicle():
	vehicle = connect('/dev/serial0', baud=921600, wait_ready=True,heartbeat_timeout=30)
	return vehicle