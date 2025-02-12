# Gradle
Gradle should be used to build the c++ native firmware. Most of the commands can be run from VSCode.  press `Shift + Ctrl + Backspace` to open the command pallete, then type "WPI" to see a listing.

## Firmware Build
```bash
./gradlew build
```

## Simulate
```
./gradlew simulateNative
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
