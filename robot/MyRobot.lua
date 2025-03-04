local ffi = require ('ffi')
ffi.load ('frc-bot-2025', true)

local TimedRobot = require ('frc.TimedRobot')
local RobotContainer = require ('RobotContainer')

---@class MyRobot 
local MyRobot = TimedRobot.derive()

function MyRobot:robotInit()
    self.container = RobotContainer.new()
end

function MyRobot:robotPeriodic() end

function MyRobot:disabledInit()
    print ("MyRobot:disabledInit()")
end
function MyRobot:disabledPeriodic() end

function MyRobot:autonomousInit()
    print ("MyRobot:autonomousInit()")
end
function MyRobot:autonomousPeriodic() end

function MyRobot:teleopInit()
    print ("MyRobot:teleopInit()")
end
function MyRobot:teleopPeriodic() end

function MyRobot:testInit()
    print ("MyRobot:testInit()")
end
function MyRobot:testPeriodic() end

function MyRobot:simulationInit() end
function MyRobot:simulationPeriodic() end

function MyRobot:disabledExit() end
function MyRobot:autonomousExit() end
function MyRobot:teleopExit() end
function MyRobot:testExit() end

local function new()
    local r = TimedRobot.init ({}, 0.02)
    setmetatable (r, { __index = MyRobot })
    return r
end

return {
    new = new
}
