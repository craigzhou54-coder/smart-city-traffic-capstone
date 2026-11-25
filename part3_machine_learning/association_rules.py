import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

df = pd.read_csv(
    "../part2_python/data/processed/traffic_features.csv"
)

# Time of Day
def time_period(hour):
    if hour < 6:
        return "Night"
    elif hour < 12:
        return "Morning"
    elif hour < 18:
        return "Afternoon"
    else:
        return "Evening"

df["Time_Period"] = (
    df["Hour"]
    .apply(time_period)
)

# Apriori dataset
rules_df = pd.DataFrame()

rules_df["Night"] = (
    df["Time_Period"] == "Night"
)

rules_df["Morning"] = (
    df["Time_Period"] == "Morning"
)

rules_df["Afternoon"] = (
    df["Time_Period"] == "Afternoon"
)

rules_df["Evening"] = (
    df["Time_Period"] == "Evening"
)

rules_df["Weekend"] = (
    df["Weekend"] == 1
)

rules_df["Severe_Weather"] = (
    df["Severe_Weather"] == 1
)

rules_df["Low_Visibility"] = (
    df["Low_Visibility"] == 1
)

rules_df["High_Congestion"] = (
    df["Congestion_Category"]
    .isin(["High", "Severe"])
)

# Apriori

frequent_itemsets = apriori(
    rules_df,
    min_support=0.05,
    use_colnames=True
)

# Association Rules

rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1
)

# Rules of highest lift

rules = rules.sort_values(
    by="lift",
    ascending=False
)

print(
    rules[
        [
            "antecedents",
            "consequents",
            "support",
            "confidence",
            "lift"
        ]

   ].head(10)
)