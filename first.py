import pandas as pd
sf = pd.read_csv("data.csv")
# print(sf.head())
# print(sf.columns)
# print(sf.shape)
print(sf.info())
# print(sf.describe())
sf.drop(columns=['id', 'is_preparatory', 'program_duration', 'degree_short'], inplace=True)
print(sf.head())

print("New column Rank-difference")
sf["rank-diff"] = sf["closing_rank"] - sf["opening_rank"]
print(sf.head())

# print("mean age " + str(sf["Age"].max()))
most_competitive = (
    sf.groupby("program_name")["closing_rank"]
      .mean()
      .sort_values()
      .head(1)
)
print("Most Competitive Branch:")
print(most_competitive)

least_competitive = (
    sf.groupby("program_name")["closing_rank"]
    .mean()
    .sort_values()
    .tail(1)
)
print("Least Competitive Branch:")
print(least_competitive)

iit_nit_comparison = (
    sf.groupby("institute_type")["closing_rank"]
      .mean()
      .sort_values()
)

print("IIT vs NIT Competition Comparison:")
print(iit_nit_comparison)

catagory_counts = (
   sf.groupby("category")["closing_rank"]
      .mean()
      .sort_values() 

)
print("Category-wise Competition Comparison:")
print(catagory_counts)

cat_branch = (
    sf.groupby(["category", "program_name"])["closing_rank"]
      .mean()
      .sort_values()
      .head(10)
)

print("Top Competitive Category + Branch combos:")
print(cat_branch)

sf.to_csv("cleaned_data.csv", index=False)
print(sf)
