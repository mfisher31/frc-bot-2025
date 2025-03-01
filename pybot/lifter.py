import logging
from phoenix6.hardware import talon_fx

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Lifter:
    def __init__(self, master_id):
        self.motor = talon_fx.TalonFX(master_id)

    def move_down(self):
        try:
            if self.motor.getReverseLimitSwitch().isPressed():
                logger.warning("Reverse limit reached; cannot move down")
                self.stop()
            else:
                self.motor.set(-0.05)  # Gentle downward movement
        except Exception as e:
            logger.error(f"Error moving down: {e}")

    def move_up(self):
        try:
            if self.motor.getForwardLimitSwitch().isPressed():
                logger.warning("Forward limit reached; cannot move up")
                self.stop()
            else:
                self.motor.set(0.10)  # Upward movement
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