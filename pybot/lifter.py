from phoenix6.hardware import talon_fx
from phoenix6.configs.talon_fx_configs import TalonFXConfiguration, MotorOutputConfigs

class Lifter:
    def __init__(self, motor_ids):
        self.motors = [talon_fx.TalonFX(id) for id in motor_ids]
        self._configure_motors()

    def _configure_motors(self):
        for i, motor in enumerate(self.motors):
            motor.configFactoryDefault()
            
            # Create a TalonFXConfiguration object
            config = TalonFXConfiguration()
            
            # Set the motor inversion
            motor_output_config = MotorOutputConfigs()
            motor_output_config.inverted = (i == 1)  # Invert the second motor
            config.with_motor_output(motor_output_config)
            
            # Apply the configuration to the motor
            motor.getConfigurator().apply(config)
            
            motor.configPeakCurrentLimit(40)
            motor.configContinuousCurrentLimit(30)
            motor.enableCurrentLimit(True)

    def move_up(self):
        for motor in self.motors:
            motor.set(0.1)

    def move_down(self):
        for motor in self.motors:
            motor.set(-0.1)

    def stop(self):
        for motor in self.motors:
            motor.set(0.0)

    def get_positions(self):
        return [motor.get_position().value for motor in self.motors]