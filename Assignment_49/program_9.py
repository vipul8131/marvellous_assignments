import numpy as np
from sklearn.metrics import classification_report

def main():
    y_test = np.array([1,1,1,1,0,0,0,0])
    y_pred = np.array([1,1,0,1,0,1,0,0])

    cls_report = classification_report(y_test, y_pred)

    print("Colassification report:")
    print(cls_report)

if __name__ == "__main__":
    main()