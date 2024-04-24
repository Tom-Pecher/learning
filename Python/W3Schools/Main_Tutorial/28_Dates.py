
# PYTHON: W3Schools - Tutorial
# Section 28: Dates


# BASICS
    # Although there is no date datatype in Python, we can import the datetime library to manipulate dates and times:
import datetime as dt

    # We can obtain the current time like so:
x = dt.datetime.now() # NOTE: returns YEAR-MONTH-DAY HOUR:MINUTE:SECOND.MICROSECOND
print("1.", x)

    # We can access specific parts of the datetime object:
print("2.", x.year)

    # We can also create our own datatime objects at custom times:
y = dt.datetime(2020, 5, 17) # NOTE: Unspecified entries are 0 by default.
print("3.", y)

    # We can also format the datetime object in a number of ways, %A returns the full name of the week day:
print("4.", y.strftime("%A"))


# FORMAT CODES
    # %a 	Weekday, short version 	                                        Wed 	
    # %A 	Weekday, full version 	                                        Wednesday 	
    # %w 	Weekday as a number 0-6, 0 is Sunday 	                        3 	
    # %d 	Day of month 01-31 	                                            31 	
    # %b 	Month name, short version 	                                    Dec 	
    # %B 	Month name, full version 	                                    December 	
    # %m 	Month as a number 01-12 	                                    12 	
    # %y 	Year, short version, without century 	                        18 	
    # %Y 	Year, full version 	                                            2018 	
    # %H 	Hour 00-23 	                                                    17 	
    # %I 	Hour 00-12 	                                                    05 	
    # %p 	AM/PM 	                                                        PM 	
    # %M 	Minute 00-59 	                                                41 	
    # %S 	Second 00-59 	                                                08 	
    # %f 	Microsecond 000000-999999 	                                    548513 	
    # %z 	UTC offset 	                                                    +0100 	
    # %Z 	Timezone 	                                                    CST 	
    # %j 	Day number of year 001-366 	                                    365 	
    # %U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
    # %W 	Week number of year, Monday as the first day of week, 00-53 	52 	
    # %c 	Local version of date and time 	                                Mon Dec 31 17:41:00 2018 	
    # %C 	Century 	                                                    20 	
    # %x 	Local version of date 	                                        12/31/18 	
    # %X 	Local version of time 	                                        17:41:00 	
    # %% 	A % character 	                                                % 	
    # %G 	ISO 8601 year 	                                                2018 	
    # %u 	ISO 8601 weekday (1-7) 	                                        1 	
    # %V 	ISO 8601 weeknumber (01-53) 	                                01
