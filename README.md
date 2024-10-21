# Robotic Locomotion through Active and Passive Morphological Adaptation

This repository contains the onboard software for the robot developed in the paper **"Robotic Locomotion through Active and Passive Morphological Adaptation in Extreme Outdoor Environments"**. The robot showcases active morphological reconfiguration to navigate complex terrains with multi-modal locomotion, including driving, rolling, and swimming.

## Overview
All electronics, including sensors, computing, and power, are located in the robot's central payload. The software here drives these capabilities and facilitates efficient data recording, control of the actuation systems, and autonomous operation.  

## Hardware Setup
- **Power**: Power is managed by a Holybro PM02D power module and provided by a 3S 1600mAh LiPo battery.
- **Computing**: An onboard Raspberry Pi 5 (8GB) runs all software.
- **Sensors**:
  - **PCA9685 PWM/Servo Driver**: Controls motors and winches.
  - **AS5048B Position Sensors**: Capture winch spool rotations.
  - **LSM6DSOX + LIS3MDL IMU**: Provides acceleration, angular rate, and magnetic field data.
  - **INA220 Power Monitor**: Tracks power usage.
  - **Septentrio MosaicHat GNSS**: Provides precise localization with RTK corrections via a mobile Wi-Fi connection.
- **Actuators**: 4 wheel motors are mounted along the frame for wheeled locomotion and 2 winch motors are mounted to the central payload for reconfiguration.

## Software
The robot leverages the [**ROSbloX** project](https://rosblox.github.io/), which provides modular building blocks for robotic software development. These [ROSbloX modules](https://github.com/rosblox) allow the robot to perform various functions, including locomotion, morphological adaptation, and sensor data collection. 
This repository contains the configuration files needed to run ROSbloX specifically tailored for the robot's onboard computer. The software enables:

- **Locomotion Control**: Managing the robot's movement through different terrains using [ROS2 Nav2](https://docs.nav2.org/).
- **Morphological Reconfiguration**: Enabling the robot to switch between different shapes and adapt to its environment efficiently.
- **Data Visualization and Recording**: A web interface provides real-time data visualization, and all sensor data can be recorded directly for analysis and post-processing.

## Citation
If you use this work, please cite the following paper:

```

... to be updated soon ...

@misc{polzin_rosblox_2024_new,
  author = {Polzin, Max},
  title = {{ROSbloX}},
  year = {2024},
  url = {https://rosblox.github.io/}
}
```

## License
The software is released under a permissive open-source license.

## Contact
For questions, feedback, or collaboration, please reach out via [**ROSbloX Discussions**](https://github.com/orgs/rosblox/discussions) or email at **polzin.max@gmail.com**.

