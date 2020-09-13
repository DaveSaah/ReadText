__author__ = 'David Saah <dasorange.hope@gmail.com>'
__copyright__ = 'Copyright (c) 2020'

esd=str(input ("Enter a filename: "))
with open(esd) as f:
   print(f.read())