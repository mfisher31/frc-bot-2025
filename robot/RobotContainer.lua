local ffi = require ('ffi')

ffi.cdef[[
typedef struct cRobotContainer cRobotContainer;
cRobotContainer* cRobotContainerNew();
void cRobotContainerConfigureBindings (cRobotContainer* self);
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

function RobotContainer:configureBindings()
    ffi.C.cRobotContainerConfigureBindings (self)
end

ffi.metatype ('cRobotContainer', RobotContainer_mt)
return RobotContainer
