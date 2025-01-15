
#1. I used “import csv” to use the csv file in pycharm.


import csv
import statistics

#2. I set up a list, dictionary to ease the filtering process.
#“Time_Counts” will be used for the summarising process.

list1 = []
Which_State = {}
Time_Counts = {

#3. Each row will count when the accident happened per state.


    "Vic": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "SA": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "NSW": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "Qld": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "WA": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "NT": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "ACT": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
    "Tas": {"Dawn": 0, "Morning": 0, "Noon": 0, "Evening": 0, "Night": 0, "NaN": 0},
}


#4. I used the “def” function to reduce the overall length of the code.
#Since the code needs to process counts for 8 different states,
#without the def function, we would have to copy and paste the same
#code repeatedly for each state.


def categorize(state, time):
    if time:
        try:
            time_split = time.split(":")
            hour = int(time_split[0])

            if 0 <= hour < 5:
                Time_Counts[state]["Dawn"] += 1
            elif 5 <= hour < 9:
                Time_Counts[state]["Morning"] += 1
            elif 9 <= hour < 17:
                Time_Counts[state]["Noon"] += 1
            elif 17 <= hour < 21:
                Time_Counts[state]["Evening"] += 1
            else:
                Time_Counts[state]["Night"] += 1
        except ValueError:
            Time_Counts[state]["NaN"] += 1
    else:
        Time_Counts[state]["NaN"] += 1

# 6. In this process, it will filter out if there are
#missing values. The missing values will be counted as “NaN”



States = 0

Dawn = 0
Morning = 0
Noon = 0
Evening = 0
Night = 0
NaN = 0
is_first_line = True


for row in open("Cleaned_csv_crash_data.csv"):

#7. The first row is metadata, so this code passes over it.

    if is_first_line:
        is_first_line = False  # 첫 번째 줄(헤더)은 무시
    else:

        #8. Csv format is divided by ”,” in the text file, so I used the split method.

        values = row.split(",")  # 줄 바꿈 문자 제거 후 쉼표로 분리

        #9. Retrieve the fields

        Time = values[5]  # 시간 필드를 가져옴
        State = values[1] # 주(State) 필드를 가져옴
        Year = values[3]

        #10. Filtering 2017-2021 by using if statement.

        if int(Year) >= 2017:
            if State in Time_Counts:

                #11. Classifying accident counts by time of day using “def” above.

                categorize(State, Time)  # 시간대별로 사고 횟수 분류


#12. This code summarize the count of accident and calculate average.
total_dawn = 0
total_morning = 0
total_noon = 0
total_evening = 0
total_night = 0
total_nan = 0
state_count = len(Time_Counts)

for state in Time_Counts:
    print(f"{state}:")
    print(f"Dawn: {Time_Counts[state]['Dawn']} times")
    print(f"Morning: {Time_Counts[state]['Morning']} times")
    print(f"Noon: {Time_Counts[state]['Noon']} times")
    print(f"Evening: {Time_Counts[state]['Evening']} times")
    print(f"Night: {Time_Counts[state]['Night']} times")
    print(f"NaN: {Time_Counts[state]['NaN']} times")
    print()

    total_dawn += Time_Counts[state]['Dawn']
    total_morning += Time_Counts[state]['Morning']
    total_noon += Time_Counts[state]['Noon']
    total_evening += Time_Counts[state]['Evening']
    total_night += Time_Counts[state]['Night']
    total_nan += Time_Counts[state]['NaN']

avg_dawn = total_dawn / state_count
avg_morning = total_morning / state_count
avg_noon = total_noon / state_count
avg_evening = total_evening / state_count
avg_night = total_night / state_count
avg_nan = total_nan / state_count

print("Average accidents per time period across all states:")
print(f"Dawn: {avg_dawn:.2f} times on average")
print(f"Morning: {avg_morning:.2f} times on average")
print(f"Noon: {avg_noon:.2f} times on average")
print(f"Evening: {avg_evening:.2f} times on average")
print(f"Night: {avg_night:.2f} times on average")
print(f"NaN: {avg_nan:.2f} times on average")