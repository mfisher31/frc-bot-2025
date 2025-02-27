#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import typing

from robotcontainer import RobotContainer

class MyRobot(wpilib.TimedRobot):
    autonomousCommand: typing.Optional[commands2.Command] = None
    
    def robotInit(self) -> None:
        self.container = RobotContainer()
        self.scheduler = commands2.CommandScheduler.getInstance()

    def robotPeriodic(self) -> None:
        self.scheduler.run()

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.getAutonomousCommand()
        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

        self.container.configureButtonBindings()

    def teleopPeriodic(self) -> None:
        pass

    def testInit(self) -> None:
        self.scheduler.cancelAll()

    def simulationInit(self) -> None:
        pass
    def simulationPeriodic(self) -> None:
        pass
