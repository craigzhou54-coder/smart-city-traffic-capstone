### Smart City Traffic Intelligence Capstone

## Project Overview

This project develops an end-to-end traffic intelligence solution using the Metro Interstate Traffic Volume dataset.

The project consists of:

Part 1: Data Analytics
Part 2: Traffic Analytics Pipeline Engineering
Part 3: Machine Learning, Explainable AI and MLOps
Repository Structure

smart-city-traffic-capstone/

├── part1_data_analytics/ ├── part2_python/ ├── part3_machine_learning/ ├── reports/ └── README.md

## Part 1 – Data Analytics

# Contents:

SQL Analysis
Statistical Analysis
Probability Analysis
Power BI Dashboard
Data Analytics Insights Report

## Key Findings:

Metro Interstate Traffic Volume

Accident Data
No real accident dataset was available.

A documented proxy label (High_Risk) was created using:
    . Congestion level
    . Severe weather
    . Low visibility

Peak traffic period occurs at approximately 16:00.
Weekday traffic is substantially higher than weekend traffic.
Weather contributes to traffic variation but temporal behaviour is a stronger predictor.

## Part 2 – Traffic Analytics Pipeline

# Components:

pipeline.py
feature_engineering.py
visualizations.py
cli_app.py

# Generated Outputs:

traffic_clean.csv
traffic_features.csv
pipeline.log
Visualisation figures

# CLI Commands:

python3 cli_app.py peak

python3 cli_app.py weekend

python3 cli_app.py weather

python3 cli_app.py recommend

# Logging Configuration

The project uses Python's logging module.

Log format:

Timestamp
Log Level
Module Name
Message

Logging Levels:

# INFO

Used for:

Dataset loading
Feature engineering completion
Figure generation
Model training completion

# WARNING

Used for:

Invalid values
Imputation operations
Monitoring alerts
Data quality issues

# ERROR

Used for:

Missing files
Invalid commands
Runtime failures

## Part 3 – Machine Learning and AI

# Supervised Learning

Regression Models:

Linear Regression
Random Forest Regressor
Neural Network

Classification Models:

Logistic Regression
Random Forest Classifier

# Unsupervised Learning

K-Means Clustering
Association Rule Mining

# Explainable AI

SHAP was used to explain model behaviour and identify the most influential traffic predictors.

# MLOps

Implemented:

MLflow Experiment Tracking
FastAPI Deployment Simulation
Monitoring
Alerting

# Recommendation System

The recommendation engine identifies lower-congestion travel periods and generates travel recommendations.

Example:

"For flexible journeys, consider travelling between 01:00 and 03:59, when historical traffic volumes are typically lower."

## Responsible AI Statement

No real accident dataset was available.

A documented proxy label named High_Risk was created using:

Congestion Category
Severe Weather
Low Visibility
The resulting models therefore estimate traffic risk rather than actual accident likelihood.

Known limitations include:

Missing observations between September 2014 and May 2015
Duplicate timestamps
Sensor anomalies
Incomplete holiday coverage

## How To Run

# Part 2 Pipeline
python3 pipeline.py

# Feature Engineering
python3 feature_engineering.py

# Visualisations
python3 visualizations.py

# Part 3 Machine Learning
python3 regression.py
python3 classification.py
python3 clustering.py
python3 deep_learning.py

# FastAPI Deployment
uvicorn deployment:app --reload
Open:

http://127.0.0.1:8000/docs

# MLflow Tracking
python3 mlflow_tracking.py

mlflow ui
Open:

http://127.0.0.1:5000

# Repository

This Repository contains all files, code, reports, and analysis for the capstone project.

# Author
Craig Zhou