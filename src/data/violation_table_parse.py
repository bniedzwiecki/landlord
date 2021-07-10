import pandas as pd
import json


def main():
    print("Hello!")
    tables = pd.ExcelFile('tables.xlsx')
    df1 = pd.read_excel(tables, "lowPoor")
    # df2 = pd.read_excel(tables, "ownerInNebraska")
    # df3 = pd.read_excel(tables, "ownerOutOfNebraska")
    violations_low = df1['VIOLATIONS'].tolist()
    res = json.loads(violations_low)
    print(res)
    # for index in range(len(violations_low)):
    #     print(violations_low[index])
    #     print(type(violations_low[index]))

    # violations_in = df2['VIOLATIONS'].tolist()
    # violations_out = df3['VIOLATIONS'].tolist()

    # for index in range(len(violations_low)):
    #     if violations_low[index] = '[]'
    #         continue


if __name__=='__main__':
    main()