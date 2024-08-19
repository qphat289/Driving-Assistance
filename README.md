# Car Driving Assistance Solution


## Overview

This project, developed by Group 2 under the mentorship of Vũ Hoàng Việt and Nguyễn Võ Thành Khang, presents a car driving assistance solution tailored for Vietnam's traffic conditions. The system uses rear and front cameras to enhance driver awareness, reduce stress, and improve safety by providing timely warnings for rear obstacles and pedestrian crosswalks.

## Problem Statement
Rear Camera
In Vietnam's congested traffic, drivers face challenges in monitoring vehicles behind them, leading to a higher risk of accidents during braking or lane changes. The rear camera system addresses issues like limited visibility, delayed information, and driver distraction.
<p align="center">
    <img src="./docs/images/traffic-jam-vietnam.jpg" alt="Image" width="70%"/>
</p>
Front Camera
Pedestrian safety is compromised due to the lack of adherence to crosswalk rules. The front camera system aims to reduce accidents by alerting drivers of pedestrian crosswalks.
<p align="center">
    <img src="./docs/images/rasie-hand-to-cross-streets-bmXd.jpg" alt="Image" width="70%"/>
</p>

## System Features
Rear Camera:
Issues voice warnings when vehicles are detected within a 5-meter warning zone during turns or braking.

Front Camera:
Alerts drivers when approaching a pedestrian crosswalk.

## Data Collection and Preprocessing
Vehicle Data: Collected from YouTube dashcam videos and self-recorded footage, including both day and night scenarios. Data was annotated and split into training, validation, and test sets.
<p align="center">
    <img src="./docs/images/dataset.png" alt="Image" width="100%"/>
</p>
Pedestrian Crosswalk Data: Gathered from Roboflow and additional self-collected images to capture various perspectives and conditions.
<p align="center">
    <img src="./docs/images/dataset2.png" alt="Image" width="100%"/>
</p>

## Model Training
The project utilizes the [YOLO (You Only Look Once)](https://github.com/ultralytics/ultralytics) object detection algorithm due to its balance of speed and accuracy. The dataset was augmented to enhance model performance in different scenarios, such as flipping images, adjusting brightness, and adding blur to simulate real-world conditions.

## Future Plans
Database Expansion: Continuously collecting and refining the dataset to cover more scenarios.

[Car Direction Predictions](https://woven.toyota/en/prediction-dataset/): Enhancing the system to predict vehicle movements based on detected obstacles and road conditions.
<p align="center">
    <img src="./docs/images/Prediction_Dataset_Gif.gif" alt="Image" width="60%"/>
</p>

## Requirements

Hardware: Suitable for real-time inference with a response time under 10ms.

Software: Python, OpenCV, YOLO, and other relevant machine learning libraries.

## Usage
Clone the repository.

Install the required dependencies.

Run the training scripts to train the model on the provided dataset.

Deploy the model on a suitable hardware platform for real-time vehicle assistance.

## License
This project is licensed under the MIT License.

## Acknowledgements
We would like to thank our mentors, Vũ Hoàng Việt and Nguyễn Võ Thành Khang, for their guidance throughout this project.

