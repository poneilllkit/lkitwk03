"""
# File          : sample2_if.py
# Created       : 28.09.2021
# Author        : P. O'Neill
# Version       : v1.0.0
# Licencing     : (C) 2021 Pierce O'Neill, LYIT
#               Available under GNU Public License (GPL)
# Description     :
#
"""

if __name__ == '__main__':
    grade = 30
    module_1 = "python"

    if grade >= 70 and module_1 == "python":
        print('You have earned a Distinction!') # Comments can be placed anywhere
        # Remember that comments should be included to explain
        # all interesting sections of code!

    elif grade >= 60:
        print("You have earned an M.1.")
    elif grade >= 50:
        print("You have earned an M.2.")
    elif grade >= 40:
        print('You have passed')
    else:
        print("please try again")
