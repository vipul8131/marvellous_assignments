import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, r2_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier, BaggingClassifier, RandomForestClassifier, AdaBoostClassifier

def main():
    df = pd.read_csv("Fraudulent_Transaction_Detection.csv")

    print(df.shape)
    # print(df.head(10))

    # checking if is there any missing value or empty column or null
    print(df.isnull().sum())

    # Splitting independant and dependant variables
    X = df.drop(columns=['Fraud'])
    y = df['Fraud']

    print(X.shape)
    print(y.shape)

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # splitting dataset into 4 parts for training and testing

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # load the models
    model_tree = DecisionTreeClassifier(max_depth=5)
    # train and predict Decisiontree model
    model_tree.fit(X_train, y_train)
    y_tree_pred = model_tree.predict(X_test)
    # accuracy of tree_model
    accuracy_tree = accuracy_score(y_test, y_tree_pred)
    print("Accuracy of Decisiontreeclassifier: ", accuracy_tree)

    print("Classfication report of Decisiontree:")
    print(classification_report(y_test, y_tree_pred))

    model_randforest = RandomForestClassifier(n_estimators=10)
    # train and predict Randomforestclassifier model
    model_randforest.fit(X_train, y_train)
    y_rf_pred = model_randforest.predict(X_test)
    # accuracy of tree_model
    accuracy_rf = accuracy_score(y_test, y_rf_pred)
    print("Accuracy of Randomforestclassifier: ", accuracy_rf)
    print("Classfication report of randomforest:")
    print(classification_report(y_test, y_rf_pred))

    model_bagging = BaggingClassifier(n_estimators=100, estimator=model_tree)
    # train and predict BaggingClassifier model
    model_bagging.fit(X_train, y_train)
    y_bag_pred = model_bagging.predict(X_test)
    # accuracy of tree_model
    accuracy_bag = accuracy_score(y_test, y_bag_pred)
    print("Accuracy of BaggingClassifier: ", accuracy_bag)
    print("Classfication report of BaggingClassifier:")
    print(classification_report(y_test, y_bag_pred))

    model_adaboost = AdaBoostClassifier(n_estimators=100)
    # train and predict AdaBoostClassifier model
    model_adaboost.fit(X_train, y_train)
    y_ada_pred = model_adaboost.predict(X_test)
    # accuracy of tree_model
    accuracy_ada = accuracy_score(y_test, y_ada_pred)
    print("Accuracy of AdaBoostClassifier: ", accuracy_ada)

    print("Classfication report of AdaBoostClassifier:")
    print(classification_report(y_test, y_ada_pred))

    model = VotingClassifier(estimators=[
        ("dt", model_tree),
        ("rf", model_randforest),
        ("ada", model_adaboost),
        ("bagging", model_bagging)
    ], voting='hard')

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy_model = accuracy_score(y_test, y_pred)

    print("Accuracy of the voting model:", accuracy_model)

    print("Classfication report of votingclassfier:")
    print(classification_report(y_test, y_pred))

    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("R2 score:")
    print(r2_score(y_test, y_pred))


if __name__ == "__main__":
    main()