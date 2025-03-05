local ffi = require('ffi')

local CommandScheduler = require('frc2.command.CommandScheduler')
local TimedRobot = require('frc.TimedRobot')
local RobotContainer = require('RobotContainer')

ffi.load('frc-bot-2025', true)

---@class MyRobot
local MyRobot = TimedRobot.derive()

function MyRobot:robotInit()
    self.container = RobotContainer.new()
    self.scheduler = CommandScheduler.getInstance()
end

function MyRobot:robotPeriodic()
    self.scheduler:run()
end

function MyRobot:disabledInit()
end

function MyRobot:disabledPeriodic()
end

function MyRobot:disabledExit() end

function MyRobot:autonomousInit() end

function MyRobot:autonomousPeriodic()
end

function MyRobot:teleopInit()
    if not self.controlBound then
        self.container:configureBindings()
        self.controlBound = true
    end
end

function MyRobot:teleopPeriodic()
end

function MyRobot:testInit() end
function MyRobot:testPeriodic() end

function MyRobot:simulationInit() end
function MyRobot:simulationPeriodic() end

function MyRobot.new()
    local r = TimedRobot.init({}, 0.01)
    setmetatable (r, { __index = MyRobot })
    r.controlBound = false;
    r.container = RobotContainer.new()
    return r
end

return {
    new = MyRobot.new
}
