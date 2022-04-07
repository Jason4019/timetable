import requests
import pandas as pd

# your_class = input("input your class:")
your_class = 920611
url = f"https://iis.bsuir.by/api/v1/schedule?studentGroup={your_class}"


res = requests.get(url)
schedules = res.json()["schedules"]
timetable = []
for week in schedules:
    weekday = week["weekDay"]
    for schedule in week["schedule"]:
        auditory = schedule["auditory"][0]
        name = schedule["employee"][0]["firstName"] + ' ' + \
            schedule["employee"][0]["middleName"] + ' ' + schedule["employee"][0]["lastName"]
        lessonTime = schedule["lessonTime"]
        lessonType = schedule["lessonType"]
        weekNumber = schedule["weekNumber"]
        subject = schedule["subject"]
        subjectFullName = schedule["subjectFullName"]
        timetable.append({"auditory": auditory,
                          "name": name,
                          "lessonTime": lessonTime,
                          "lessonType": lessonType,
                          "weekday": weekday,
                          "weekNumber": weekNumber,
                          "subject": subject,
                          "subjectFullName": subjectFullName})
df = pd.DataFrame(timetable)
df.to_json("a.csv")
print(df)
res.close()
