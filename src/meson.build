executable ('frcUserProgram', 
    '''
        tunerx/cpp/generated/TunerConstants.cpp
        tunerx/cpp/Robot.cpp
        tunerx/cpp/RobotContainer.cpp
        tunerx/cpp/Telemetry.cpp    
        tunerx/cpp/subsystems/CommandSwerveDrivetrain.cpp
        limelight.cpp
    '''.split(),
    include_directories: include_directories ('.', 'tunerx/include'),
    dependencies: [ wpilib_deps, luabot_dep ],
    link_args: [  ]
)
