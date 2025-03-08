#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import commands2
import commands2.button
import commands2.cmd

from generated.tuner_constants import TunerConstants
from telemetry import Telemetry

from phoenix6 import swerve
from wpimath.units import rotationsToRadians
from lifter import Lifter  # Import the Lifter class
import wpilib
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        self._max_speed = (
            TunerConstants.speed_at_12_volts * .6
        )  # speed_at_12_volts desired top speed
        self._max_angular_rate = rotationsToRadians(
            0.75 * .4
            #maybe limit this rotational
        )  # 3/4 of a rotation per second max angular velocity

        # Drive Inversion multiplier
        self._driveMultiplier = -1.0

        # Setting up bindings for necessary control of the swerve drive platform
        self._drive = (
            swerve.requests.FieldCentric()
            .with_deadband(self._max_speed * 0.1)
            .with_rotational_deadband(
                self._max_angular_rate * 0.1
            )  # Add a 10% deadband
            .with_drive_request_type(
                swerve.SwerveModule.DriveRequestType.OPEN_LOOP_VOLTAGE
            )  # Use open-loop control for drive motors
        )
        self._brake = swerve.requests.SwerveDriveBrake()
        self._point = swerve.requests.PointWheelsAt()

        self._logger = Telemetry(self._max_speed)

        self.drivetrain = TunerConstants.create_drivetrain()

        # Initialize the elevator with motor IDs
        self.elevator = Lifter(20, 16)
        # Initialize the intake with motor IDs
        self.intake = Lifter(18, 22)

        # Setup telemetry
        self._registerTelemetery()

    def configureButtonBindings(self) -> None:
        """
        Setup which buttons do what.
        """
        if not hasattr (self, '_joystick') or self._joystick == None:
            self._joystick = commands2.button.CommandXboxController (0)

        # Cache the multiplier
        self._driveMultiplier = -1.0 if self.isRedAlliance() else 1.0
        
        # Note that X is defined as forward according to WPILib convention,
        # and Y is defined as to the left according to WPILib convention.
        self.drivetrain.setDefaultCommand(
            # Drivetrain will execute this command periodically
            self.drivetrain.apply_request(
                lambda: (
                    self._drive.with_velocity_x(
                        self._driveMultiplier * self._joystick.getLeftY() * self._max_speed
                    )  # Drive forward with negative Y (forward)
                    .with_velocity_y(
                        self._driveMultiplier * self._joystick.getLeftX() * self._max_speed
                    )  # Drive left with negative X (left)
                    .with_rotational_rate(
                        self._driveMultiplier * self._joystick.getRightX() * self._max_angular_rate
                    )  # Drive counterclockwise with negative X (left)
                )
            )
        )
        
        # reset the field-centric heading on left bumper press
        self._joystick.x().onTrue(
            self.drivetrain.runOnce(lambda: self.resetHeading())
        )
       
        # Configure buttons for elevator control
        self._joystick.y().whileTrue(commands2.cmd.startEnd(
           lambda: self.elevator.moveUp(),
           lambda: self.elevator.stop()
        ))

        self._joystick.a().whileTrue(commands2.cmd.startEnd(
           lambda: self.elevator.moveDown(),
           lambda: self.elevator.stop()
        ))
    
        
        self._joystick.rightTrigger().onTrue(commands2.cmd.runOnce(self.elevator.stop, self.elevator))

        # Set the rumble when the 'X' button is pressed
        #self._joystick.x().whileTrue(commands2.cmd.startEnd(
        #    lambda: self._joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kBothRumble, 1),
        #    lambda: self._joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kBothRumble, 0)
        #))
        #if wpilib.DriverStation.isTeleop() and wpilib.DriverStation.getMatchTime() <= 15:
        #    commands2.cmd.run(
        #    lambda: self._joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kRightRumble, 1),
        #    lambda: self._joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kRightRumble, 0),
        #    lambda: self._joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kLeftRumble, 1),
        #    lambda: self._joystick.setRumble(wpilib.interfaces.GenericHID.RumbleType.kLeftRumble, 0)
        #)

        # Log elevator positions when the 'B' button is pressed
        #self._joystick.b().whileTrue(commands2.cmd.run(lambda: logging.info(self.elevator.get_positions()), self.elevator))

        # Configure buttons for intake control
        self._joystick.rightBumper().whileTrue(commands2.cmd.startEnd(
            lambda: self.intake.setMotor(1),
            lambda: self.intake.stop()
        ))

        # Theres a chance red vs blue has changed, so do this now.
        self.resetHeading()

    def resetHeading(self):
        self.drivetrain.seed_field_centric()
    
    def _registerTelemetery (self):
        self.drivetrain.register_telemetry(
            lambda state: self._logger.telemeterize(state)
        )

    def getAutonomousCommand(self, selected_traj_file: str) -> commands2.Command:
        from autos import FollowTrajectory
        return FollowTrajectory (self.drivetrain, 
                                 self.intake, 
                                 selected_traj_file, 
                                 is_red_alliance = self.isRedAlliance())
    
    def isRedAlliance(self):
        return wpilib.DriverStation.getAlliance() == wpilib.DriverStation.Alliance.kRed