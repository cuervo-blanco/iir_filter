import numpy as np

class IIRFilter:
    def __init__(self, b_0, b_1, b_2, a_1, a_2):
        self.a = [1.0, a_1, a_2]
        self.b = [b_0, b_1, b_2]

    def filter(self, x, y):
        s_1 = 0;
        s_2 = 0;
        for i in range(len(x)):
            x_0 = x[i]
            y_0 = self.b[0] * x_0 + s_1
            s_1 = self.b[1] * x_0 + s_2 - self.a[1] * y_0
            s_2 = self.b[2] * x_0 - self.a[2] * y_0
            y[i] = y_0
