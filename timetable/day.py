import pandas as pd


def weektable(weeknumber):
    row = [
        "09:00-10:20",
        "10:35-11:55",
        "12:25-13:45",
        "14:00-15:20",
        "15:50-17:10",
        "17:25-18:45",
        "19:00-20:20",
        "20:35-21:55"]
    col = {"Понедельник": "周一",
           "Вторник": "周二",
           "Среда": "周三",
           "Четверг": "周四",
           "Пятница": "周五",
           "Суббота": "周六",
           "Воскресенье": "周日"}
    day = {"subject": "", "auditory": "", "lessonType": "", "lessonTime": "", "subjectFullName": ""}
    week = [[day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day],
            [day, day, day, day, day, day, day]
            ]
    dataset = pd.read_csv(weeknumber + ".csv")

    def find_location(dataset, row, col):
        for num in range(len(dataset["weekday"])):
            if dataset["weekday"].values[num] == col and dataset["lessonTime"].values[num] == row:
                return num
        return -1

    rnum = 0
    for i in row:
        cnum = 0
        for j in col:
            location = find_location(dataset, i, j)
            if location >= 0:
                week[rnum][cnum] = dataset.iloc[[location], 1:].to_dict("records")[0]
            cnum += 1
        rnum += 1
    # df = pd.DataFrame(week)
    # df.to_csv("weektable" + weeknumber + ".csv")
    return week
