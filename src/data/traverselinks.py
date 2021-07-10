import json
import pandas as pd
import numpy as np

def main():
    df1 = pd.read_json("lowPoorWornOutConditionParcels.json")
    df2 = pd.read_json("ownerInNebraskaOutOfOmahaParcels.json")
    df3 = pd.read_json("ownerOutOfNebraskaParcels.json")
    
    violations1 = df1["VIOLATION_LINKS"]
    violations2 = df2["VIOLATION_LINKS"]
    violations3 = df3["VIOLATION_LINKS"]

    links_list = []
    for row in violations1:
        print(row)
    # links = df["VIOLATIONS"]
    # links.to_excel("links.xlsx")
    with pd.ExcelWriter("tables.xlsx") as writer:
        df1.to_excel(writer, sheet_name="lowPoor")
        df2.to_excel(writer, sheet_name="ownerInNebraska")
        df3.to_excel(writer, sheet_name="ownerOutOfNebraska")
        violations1.to_excel(writer, sheet_name="links1")
        violations2.to_excel(writer, sheet_name="links2")
        violations3.to_excel(writer, sheet_name="links3")





if __name__=='__main__':
    main()