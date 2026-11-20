# Traffic Analysis Pipeline

## Project Overview

This project builds a reproducible traffic analysis pipeline using the Metro Interstate Traffic Volume dataset.

The pipeline includes:

- Data loading
- Data validation
- Data cleaning
- Feature engineering
- Visualisation
- Command-line analytics application

---

## Project Structure

part2_python/

- pipeline.py
- feature_engineering.py
- visualizations.py
- cli_app.py
- config.py
- logs/
- figures/
- data/processed/

## Pipeline Workflow

Raw Dataset -> pipeline.py -> traffic_clean.csv -> feature_engineering.py -> traffic_features.csv -> visualizations.py -> cli_app.py

---

## Logging Configuration

The project uses Python's logging module.

Logs are written to:

logs/pipeline.log

The logging formatter includes:

- Timestamp
- Log level
- Module name
- Message

Log Levels:

DEBUG
- Intermediate calculations

INFO
- Normal pipeline milestone

WARNING
- Data cleaning actions and imputations

ERROR
- Failurs that prevent execution

### Logging Levels

DEBUG

- Intermediate calculations
- Quartile thresholds
- Feature engineering diagnostics

INFO

- Dataset loaded
- Schema validation completed
- Features created
- Visualisation saved
- CLI command executed

WARNING

- Duplicate timestamps detected
- Invalid temperatures detected
- Rainfall outliers detected
- Median imputation performed

ERROR

- File loading failures
- Invalid command execution
- Pipeline failures

---

### Congestion Category Logic

A data-driven congestion category was created using traffic volume quartiles.

The traffic distribution was divided into four groups based on the 25th, 50th and 75th percentile thresholds:

- Low: traffic_volume < Q1
- Medium: Q1 <= traffic_volume <Q2
- High: Q2 <= traffic_volume < Q3
- Severe: traffic_volume >= Q3

This approach was selected because it reflects the actual distribution of traffic observations and provides balanced congestion classes for subsequent machine-learning tasks.

---

## Visualization Summary

### Traffic by Hour
Traffic volume peeks during afternoon commuting periods, with the highest 
average traffic occurring around 16:00

### Weekday vs Weekend
Weekday traffic volume is substantially higher than weekend traffic volume,
indicating strong commuter influence.

### Temperature vs Traffic
A week positive relationship exists between temperature and traffic volume, consistent with the observed correlation coefficient from Part 1.

---

## CLI Commands

Peak Hour

\\\bash
python3 cli_app.py peak 

Weekend Traffic

\\\bash
python3 cli_app.py weekend

Weather Analysis

\\\bash
python3 cli_app.py weather

Travel Recommendation

\\\bash
python3 cli_app.py recommend

---

## Key Outputs

Generated Files:

- data/processed/traffic_clean.csv
- data/processed/traffic_features.csv
- figures/traffic_by_hour.png
- figures/weekday_weekend.png
- figures/temperature_traffic.png
- logs/pipeline.log