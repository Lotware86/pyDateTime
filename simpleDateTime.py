# Bosco Lo - Fall 2018 - 11:51 PM 06 Nov 2018 - C programming for fun - All rights reserved
import time as t

year, month, days, hour, minute, seconds = t.strftime("%Y,%m,%d,%H,%M, %S").split(',')
seconds_from_beginning_of_month = int(days) * 86400 + int(hour) * 3600 \
                                    + int(minute) * 60 + int(seconds)
print("\n" + seconds_from_beginning_of_month.__str__() + " seconds from first day of the month.\n")
print(t.strftime("%a, %d %b %Y at %H:%M:%S GMT%z %Z"))
