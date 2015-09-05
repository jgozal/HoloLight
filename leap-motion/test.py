import Leap, sys, thread
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture,SwipeGesture

class LeapMotionListener(Leap.Listener):
    state_names = ["STATE_INVAILD","STATE_START","STATE_UPDATE", "STATE_END"]

    def on_init(self, controller):
        print "Initialized"
    def on_connect(self, controller):
        print "Connected"
        
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        print "All gestures enabled"
    def on_disconnect(self, controller):
        print "Disconnected"
    def on_exit(self, controller):
        print "Exit"
    def on_frame(self, controller):
        frame= controller.frame()
        print "\n Frame ID"+ str(frame.id)
        print "num of hands:  " +str(len(frame.hands)) 
        print "num of gestures:  " +str(len(frame.gestures()))
        for gesture in frame.gestures():
            if gesture.type is Leap.Gesture.TYPE_CIRCLE:
                circle = Leap.CircleGesture(gesture)
            elif gesture.type is Leap.Gesture.TYPE_SWIPE:
                swipe = Leap.SwipeGesture(gesture)
            elif gesture.type is Leap.Gesture.TYPE_KEY_TAP:
                key_tap = Leap.KeyTapGesture(gesture)
            elif gesture.type is Leap.Gesture.TYPE_SCREEN_TAP:
                screen_tap = Leap.ScreenTapGesture(gesture)
                
def main():
    listener= LeapMotionListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    print "Press enter to quit: " 
    
    try:
       sys.stdin.readline() 
    except KeyboardInterrupt: 
        pass        
    finally:
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
