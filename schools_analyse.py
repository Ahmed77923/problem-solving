import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
# print(schools.head())

# To find schools with average_math >= 640, filter the DataFrame directly
best_math_schools = schools[
    schools["average_math"] >= 640
][["school_name", "average_math"]].sort_values(
    "average_math", ascending=False
)
# If you want to keep the filtered DataFrame, assign it to a new variable, not as a column
# If you want to add a boolean column indicating if a school is a "best math school":
schools['best_math_school'] = schools["average_math"] >= 640

# Calculate total SAT score
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']

# To get the top 10 schools, use the filtered DataFrame
top_10_schools = schools.sort_values('total_SAT', ascending=False).head(10)[['school_name', 'total_SAT']]

# احسب الإحصائيات لكل borough
borough_stats = (
    schools
    .groupby('borough')
    .agg(
        num_schools=('total_SAT', 'count'),
        average_SAT=('total_SAT', 'mean'),
        std_SAT=('total_SAT', 'std')
    )
    .round(2)
)

largest_std_dev = (
    borough_stats
    .sort_values('std_SAT', ascending=False)
    .head(1)
    .reset_index()
)

print(largest_std_dev)

