from datetime import datetime

def solution_station_2(date_string):
    # Dictionary mapping English weekday names to Japanese
    japanese_weekdays = {
        'Monday': '月曜日',
        'Tuesday': '火曜日',
        'Wednesday': '水曜日',
        'Thursday': '木曜日', 
        'Friday': '金曜日', 
        'Saturday': '土曜日', 
        'Sunday': '日曜日', 
    } 
    try:
        # Parse the input date string
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        
        # Get the weekday name in English
        weekday_name = date_object.strftime('%A')
        
        # Return the corresponding Japanese weekday
        return solution_station_2[weekday_name]
    
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

      
      
