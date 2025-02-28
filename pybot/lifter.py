import logging
from phoenix6.hardware import talon_fx

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define position limits
POS_MIN = 1.3
POS_MAX = 19

class Lifter:
    def __init__(self, right_id):
        self.motor = talon_fx.TalonFX(right_id)
        self.can_move_up_flag = True
        self.can_move_down_flag = True

    def can_run_motor(self):
        val = float(self.motor.get_position().value)
        return POS_MIN < val < POS_MAX
    
    def can_move_down(self):
        val = float(self.motor.get_position().value)
        return val > POS_MIN and self.can_move_down_flag
    
    def can_move_up(self):
        val = float(self.motor.get_position().value)
        return val < POS_MAX and self.can_move_up_flag

    def move_down(self):
        try:
            if not self.can_move_down():
                logger.warning("Motor is out of range, cannot move down")
                self.stop()
                self.can_move_down_flag = False
                return

            self.motor.set(-0.05)
        except Exception as e:
            logger.error(f"Error moving down: {e}")

    def move_up(self):
        try:
            if not self.can_move_up():
                logger.warning("Motor is out of range, cannot move up")
                self.stop()
                self.can_move_up_flag = False
                return

            self.motor.set(0.10)
        except Exception as e:
            logger.error(f"Error moving up: {e}")

    def stop(self):
        try:
            self.motor.stopMotor()
        except Exception as e:
            logger.error(f"Error stopping motor: {e}")
        
    def set_motor(self, value):
        try:
            self.motor.set(value)
        except Exception as e:
            logger.error(f"Error setting motor: {e}")

    def get_position(self):
        try:
            return self.motor.get_position().value
        except Exception as e:
            logger.error(f"Error getting position: {e}")
            return None