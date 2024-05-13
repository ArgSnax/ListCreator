# Title: List Creator
# By: Chance Brown
# Date: 5/3/2024

#Functions
def createType(type):
    if(type == "list"):
        finType = []
    elif(type == "tuple"):
        finType = ()
    elif(type == "dictionary"):
        finType = {}
    else:
        #Make it so itsd a list but once done it is converted to a set, and so on so forth
        finType = {"placeholder", "placeholder"}
    return finType

def addFixedNums(num, dataset):
    numControl = 1
    while(num > 0):
        if(type(dataset) == set):
            if(numControl == 1):
                dataset = list(dataset)
                dataset.clear()
                dataset.append("setControl")
        elif(type(dataset) == tuple):
            if(numControl == 1):
                dataset = list(dataset)
                dataset.append("tupleControl")
        elif(type(dataset) == dict):
            dataset.update({("key" + str(numControl)): ("value" + str(numControl))})
        elif(type(dataset) == list):
            dataset.append("item" + str(numControl))
            if("setControl" in dataset and num <= 1):
                dataset[0] = "item1"
                dataset = set(dataset)
            if("tupleControl" in dataset and num <= 1):
                dataset[0] = "item1"
                dataset = tuple(dataset)
        numControl += 1
        num  = num - 1

    return dataset
#Intro For User
print(
    "\nList Creator\n\n"
    "This is a in-class program made by Chance Brown to test \nhis coding skills from tutorials"
    " he had recently watched.\n\n"
    "This program is a simple dataset creator to create the 4 types of data sets, \nand modify them. \n"
)

#Gathering Info
userType = input("What type of variable set would you like to create? (Ex. List, Tuple, Dictionary, Set): ").lower()
dataSet = createType(userType)
numVars = int(input("How many variables would you like to add?: "))
newDataSet = addFixedNums(numVars, dataSet)
print(newDataSet, "\n")
print(type(newDataSet))
while True:
    mod = str(input("Would you like to modify an item?: "))

    if(mod == "Yes" or mod == "yes"):
        itemType = str(type(newDataSet))
        modNum = (int(input("Which numbered item? (ex: 1): "))-1)
        modItem = str(input("What should the item name be?: "))
        if(itemType == "<class 'list'>"):
            newDataSet[modNum] = modItem
            print(newDataSet)
        elif(itemType == "<class 'dict'>"):
            modValue = str(input("What should the value be?: "))
            newDataSet[modItem] = newDataSet.pop(f'key{modNum+1}')
            newDataSet.update({modItem: modValue})
            print(newDataSet)
        elif(itemType == "<class 'set'>"):
            newDataSet = list(newDataSet)
            print(newDataSet)
            newDataSet[modNum] = modItem
            newDataSet = set(newDataSet)
            print(newDataSet)
        elif(itemType == "<class 'tuple'>"):
            newDataSet = list(newDataSet)
            newDataSet[modNum] = modItem
            newDataSet = tuple(newDataSet)
            print(newDataSet)
    else:
        break