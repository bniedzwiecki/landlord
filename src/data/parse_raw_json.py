import json


def main():
    with open("lowPoorWornOutConditionParcels.json","r") as file:

        res = json.load(file)
        for row in range(len(res)):
            print(row)




if __name__ == '__main__':
    main()