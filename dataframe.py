# import pandas as pd
# #read data from csv file into dataframe
# df = pd.read_csv("mydataset.json",encoding="latin")utf-8
# print(df)

# import pandas as pd
# df = pd.read_json("mydatasethiba.json")
# print(df)

# import pandas as pd
# data =data = {
#     "Name": ['Faraz', 'Miral', 'Zoha'],
#     "Age": [12, 56, 78],
#     "City": ['Karachi', 'Lahore', 'Islamabad']
# }

# df = pd.DataFrame(data)
# print(df)

# df.to_csv("output.csv",index=False)
# df.to_json("output.xlsx",index=False)
# df.to_excel("output.json",index=False)

#version
# import pandas as pd
# print(pd.__version__)

#Series = A pandas series is like a column in a table(1_d)
import pandas as pd
a = [1,2,3]
myvar = pd.Series(a, index = ["x","y","z"])
print(myvar)
print(myvar["x"])

#key / value Object
import pandas as pd
animals = {"lion":3, "elephant":5, "zebra":8}
myvar = pd.Series(animals)
print(myvar)