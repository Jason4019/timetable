import pandas as pd


def dis_week(week_num, data):
    dataset = pd.read_csv(data)
    j = 0
    ans = []
    for x in dataset["weekNumber"]:
        if x.find(week_num) >= 0:
            ans.append(j)
        j += 1
    print(ans, len(ans))
    dataset.iloc[ans, [7, 1, 4, 3, 8, 5]].to_csv(week_num+".csv")


for i in range(5):
    dis_week(str(i), "a.csv")
