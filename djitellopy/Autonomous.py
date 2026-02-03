from djitellopy import Tello

tello = Tello()
tello.connect()

tello.takeoff()
# tello.move_up(50)
tello.move_forward(100)

tello.land()