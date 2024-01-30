import pandas as pd
import random

# Define the parameters
dorms_data = ["12", "13", "14", "15", "17", "18", "23", "24", "32", "33", "40", "43", "54", "55", "56", "57", "62", "63", "64"]
brody_home_stops = ["12", "13", "14", "15", "17", "18"]
south_home_stops = ["23", "24"]
east_home_stops = ["32", "33"]
north_home_stops = ["40", "43"]
shopping_home_stops = ["54", "55", "56"]
parkinglot_home_stops = ["62", "63", "64"]
bus_stops = ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", 
             "23", "24", "25", "26", "27", "30", "31", "32", "33", "34", "35", "36", "37", 
             "40","41", "42", "43", "44", "45", "46", "50", "51", "52", "53", "54", "55", 
             "56", "57", "60", "61", "62", "63", "64", "65", "66", "67"]
neighborhoods = ["East Neighborhood", "South Neighborhood", "North Neighborhood", "Brody Neighborhood", "Central Neighborhood"]
activities = ["Gym", "Swimming", "Library", "Cafeteria", "Music Practice", "Art Workshop", "Tennis", "Basketball"]
morning_class_times = ["8am", "9am", "10am", "11am", "12pm"]
afternoon_class_times = ["1pm", "2pm", "3pm", "4pm", "5pm"]
activity_times = ["6am", "7am", "8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm", "6pm", "7pm", "8pm", "9pm"]

# Create random data for 500 students
data = []
for _ in range(2500):
    name = f"Name{_}"
    last_name = f"LastName{_}"
    pid = random.randint(100000000, 999999999)
    home = random.choice(dorms_data)
    class1 = random.choice(bus_stops)
    class1_time = random.choice(morning_class_times)
    class2 = random.choice(bus_stops)
    class2_time = random.choice(afternoon_class_times)

    activity = random.choice(activities)
    activity_location = random.choice(bus_stops)
    activity_time = random.choice(activity_times)

    # Ensure activity time is not the same as class times
    while activity_time in [class1_time, class2_time]:
        activity_time = random.choice(activity_times)

    data.append([name, last_name, pid, home, class1, class1_time, class2, class2_time, activity, activity_location, activity_time])

# Create a DataFrame
df = pd.DataFrame(data, columns=["Name", "LastName", "PID", "Home", "Class1", "Class1Time", "Class2", "Class2Time", "Activity", "ActivityLocation", "ActivityTime"])

# Export to Excel
df.to_excel(r'C:\Users\15175\Desktop\Spartahack9\ClassDataSet.xlsx', index=False)

# Display the first few rows to verify the data
print(df.head())
