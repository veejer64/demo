import pandas as pd

#
#  Just a file to demonstrate dependency management with venv
#  

def func1():
    inputfile = "testfile.txt"
    datafile = pd.read_csv(inputfile)


if __name__ == '__main__':
    func1()
