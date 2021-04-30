from rplidar import RPLidar
import time
lidar = RPLidar('/dev/ttyUSB0',256000)

info = lidar.get_info()
print(info)

print ("starting spinning .......\n")
time.sleep(5)
print ("scanning started")

try:
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            #scan_data[min([359, floor(angle)])] = distance
            if (angle > 350.0 and angle < 359.9 and distance < 400) :
                print ("Frontal")
                print ("\n")

            if (angle > 90.0 and angle < 91.0 and distance < 400) :
                print ("Left")
                print ("\n")
                
            if (angle > 270.0 and angle < 271.0 and distance < 400) :
                print ("Right")
                print ("\n")


except KeyboardInterrupt:
    print('Stoping.')
      
lidar.stop()
lidar.stop_motor()
lidar.disconnect()