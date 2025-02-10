[![Build](https://github.com/snidercs/bot-2024/actions/workflows/build.yml/badge.svg)](https://github.com/snidercs/bot-2024/actions/workflows/build.yml)
# Robot Firmware FRC 2025
## Features
- 

## Clone
Should be possible inside vscode, or...

```bash
git clone --recursive git@github.com:snidercs/frc-bot-2025.git
```

## Clang Format
The c++ code should be formatted before submitting pull requests. Do this with python or gradle.

```bash
# Run the python script directly
python3 util/format.py
# or do it wrapped in a gradle task
./gradlew clangFormat
```

## Requirements

### Dependencies
The `gradle build` and `gradle deploy` tasks both need roboRIO libraries and headers in place.  Most of them are handled by wpilib, but some need special attention.

**Linux**
```bash
# multilib support is needed for cross building, install if needed
sudo apt-get install gcc-multilib g++-multilib cmake python3 python3-pip
```

**macOS**

### Firmware Build with WPIlib VSCode
After LuaJIT is compiled, open a terminal and do:
```bash
./gradlew build
```

## Testing
Run all unit tests.
```bash
./gradlew check
```

## Deployment
Run the following command to deploy code to the roboRIO
```bash
./gradlew deploy
```

If it gives problems, cleaning the project could help. The `--info` option could give more information too.
```bash
./gradlew clean
./gradlew deploy --info
```


## Meson
The firmware for desktop/simulator can be built with meson.  You must first compile wpilib using cmake and install to the system before this will work.

```
meson setup build-meson
ninja -C build-meson -j4
```

And to run it, use the launcher script
```
sh util/simulate.sh
```

## WPILib CMake Build
allwpilib should compile as a subproject, but if it is failing then you should compile wpilib with cmake and install it. It is needed for meson to build the simulator.
```
# Clone the repository.
git clone https://github.com/wpilibsuite/allwpilib

# Create a build directory and move in to it.
cd allwpilib
mkdir -p build-cmake
cd build-cmake

cmake .. -G Ninja -DWITH_JAVA=NO -DWITH_DOCS=NO -DWITH_TESTS=NO
ninja
```

If you'reon a slow machine or have less than 16G of ram, tone it back.
```
ninja -j4
```

Then install it
```
sudo ninja install
```
## Meson and the RIO
This build is a work in progress.

### Acquire Shared Libraries
Gradle does not make it easy to utilize built artifacts externally. Thankfully, there is a task which will stage these libraries for us in the build-tree.

```
./gradlew installFrcUserProgramLinuxathenaReleaseExecutable --max-workers=2
```

### Setup and Build
TODO
