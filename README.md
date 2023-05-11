# PySNRootFinder
This is a small project for a course in my major. The purpose of it is to estimate a root (whichever it is) of a specific function declared in the program (although it could work for any function) using the Secant method and the Newton-Raphson method.

It works by alternating both algorithms. With the required parameters, each algorithm calculates an approximation of the root and passes it to the next method to make a better approximation based on that value. This process continues until a desired level of accuracy is reached.

The data related to the operations and the output of every method is collected into a DataFrame.

# Versions
- **Python 3.11.1**
  - numpy 1.24.2
  - equation 1.2.1
  - matplotlib 3.7.1
  - pandas 2.0.0
