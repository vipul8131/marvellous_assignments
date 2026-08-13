import math

def CalculateEucDistance(data, points):
    result = ((data['X'] - points['X'])**2) + ((data['Y']-points['Y'])**2)
    return math.sqrt(result)

def KNNClassfier(x,y, dataset):
    new_point = {'X': x, 'Y': y}
    for i in dataset:
        i['distance'] = CalculateEucDistance(i, new_point)

    #display dataset with distance
    for i in dataset:
        print(i)
    print("-"*50)
    # sorting and filter top 3 records
    sorted_data = sorted(dataset, key=lambda x:x['distance'])
    nearest_item = sorted_data[:3]
    print("-"*50)
    for i in nearest_item:
        print(i)
    print("-"*50)
    # get max number of count
    data = {}
    for i in nearest_item:
        data[i['label']] = data.get(i['label'],0) + 1

    # get final count of nearest point
    iMax = 0
    name = ''
    for i in data:
        if data[i] > iMax:
            iMax = data[i]
            name = i
    print("Predicted result is:",name)    

def main():
    x = int(input("Enter x cordinate:"))
    y = int(input("Enter y cordinate:"))

    dataset = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]
    KNNClassfier(x,y, dataset)

if __name__ == "__main__":
    main()