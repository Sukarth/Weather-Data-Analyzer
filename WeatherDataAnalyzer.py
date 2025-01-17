"""
Weather Data Analyzer

Usage:
    python WeatherDataAnalyzer.py

Description:
    This program reads weather data from a specified text file and calculates the average 
    temperature for each month. It categorizes the weather records by month and 
    prints both the average temperature and individual records for each month.

Dependencies:
  - Python 3.x
  - Standard libraries:
    - datetime

Execution instructions:
    1. Run the program using the command: python WeatherDataAnalyzer.py
    2. When prompted, enter the name of the weather data file (e.g., "weather_data.txt").
        a. NOTE: the file must be in the same directory as the program
    3. The program will read the data, calculate the average weather for the months provided in the input, and print the results.

Example input text file format:
    Each line in the input text file should contain:
    YYYY-MM-DD,temperature,humidity
    For example:
    2024-01-01,5.2,78
    2024-01-02,4.8,80

Example output printed to the console:

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

    
Author: Sukarth Acharya
Version: 1.0
Version Created: 17.01.25

"""

from datetime import datetime  # Import the datetime class for handling date and time


class WeatherRecord:
    """
    Represents a single day's weather data, including date, temperature, and humidity.

    Attributes:
        date (datetime): The date of the weather record.
        temperature (float): The temperature recorded on that date.
        humidity (float): The humidity recorded on that date.

    """

    def __init__(self, date_str, temp_str, humidity_str):
        """
        Initializes a WeatherRecord object.

        Args:
            date_str (str): The date as a string in the format YYYY-MM-DD.
            temp_str (str): The temperature as a string.
            humidity_str (str): The humidity as a string.
            
        Returns:
            None

        """
        # Convert the date string to a datetime object in the format of year-month-day (%Y-%m-%d) by passing it to the strptime function
        self.date = datetime.strptime(date_str, "%Y-%m-%d") # basically changes the format of the date in the input to match the given format: 'year-month-day'

        # Convert temperature and humidity strings to float/decimals
        self.temperature = float(temp_str)
        self.humidity = float(humidity_str)

    def __str__(self):
        """
        Returns a formatted string representation of the weather record.

        Returns:
            str: A string that includes the formatted date, temperature, and humidity.

        """
        # Get the full name of the day of the week (e.g., Monday)
        day_name = self.date.strftime("%A") # %A converts the day to the name of the day
        # strftime() is a function that converts date and time into formatted strings. It allows you to customize the output of date and time information according to the format specified inside the brackets. 

        # Format the date to include the day name, month, and day (e.g., "Thursday, March 1")
        formatted_date = self.date.strftime(f"{day_name}, %B %d")

        # Return a string that includes the formatted date, temperature, and humidity
        return f"{formatted_date}: {self.temperature}°C, {self.humidity}% humidity"


def read_weather_file(filename):
    """
    Reads weather data from a file and returns a list of WeatherRecord objects.

    Args:
        filename (str): The name of the file containing weather data.

    Returns:
        list: A list of WeatherRecord objects or an empty list if an error occurs.

    """
    records = []  # Initialize an empty list to store WeatherRecord objects

    try: # Attempting to read weather data from the text file and save it to the 'records' variable
        
        with open(filename, "r") as file: # Attempting to open the specified file in read mode
            for line in file:  # Iterate through each line in the file
                line = line.strip()  # Remove leading/trailing whitespace
                if not line: # skip empty lines
                    continue

                parts = line.split(",")  # Split the line into components (date, temp, humidity) at every comma

                if len(parts) == 3:  # Check if there are exactly three parts
                    records.append(WeatherRecord(*parts))  # Create a WeatherRecord object using the class and add it to the list of records. The '*' essentially splits the list into its 3 parts and supplies them to their respective arguments in the WeatherRecord class.
                else:
                    print(f"Skipping invalid line: {line}")  # Print a message for any invalid lines 
    except FileNotFoundError: # Checking for case where file does not exist
        print(f"Error: File '{filename}' could not be found.")  # informing the user that the specified file could not be found
        return []  # Return an empty list if the file is not found
    except Exception as e: # checking for any other errors
        print(f"Error reading file: {e}")  # Handle any other exceptions that may occur by displaying it to the user
        return []  # Return an empty list on error

    return records  # Return the list of WeatherRecord objects


def categorize_and_calculate(records):
    """
    Categorizes records by month and calculates average temperature for each month.

    Args:
        records (list): A list of WeatherRecord objects.

    Returns:
        None: This function prints results directly and does not return any value.
    """

    if not records:  # Check if there are no records to process
        print("No records to process.") # tell the user when there are no records
        return

    # Categorize data into months
    monthly_data = []  # Initialize an empty list to store categorized data

    for record in records:  # Iterate through each weather record
       
        month_year = record.date.strftime("%B %Y")  # Extract the month and year from the record's date in this format: "Month Year" (ex: "January 2024")
        
        # Searcing for an existing list for this month_year in our monthly_data
        found = False  # variable to track if a matching month_year has been found
        for item in monthly_data:
            if item[0] == month_year:  # Check if this item's month_year matches our current record
                item[1].append(record)  # If a match is found, add the record to this month's list
                found = True  # Set flag to True as a match has been found
                break  # Exit the loop the correct month has been found and updated
        
        # If no matching month_year was found in our monthly_data
        if not found:
            # Create a new list  for this month_year and add it to monthly_data
            # The new list contains two elements: The month_year string and a list containing the current record
            monthly_data.append([month_year, [record]])

    # Calculate and print results for each month
    for month_data in monthly_data:
        month_year = month_data[0]  # Get the month-year string
        records = month_data[1]     # Get the list of records for this month

        temperatures = [record.temperature for record in records]  # Extract temperatures from records
        avg_temp = sum(temperatures) / len(temperatures)  # Calculate average temperature

        # Print the average temperature for this month
        print(f"\nAverage temperature for {month_year}: {avg_temp:.1f}°C\n")

        # Print each weather record for this month (in the same year)
        for record in records:
            print(record)

        print()  # Print an empty line for better readability


def main():
    """
    Main function to execute the weather data analysis program.

    Args:
        None

    Returns:
        None
    
    """
    # Prompt the user for the file name containing weather data
    filename = input("Enter the weather data file name: ")

    # Read weather data from the specified TEXT file
    records = read_weather_file(filename)

    # Analyze and categorize the weather data by month
    categorize_and_calculate(records)


# Run the program only if it is executed directly, and not when imported as a module
if __name__ == "__main__":
    main()
