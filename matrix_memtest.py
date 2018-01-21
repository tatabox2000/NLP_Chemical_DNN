import numpy as np
import sys

class numpy_test():
    def __init__(self):
        self.num =1000000
    def numpy_matrix(self):
        matrix = np.arange(1,self.num+1,1)
        print(sys.getsizeof(matrix))
        # np.reshape(matrix,10)
        print(matrix)

if __name__ == '__main__':
    numpy_test = numpy_test()
    numpy_test.numpy_matrix()