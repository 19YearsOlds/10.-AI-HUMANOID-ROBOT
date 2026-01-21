import threading
import robot_vision
import robot_speech
import robot_brain
import robot_movement


t1 = threading.Thread(target=robot_vision.run)
t2 = threading.Thread(target=robot_speech.run)
t1.start()
t2.start()


robot_brain.run()

robot_movement.run()