import csv
import math
from datetime import datetime
from operator import mod

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    from datetime import datetime
    date = datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z") 
    date_string = str(f'{date.strftime("%A")} {date.strftime("%d")} {date.strftime("%B")} {date.strftime("%Y")}')
    return date_string
    


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    
    temp_in_celcius = (float(temp_in_farenheit)-32)*5/9
    temp_in_celcius_rounded = float( "{:.1f}".format(temp_in_celcius))
    return temp_in_celcius_rounded

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    counter=0
    total=0
    for number in weather_data:
        total+= float(number)
        counter+=1
        temp_mean = total/counter

    return temp_mean


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        reader = csv.reader(file)
        csv_data = []
        is_header = True
        for row in reader:
            if is_header == False:
                if row != []:
                    line = [f"{row[0]}",float(row[1]),float(row[2])]
                    csv_data.append(line)
            is_header = False
    return csv_data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    
    else:
        temp_min = float(weather_data[0])
        index = 0
        index_min = index
        for temp in weather_data:
            if float(temp) <= temp_min:
                temp_min = float(temp)
                index_min = index
            index += 1
        return temp_min, index_min

    
              
def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    
    else:
        temp_max = float(weather_data[0])
        index = 0
        index_max = index
        for temp in weather_data:
            if float(temp) >= temp_max:
                temp_max = float(temp)
                index_max = index
            index += 1
        return temp_max, index_max



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
   
    weather_min = []    
    weather_max = []    
    for row in weather_data:
        weather_min.append(row[1]) 
        weather_max.append(row[2]) 

    lowest_data = find_min(weather_min)    
    highest_data = find_max(weather_max)   
    average_low = convert_f_to_c(calculate_mean(weather_min))  
    average_high = convert_f_to_c(calculate_mean(weather_max))  
    num_day = len(weather_data)
    temp_lowest = convert_f_to_c(lowest_data[0])
    date_lowest = convert_date(weather_data[lowest_data[1]][0]) 
    temp_highest = convert_f_to_c(highest_data[0])
    date_highest = convert_date(weather_data[highest_data[1]][0]) 

    result = f"{num_day} Day Overview\n"
    result += f"  The lowest temperature will be {format_temperature(temp_lowest)}, and will occur on {date_lowest}.\n"
    result += f"  The highest temperature will be {format_temperature(temp_highest)}, and will occur on {date_highest}.\n"
    result += f"  The average low this week is {format_temperature(average_low)}.\n"
    result += f"  The average high this week is {format_temperature(average_high)}.\n"
    return result


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""
    for row in weather_data:
        date = convert_date(row[0])
        temp_min = format_temperature(convert_f_to_c(row[1]))
        temp_max = format_temperature(convert_f_to_c(row[2]))
        result += f"---- {date} ----\n"
        result += f"  Minimum Temperature: {temp_min}\n"
        result += f"  Maximum Temperature: {temp_max}\n\n"
    return result

        

