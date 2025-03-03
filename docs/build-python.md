# Robotpy
Building and deploying python

## Install Python
```
sudo apt install python3 python3-pip
```

For mac and PC, use whatever means is most reliable for you.

## Install Robotpy
```
pip3 install robotpy
```

## The Code
It lives in a subdirectory, `pybot`, so change in to that first:
```
cd pybot
```

## Sync up
```
robotpy sync
```

## Phoenix6 Updates
This library can update frequently. The sim can run in HW mode by default. "Make sure your phoenix6 is up to date using [pip]. You can also force simulation to run by setting the CTR_TARGET=Simulation environment variable."
```sh
python -m pip install -U phoenix6
```

## Simulate
```sh
robotpy sim
```

## Build
TODO: Not needed yet.

## Deploy
```sh
robotpy deploy --skip-tests
```
