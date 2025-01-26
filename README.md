# Uncommon Python Bug: Robust Average Calculation

This repository demonstrates a potential error in Python when calculating the average of a list of numbers and showcases a robust solution. The bug involves cases where the input list is empty or contains non-numeric elements. The solution implements comprehensive error handling to address these scenarios. 

## Bug
The original code handles the empty list case correctly but fails when a non-numeric value is present, leading to a `TypeError`. The solution improves the function by performing a type check on each element before performing the calculation.