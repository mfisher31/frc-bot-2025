import logging
from phoenix6.hardware import talon_fx
from phoenix6.configs.talon_fx_configs import TalonFXConfiguration, MotorOutputConfigs
from phoenix6.signals import InvertedValue

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Lifter:
    def __init__(self, left_id, right_id):
        self.motors = [talon_fx.TalonFX(id) for id in [left_id, right_id]]
        self._configure_motors()

    def _configure_motors(self):
        try:
            for motor in self.motors:
                motor.configFactoryDefault()
                config = TalonFXConfiguration()
                motor_output_config = MotorOutputConfigs()
                
                # Set common properties
                motor.configPeakCurrentLimit(40)
                motor.configContinuousCurrentLimit(30)
                motor.enableCurrentLimit(True)
                
                # Specialize as needed
                #if motor.getDeviceID() == 20:
                #motor_output_config.inverted = InvertedValue.CLOCKWISE_POSITIVE
                #elif motor.getDeviceID() == 14:
                #    motor_output_config.inverted = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
                
                config.with_motor_output(motor_output_config)
                motor.getConfigurator().apply(config)
        except Exception as e:
            logger.error(f"Error configuring motors: {e}")

    def move_down(self):
        try:
            limit_hit = False
            for index, motor in enumerate(self.motors):
                if index == 0 and float(motor.get_position().value)  >= .3 or limit_hit:
                    logger.warning(f"Motor 20 passed its limit")
                    limit_hit = True
                    return
                if index == 1 and float(motor.get_position().value)  >= 1 or limit_hit:
                    logger.warning(f"Motor 14 passed its limit")
                    limit_hit = True
                    return
                motor.set(0.3)
        except Exception as e:
            logger.error(f"Error moving down: {e}")

    def move_up(self):
        try:
            limit_hit = False
            for index, motor in enumerate(self.motors):
                if index == 0 and float(motor.get_position().value)  <= -100 or limit_hit:
                    logger.warning(f"Motor 20 passed its limit")
                    limit_hit = True
                    return
                if index == 1 and float(motor.get_position().value) <= -100 or limit_hit:
                    logger.warning(f"Motor 14 passed its limit")
                    limit_hit = True
                    return
                motor.set(-0.3)
        except Exception as e:
            logger.error(f"Error moving up: {e}")

    def stop(self):
        try:
            for motor in self.motors:
                motor.stopMotor()
                logger.info(f"Motor {motor}: {motor.get_position()}")
        except Exception as e:
            logger.error(f"Error stopping motors: {e}")

    def get_positions(self):
        try:
            positions = [motor.get_position().value for motor in self.motors]
            return positions
        except Exception as e:
            logger.error(f"Error getting positions: {e}")
            return []