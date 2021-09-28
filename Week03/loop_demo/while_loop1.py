"""
# File          : while_loop1.py
# Created       : 28.09.2021
# Author        : P. O'Neill
# Version       : v1.0.0
# Licencing     : (C) 2021 Pierce O'Neill, LYIT
#               Available under GNU Public License (GPL)
# Description     :
#
"""
if __name__ == '__main__':
    # sample while loop
    # max = 5
    # counter = 0
    # total = 0
    # while counter <= max:
    #     total += 9.99
    #     counter += 1
    # print("The final amount is: {0:5.2f}".format(total))

    # While true sample
    text = ""
    while 1:
        print("Enter Name")
        uname = input()
        if (uname == "joe"):
            break
        print("Finished")
