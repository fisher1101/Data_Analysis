import pandas as pd

data = pd.DataFrame({
    "OMG":["HJ","JH","AR"],
    "LVLZ":["JA","YI","JS"]
}, index = ["A","B","C"])

data["RCPC"] = pd.Series(["YK", "DH", "YH"], index = ["A", "B", "C"])
print(data)