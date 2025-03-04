local ffi = require ('ffi')

ffi.cdef[[
typedef struct cRobotContainer cRobotContainer;
cRobotContainer* cRobotContainerNew();
]]

ffi.load ('frc-bot-2025', true)

---DriverStation wrapper
---@class RobotContainer
local RobotContainer = {}
local RobotContainer_mt = {
    __index = RobotContainer
}

function RobotContainer.new()
    return ffi.C.cRobotContainerNew ()
end

ffi.metatype('cRobotContainer', RobotContainer_mt)
return RobotContainer
