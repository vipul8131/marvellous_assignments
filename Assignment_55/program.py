import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.preprocessing import StandardScaler

def main():
    df = pd.read_csv("Customer_Loan_Approval.csv")
    print(df.head())
    # print(df.shape)
    # check if is there any value missing oe null columns
    print(df.isnull().sum())

    # splitting dependant and independant variables
    X = df.drop(columns=['LoanApproved'])
    y = df['LoanApproved']

    print("X.shape: ", X.shape)
    print("y.shape", y.shape)

    # Scaling data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Splitting variables for training and testing
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # load models
    tree_model = DecisionTreeClassifier(max_depth=5)

    # train and predict Decisiontree model
    tree_model.fit(X_train, y_train)
    y_tree_pred = tree_model.predict(X_test)
    # accuracy of tree_model
    accuracy_tree = accuracy_score(y_test, y_tree_pred)
    print("Accuracy of Decisiontreeclassifier: ", accuracy_tree)

    knn_model = KNeighborsClassifier(n_neighbors=5)
    # train and test KNN model
    knn_model.fit(X_train, y_train)
    y_knn_pred = knn_model.predict(X_test)
    accuracy_knn = accuracy_score(y_test, y_knn_pred)
    print("Accuracy of KNN:", accuracy_knn)

    logi_model = LogisticRegression(max_iter=1000)
    # train and test logistic regression model
    logi_model.fit(X_train, y_train)
    y_logi_pred = logi_model.predict(X_test)
    accuracy_logi = accuracy_score(y_test, y_logi_pred)

    print("Accuracy of Logistic regression model:", accuracy_logi)

    model = VotingClassifier(estimators=[
        ('logistic', logi_model),
    ('decision_tree', tree_model),
    ('knn', knn_model)
    ], voting='soft')

    # train model
    model.fit(X_train, y_train)
    # test the model
    y_pred_soft = model.predict(X_test)

    accuracy_score_soft = accuracy_score(y_test, y_pred_soft)
    print("Accuracy of VotingClassifier soft:", accuracy_score_soft)

    ##################################################

    odel = VotingClassifier(estimators=[
        ('logistic', logi_model),
    ('decision_tree', tree_model),
    ('knn', knn_model)
    ], voting='hard')

    # train model
    model.fit(X_train, y_train)
    # test the model
    y_pred_hard = model.predict(X_test)

    accuracy_score_hard = accuracy_score(y_test, y_pred_hard)
    print("Accuracy of VotingClassifier hard:", accuracy_score_hard)



if __name__ == "__main__":
    main()