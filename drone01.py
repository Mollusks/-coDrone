from codrone_edu.drone import *

drone = Drone()
drone.pair()

print("Battery:", drone.get_battery(), "%")
drone.set_drone_LED(0, 255, 0, 100)    # red, green, blue, brightness
drone.drone_buzzer(440, 500)    

drone.takeoff()
drone.hover(6)
drone.land()         # settle down

drone.close()