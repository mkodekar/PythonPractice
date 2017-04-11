num1 = -5
num2 = 5
print(abs(num1))

print(abs(num2))

if abs(num1) == abs(num2):
    print('absolute value of num1  is equal to num2')

# this function is buil in to find out the characterisitics for standard lib functions
help('urllib')

"""
this is the output for the help for the urllib function


Help on package urllib:

NAME
    urllib

MODULE REFERENCE
    https://docs.python.org/3.5/library/urllib.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

PACKAGE CONTENTS
    error
    parse
    request
    response
    robotparser

FILE
    /usr/lib/python3.5/urllib/__init__.py
    
"""

help('time')

"""
this is the output to time function

Help on built-in module time:

NAME
    time - This module provides various functions to manipulate time values.

DESCRIPTION
    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).
    
    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    
    Variables:
    
    timezone -- difference in seconds between UTC and local standard time
    altzone -- difference in  seconds between UTC and local DST time
    daylight -- whether local time should reflect DST
    tzname -- tuple of (standard time zone name, DST time zone name)
    
    Functions:
    
    time() -- return current time in seconds since the Epoch as a float
    clock() -- return CPU time since process start as a float
    sleep() -- delay for a number of seconds given as a float
    gmtime() -- convert seconds since Epoch to UTC tuple
    localtime() -- convert seconds since Epoch to local time tuple
    asctime() -- convert time tuple to string
    ctime() -- convert time in seconds to string
    mktime() -- convert local time tuple to seconds since Epoch
    strftime() -- convert time tuple to string according to format specification
    strptime() -- parse string to time tuple according to format specification
    tzset() -- change the local timezone

CLASSES
    builtins.tuple(builtins.object)
        struct_time
    
    class struct_time(builtins.tuple)
     |  The time value as returned by gmtime(), localtime(), and strptime(), and
     |  accepted by asctime(), mktime() and strftime().  May be considered as a
     |  sequence of 9 integers.
     |  
     |  Note that several fields' values are not the same as those defined by
     |  the C language standard for struct tm.  For example, the value of the
     |  field tm_year is the actual year, not year - 1900.  See individual
     |  fields' descriptions for details.
     |  
     |  Method resolution order:
     |      struct_time
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __reduce__(...)
     |      helper for pickle
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  tm_gmtoff
     |      offset from UTC in seconds
     |  
     |  tm_hour
     |      hours, range [0, 23]
     |  
     |  tm_isdst
     |      1 if summer time is in effect, 0 if not, and -1 if unknown
     |  
     |  tm_mday
     |      day of month, range [1, 31]
     |  
     |  tm_min
     |      minutes, range [0, 59]
     |  
     |  tm_mon
     |      month of year, range [1, 12]
     |  
     |  tm_sec
     |      seconds, range [0, 61])
     |  
     |  tm_wday
     |      day of week, range [0, 6], Monday is 0
     |  
     |  tm_yday
     |      day of year, range [1, 366]
     |  
     |  tm_year
     |      year, for example, 1993
     |  
     |  tm_zone
     |      abbreviation of timezone name
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  n_fields = 11
     |  
     |  n_sequence_fields = 9
     |  
     |  n_unnamed_fields = 0
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.

FUNCTIONS
    asctime(...)
        asctime([tuple]) -> string
        
        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
    
    clock(...)
        clock() -> floating point number
        
        Return the CPU time or real time since the start of the process or since
        the first call to clock().  This has as much precision as the system
        records.
    
    clock_getres(...)
        clock_getres(clk_id) -> floating point number
        
        Return the resolution (precision) of the specified clock clk_id.
    
    clock_gettime(...)
        clock_gettime(clk_id) -> floating point number
        
        Return the time of the specified clock clk_id.
    
    clock_settime(...)
        clock_settime(clk_id, time)
        
        Set the time of the specified clock clk_id.
    
    ctime(...)
        ctime(seconds) -> string
        
        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
    
    get_clock_info(...)
        get_clock_info(name: str) -> dict
        
        Get information of the specified clock.
    
    gmtime(...)
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.
        
        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
    
    localtime(...)
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)
        
        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
    
    mktime(...)
        mktime(tuple) -> floating point number
        
        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.
    
    monotonic(...)
        monotonic() -> float
        
        Monotonic clock, cannot go backward.
    
    perf_counter(...)
        perf_counter() -> float
        
        Performance counter for benchmarking.
    
    process_time(...)
        process_time() -> float
        
        Process time for profiling: sum of the kernel and user-space CPU time.
    
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
    
    strftime(...)
        strftime(format[, tuple]) -> string
        
        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    strptime(...)
        strptime(string, format) -> struct_time
        
        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).
        
        Commonly used format codes:
        
        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
    
    time(...)
        time() -> floating point number
        
        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.
    
    tzset(...)
        tzset()
        
        Initialize, or reinitialize, the local timezone to the value stored in
        os.environ['TZ']. The TZ environment variable should be specified in
        standard Unix timezone format as documented in the tzset man page
        (eg. 'US/Eastern', 'Europe/Amsterdam'). Unknown timezones will silently
        fall back to UTC. If the TZ environment variable is not set, the local
        timezone is set to the systems best guess of wallclock time.
        Changing the TZ environment variable without calling tzset *may* change
        the local timezone used by methods such as localtime, but this behaviour
        should not be relied on.

DATA
    CLOCK_MONOTONIC = 1
    CLOCK_MONOTONIC_RAW = 4
    CLOCK_PROCESS_CPUTIME_ID = 2
    CLOCK_REALTIME = 0
    CLOCK_THREAD_CPUTIME_ID = 3
    altzone = -19800
    daylight = 0
    timezone = -19800
    tzname = ('IST', 'IST')

FILE
    (built-in)


"""

exList = [5, 6, 7, 9, 11, 45]

# print max from the example list
print(max(exList))

# print minimum from the examplelist
print(min(exList))

# rounding numbers
x = 56.7790
print(round(x))

# math class and cieling, floor
import math as m

print(m.ceil(x))
print(m.floor(x))


# converting data types
intME = '78'
print(int(intME))

print(float(intME))

strMe = 110
print(str(strMe))
