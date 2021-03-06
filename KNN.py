from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def read_excel_files(loc):
    import xlrd 
    file = xlrd.open_workbook(loc)
    sheet = file.sheet_by_index(0)
    return sheet

# DataSet:
sheet = read_excel_files("C:/Users/A/Desktop/DataSet/Gender_DataSet.xlsx")
dataSet = []
for i in range(0, sheet.nrows):
    tmp_list = [sheet.cell_value(i, 0), sheet.cell_value(i, 1), sheet.cell_value(i, 2)]
    dataSet.append(tmp_list)
x = []
y = []
for i in range (0, len(dataSet)):
    tmp_list2 = [dataSet[i][0], dataSet[i][1]]
    x.append(tmp_list2)
    y.append(dataSet[i][2])

X_train = np.array(x).reshape(-1, 2)  
Y_train = np.array(y).reshape(-1, 1)

# TestSet
hight = int(input("enter Hight:    "))
weight = int(input("enter Weight:    "))
x_test = [[hight], [weight]]
X_test = np.array(x_test).reshape(-1, 2)  

### Create KNN Model
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, Y_train.ravel())
y_pred = neigh.predict(X_test)
print(X_test, "\n\n", y_pred)