#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import commands2
import typing
import os
from robotcontainer import RobotContainer
import limelight
import limelightresults
from cscore import CameraServer, HttpCamera

LATENCY_SECONDS = 0.02

class MyRobot(wpilib.TimedRobot):
    autonomousCommand: typing.Optional[commands2.Command] = None
    chooser: wpilib.SendableChooser = wpilib.SendableChooser()
    
    def __init__(self):
        super().__init__(LATENCY_SECONDS)
    
    def robotInit(self) -> None:
        self.container = RobotContainer()
        self.scheduler = commands2.CommandScheduler.getInstance()
        self.smartdashboard = wpilib.SendableChooser()
        
        # List .traj files and put them in SendableChooser
        self.list_traj_files()

        # Initialize Limelights
        self.limelightInit()

        # Initialize CameraServer
        self.cameraserverInit()

    def cameraserverInit(self):
        if self.limelight1 or self.limelight2:

            self.cameraserver = CameraServer()
            self.cameraserver.enableLogging()
        
        if self.limelight1:
            self.cameraserver.addCamera(HttpCamera(self.limelight1.get_name(), f"{addys[0]}:5800"))
        if self.limelight2:
            self.cameraserver.addCamera(HttpCamera(self.limelight2.get_name(), f"{addys[1]}:5800"))
        


    def list_traj_files(self) -> None:
        traj_dir = f"{wpilib.getOperatingDirectory()}/deploy/choreo"
        traj_files = [f for f in os.listdir(traj_dir) if f.endswith('.traj')]
        
        for traj_file in traj_files:
            self.chooser.addOption(traj_file.removesuffix('.traj'), traj_file.removesuffix('.traj'))
        
        self.chooser.setDefaultOption(traj_files[0].removesuffix('.traj'), traj_files[0].removesuffix('.traj'))
        wpilib.SmartDashboard.putData('Trajectory Files', self.chooser)

    def get_selected_traj_file(self) -> str:
        return self.chooser.getSelected()

    def robotPeriodic(self) -> None:
        """This function is called every 20 ms, no matter the mode. Use this for items like diagnostics
        that you want ran during disabled, autonomous, teleoperated and test.

        This runs after the mode specific periodic functions, but before LiveWindow and
        SmartDashboard integrated updating."""

        # Runs the Scheduler.  This is responsible for polling buttons, adding newly-scheduled
        # commands, running already-scheduled commands, removing finished or interrupted commands,
        # and running subsystem periodic() methods.  This must be called from the robot's periodic
        # block in order for anything in the Command-based framework to work.
        
        self.scheduler.run()

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        pass

    def autonomousInit(self) -> None:
        selected_traj_file = self.get_selected_traj_file()
        self.autonomousCommand = self.container.getAutonomousCommand(selected_traj_file)
        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def autonomousPeriodic(self) -> None:
        pass

    def teleopInit(self) -> None:
        # This makes sure that the autonomous stops running when
        # teleop starts running. If you want the autonomous to
        # continue until interrupted by another command, remove
        # this line or comment it out.
        #if self.autonomousCommand:
        #    self.autonomousCommand.cancel()

        self.container.configureButtonBindings()

    def teleopPeriodic(self) -> None:
        if self.limelight1 is not None:
            status1 = self.limelight1.get_status()
            result1 = self.limelight1.get_results()
            parsed_result1 = limelightresults.parse_results(result1)
            for fiducial_result in parsed_result1.fiducialResults:
                print(f"Limelight1 fiducial_id: {fiducial_result.fiducial_id}, cpu: {status1['cpu']}")

        if self.limelight2 is not None:
            status2 = self.limelight2.get_status()
            result2 = self.limelight2.get_results()
            parsed_result2 = limelightresults.parse_results(result2)
            for fiducial_result in parsed_result2.fiducialResults:
                print(f"Limelight2 fiducial_id: {fiducial_result.fiducial_id}, cpu: {status2['cpu']}")

    def testInit(self) -> None:
        self.scheduler.cancelAll()

    def simulationInit(self) -> None:
        pass

    def simulationPeriodic(self) -> None:
        pass

    def limelightInit(self):
        # save for reference
        print("----------- LIMELIGHT -----------")
        addys = limelight.discover_limelights()
        if not addys:
            print("No Limelights found")
            self.limelight1 = None
            self.limelight2 = None
            return

        if len(addys) >= 1:
            self.limelight1 = limelight.Limelight(addys[0])
            result1 = self.limelight1.get_results()
            print(result1)
            parsed_result1 = limelightresults.parse_results(result1)
            for result in parsed_result1.fiducialResults:
                print("Limelight1 fiducial_id")
                print(result.fiducial_id)

            CameraServer().addCamera(HttpCamera(self.limelight1.get_name(), f"{addys[0]}:5800"))
        else:
            self.limelight1 = None

        if len(addys) >= 2:
            self.limelight2 = limelight.Limelight(addys[1])
            result2 = self.limelight2.get_results()
            print(result2)
            parsed_result2 = limelightresults.parse_results(result2)
            for result in parsed_result2.fiducialResults:
                print("Limelight2 fiducial_id")
                print(result.fiducial_id)

            CameraServer().addCamera(HttpCamera(self.limelight2.get_name(), f"{addys[1]}:5800"))
        else:
            self.limelight2 = None

        print("----------- LIMELIGHT -----------")