import time
import appdaemon.appapi as appapi
 
class Alarm(appapi.AppDaemon):
      
    def initialize(self): 
        self.listen_state(self.what_we_want_to_do,"sensor.vision_zp3102_pir_motion_sensor_alarm_level")


    def what_we_want_to_do (self, entity, attribute, old, new, kwargs):
        self.log("------" + self.get_state("sensor.vision_zp3102_pir_motion_sensor_alarm_level"))
        #self.log("---" + self.get_state("sensor.vision_zp3102_pir_motion_sensor_alarm_level")
        #self.log("---" + self.get_state("device_tracker.androidea3abc784f46ce1e")
        #self.log("---" + self.get_state("device_tracker.android96ec900e05631826")



        if self.get_state("sensor.vision_zp3102_pir_motion_sensor_alarm_level") == '255':
            if self.get_state("device_tracker.androidea3abc784f46ce1e") == 'not_home' and self.get_state("device_tracker.android96ec900e05631826") == 'not_home':
                self.log("****alarm triggered and no one home")
                for i in range(0,4):
                    self.call_service("switch/toggle", entity_id = "switch.office_light")
                    time.sleep(5)
            self.call_service("switch/turn_on", entity_id = "switch.office_light")
        else:
            self.call_service("switch/turn_off", entity_id = "switch.office_light")

        #if self.get_state("sensor.vision_zp3102_pir_motion_sensor_alarm_level") == '0':
        #    self.call_service("switch/turn_off", entity_id = "switch/office_light")

