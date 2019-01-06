# -*- coding: utf-8 -*-
# Function helps u guess if year is leap
import unittest


def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 4 != 0:
        return True
    return False


a = isYearLeap(2000)
print(a)