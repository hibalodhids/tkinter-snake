import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# # Create DataFrame
# df = pd.DataFrame(mydataset)

# # Save to JSON file (records format: each row as a JSON object)
# df.to_json("mydatasethiba.json", orient="records", indent=2)

# print("JSON file saved!")


# df = pd.read_json("mydatasethiba.json")
# print(df)




#pip install pandas
# pd.DataFrame
# df.to_json("filename.json",orient="recorde",indent=2)
# pd.read_json


import pandas as pd

# mydataset = {
#     'name': ['Hamza', 'hiba', 'Sara'],
#     'age': [18, 20, 25],
#     'city': ['hyd', 'jam', 'qas']
# }


# # Convert to DataFrame
# df = pd.DataFrame(mydataset)

# # Print full dataset
# print(df)

# # Show first few rows
# print(df.head())

# # Summary statistics
# print(df.describe())

# # Filter rows where age is greater than 22
# print(df[df['age'] > 22])



df = pd.read_json('mydataset.json')

# print(df.to_string() ) 
print(df.loc[[0,1]] ) 