import numpy as np

def DislayInfo(X,y):
    sumX = 0
    sumY = 0
    n = len(X)
    sum_1=0
    sum_2=0
    for i in range(len(X)):
        sumX += X[i]
        sumY += y[i]

    mean_X = sumX/n
    mean_y = sumY/n

    for i in range(len(X)):
        sum_1 += ((X[i] - mean_X)*(y[i] - mean_y))
        sum_2 += (X[i] - mean_X)**2

    slope_m = sum_1 / sum_2

    intercept = mean_y - (slope_m * mean_X)

    regression_result = (slope_m * mean_X) + intercept

    print("X_bar: ", mean_X)
    print("Y_bar: ", mean_y)
    print("Coefficient:", slope_m)
    print("Intercept: ", intercept)
    print("regression_result:", regression_result)

    

def main():
    X = np.array([1,2,3,4,5])
    y = np.array([3,4,2,4,5])
    DislayInfo(X,y)

if __name__ == "__main__":
    main()