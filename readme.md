# Documentation

## Target assessment level

Target assessment level of this work is 3.

## Specification

### What does the program do?

The program

1. Reads weather data containing the date, temperature, and humidity from a specified text file
2. Categorizes the weather records by month.
3. Calculates the average temperature for each month.
4. Prints both the average temperature and individual records for each month, with appropriate spacing.

The user supplies the name of the input text file from keyboard.

### Data format

The input data text file consists of lines, each line containing:

`Date,Temperature,Humidity`

- `Date` is the date in this format: `YYYY-MM-DD`.
- `Temperature` is an integer or float.
- `Humidity` is an integer or float.

## Correctness

### Typical test case

File weather_data.txt contains weather data for 3 months (January, February and March), with 5 weather data records for January and 3 weather data records for February and March, resulting in a total of 11 weather data records.


When the program (file [WeatherDataAnalyzer.py](WeatherDataAnalyzer.py)) is run, the output is correct, with each month's data printed separately, along with that month’s average temperature:

```
Enter the weather data file name: weather_data.txt

Average temperature for January 2024: 3.5°C

Monday, January 01: 5.2°C, 78.0% humidity
Tuesday, January 02: 4.8°C, 80.0% humidity
Wednesday, January 03: 6.1°C, 75.0% humidity
Monday, January 15: -1.3°C, 65.0% humidity
Wednesday, January 31: 2.7°C, 70.0% humidity

Average temperature for February 2024: 5.9°C

Thursday, February 01: 3.5°C, 72.0% humidity
Wednesday, February 14: 8.0°C, 68.0% humidity
Wednesday, February 28: 6.2°C, 71.0% humidity

Average temperature for March 2024: 12.2°C

Friday, March 01: 9.5°C, 65.0% humidity
Friday, March 15: 12.3°C, 60.0% humidity
Sunday, March 31: 14.8°C, 55.0% humidity
```

## Resource management (level 2)

The input file is opened using a `with`-statement, so it will therefore be closed automatically.


