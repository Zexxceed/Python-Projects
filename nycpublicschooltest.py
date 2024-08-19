# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Schools with Best Math Scores
best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values(by="average_math", ascending=False)

#Top 10 perfomring schools based on combined SAT Scores
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools.sort_values("total_SAT", ascending=False)[["school_name","total_SAT"]].head(10)

#Which single borough has the largest standard deviation in the combined SAT score?
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

#Max std
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

#Rework columns
largest_std_dev = largest_std_dev.rename(columns={"count":"num_schools","mean":"average_SAT","std":"std_SAT"})

largest_std_dev.reset_index(inplace=True)