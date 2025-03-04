local ffi = require ('ffi')

ffi.cdef[[
typedef struct cRobotContainer cRobotContainer;
cRobotContainer* cRobotContainerNew();
]]

---RobotContainer wrapper
---@class RobotContainer
local RobotContainer = {}
local RobotContainer_mt = {
    __index = RobotContainer
}

function RobotContainer.new()
    return ffi.C.cRobotContainerNew()
end

ffi.metatype ('cRobotContainer', RobotContainer_mt)
return RobotContainer
