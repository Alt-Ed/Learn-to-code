"""
This program shows the basic conditional structures in Python.
Simple if-statement.
If-else statement.
If-elif-else statement.
Nested if statement.
"""

condition = True
another_condition = False

# example - simple if statement.
if condition:
    print('Condition is true!')

if not condition:
    print('Condition is false')

# if-else statement
if condition:
    print('Condition is true, if block executed')
else:
    print('Condition false, else block executed')

# if-elif-else statement
if condition:
    print('Condition is true')
elif not condition:
    print('Condition is false')
elif condition is another_condition:
    print('Both conditions have same value')
# optional else
else:
    print('None of the above conditions were met! Else block executed')

# Nested if
if condition:
    if another_condition:
        print('Both conditions were met!')
