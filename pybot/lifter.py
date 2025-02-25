from phoenix6.hardware import talon_fx
from phoenix6.configs.talon_fx_configs import TalonFXConfiguration, MotorOutputConfigs
from phoenix6.signals import InvertedValue

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
                if motor.getDeviceID() == 20:
                    motor_output_config.inverted = InvertedValue.CLOCKWISE_POSITIVE
                elif motor.getDeviceID() == 14:
                    motor_output_config.inverted = InvertedValue.COUNTER_CLOCKWISE_POSITIVE
                
                config.with_motor_output(motor_output_config)
                motor.getConfigurator().apply(config)
        except Exception as e:
            pass

    def move_up(self):
        try:
            for motor in self.motors:
                motor.set(0.1)
        except Exception as e:
            pass

    def move_down(self):
        try:
            for motor in self.motors:
                motor.set(-0.1)
        except Exception as e:
            pass

    def stop(self):
        try:
            for motor in self.motors:
                motor.set(0.0)
        except Exception as e:
            pass

    def get_positions(self):
        try:
            positions = [motor.get_position().value for motor in self.motors]
            return positions
        except Exception as e:
            return []