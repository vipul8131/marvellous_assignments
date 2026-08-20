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
    ss_tot = 0
    for i in range(len(X)):
        sum_1 += ((X[i] - mean_X)*(y[i] - mean_y))
        sum_2 += (X[i] - mean_X)**2
        ss_tot += (y[i] - mean_y)**2

    slope_m = sum_1 / sum_2

    intercept = mean_y - (slope_m * mean_X)

    y_values = []
    for i in range(len(X)):
        print(f"value of {X[i]}: {(slope_m * X[i]) + intercept}")
        y_values.append((slope_m * X[i]) + intercept)

    data = 0
    for i in range(len(y)):
        print(y_values[i])
        data += (y[i] - y_values[i])**2
    
    MSE = data/n

    print("Mean Squared Error: ", MSE)

    ss_res = data

    R2_score = 1 - (ss_res/ss_tot)

    print("R2 score:", R2_score)

def main():
    X = np.array([1,2,3,4,5])
    y = np.array([3,4,2,4,5])
    DislayInfo(X,y)

if __name__ == "__main__":
    main()