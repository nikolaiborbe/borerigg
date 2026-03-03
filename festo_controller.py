from dataclasses import dataclass

from edcon.edrive.com_modbus import ComModbus
from edcon.edrive.motion_handler import MotionHandler
from edcon.utils.logging import Logging


@dataclass
class FestoPosition:



class FestoController:
    def __init__(self):
        Logging()
        self.com = ComModbus('192.168.0.1')
        self.mot = MotionHandler(self.com)
        self.mot.acknowledge_faults()
        self.mot.enable_powerstage()
        self.mot.referencing_task()
    
    def move(self, position: FestoPosition, velocity, absolute=False):
        self.mot.position_task(position, velocity, absolute=absolute)
        self.mot.wait_for_target_position() # blocks until motion finished
    
    def shutdown(self):
        self.mot.shutdown



