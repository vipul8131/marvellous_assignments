import numpy as np
from sklearn.metrics import confusion_matrix

def main():
    y_test = np.array([1,1,1,1,0,0,0,0])
    y_pred = np.array([1,1,0,1,0,1,0,0])

    conf_metrx = confusion_matrix(y_test, y_pred)

    print("Confusion Metrix:")
    print(conf_metrx)

if __name__ == "__main__":
    main()