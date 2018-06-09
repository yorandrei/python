import sys

print('What is your name?')
name = sys.stdin.readline()
#print('Hello', name)
print('Hello, ' +  name.rstrip() + '!')

""" execute shell command command from vim:
:! python uinput.py
"""

""" read output of shell command into a buffer
:r ! dir
"""

""" Open interactive shell in vim:
:sh
"""
