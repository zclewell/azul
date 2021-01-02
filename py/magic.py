# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python

def rotate(arr):
    return list(zip(*arr[::-1]))
