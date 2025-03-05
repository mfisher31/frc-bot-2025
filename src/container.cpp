#include "RobotContainer.h"

extern "C" {
typedef struct cRobotContainer cRobotContainer;

cRobotContainer* cRobotContainerNew() {
    auto rc = new RobotContainer();
    return (cRobotContainer*) rc;
}

void cRobotContainerConfigureBindings (cRobotContainer* self) {
    ((RobotContainer*) self)->ConfigureBindings();
}
}
