# code extracted from robot.py: saved for reference.

def cameraserverInit(self):
    if self.limelight1 or self.limelight2:

        self.cameraserver = CameraServer()
        self.cameraserver.enableLogging()
    
    if self.limelight1:
        self.cameraserver.addCamera(HttpCamera(self.limelight1.get_name(), f"{addys[0]}:5800"))
    if self.limelight2:
        self.cameraserver.addCamera(HttpCamera(self.limelight2.get_name(), f"{addys[1]}:5800"))

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
        try:
            result1 = self.limelight1.get_results()
            print(result1)
            parsed_result1 = limelightresults.parse_results(result1)
            for result in parsed_result1.fiducialResults:
                print("Limelight1 fiducial_id")
                print(result.fiducial_id)

            CameraServer().addCamera(HttpCamera(self.limelight1.get_name(), f"{addys[0]}:5800"))
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Failed to connect to Limelight1: {e}")
            self.limelight1 = None
    else:
        self.limelight1 = None

    if len(addys) >= 2:
        self.limelight2 = limelight.Limelight(addys[1])
        try:
            result2 = self.limelight2.get_results()
            print(result2)
            parsed_result2 = limelightresults.parse_results(result2)
            for result in parsed_result2.fiducialResults:
                print("Limelight2 fiducial_id")
                print(result.fiducial_id)

            CameraServer().addCamera(HttpCamera(self.limelight2.get_name(), f"{addys[1]}:5800"))
        except requests.exceptions.ConnectionError as e:
            logging.error(f"Failed to connect to Limelight2: {e}")
            self.limelight2 = None
    else:
        self.limelight2 = None

    print("----------- LIMELIGHT -----------")

def teleopPeriodic_limelight_part (self) -> None:
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
