"""
# File          : question2.py
# Created       : 28.09.2021
# Author        : P. O'Neill
# Version       : v1.0.0
# Licencing     : (C) 2021 Pierce O'Neill, LYIT
#               Available under GNU Public License (GPL)
# Description     :
#
"""
print ('Running Total')
print ()

book_1 =int (input('How much is Book 1? '))
book_2 =int (input('How much is Book 2? '))
book_3 =int (input('How much is Book 3? '))
book_4 =int (input('How much is Book 4? '))
book_5 =int (input('How much is Book 5? '))


running_total = float(book_1) + float(book_2) + float(book_3) + float(book_4) + float(book_5)

print ('Your running total is',running_total)
