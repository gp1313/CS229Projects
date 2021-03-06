
# -*- coding: utf-8 -*-
import time as tm
import math

def asMinutes(s):
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)

def timeSince(since, percent):
    if percent == 0:
        return 'Estimating training time...'
    now = tm.time()
    seconds_passed = now - since
    estimated_seconds = seconds_passed / (percent)
    remaining_seconds = estimated_seconds - seconds_passed
    return '(%s remaining)' % (asMinutes(remaining_seconds))

def time_past(since):
    now = tm.time()
    seconds_passed = now - since
    print '{0:.2f} seconds '.format(seconds_passed)