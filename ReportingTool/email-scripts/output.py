import sys
import pandas as pd
from pandas import DataFrame
import json
import collections


data=r'D:\DevOps-Training-Assignments\ReportingTool\email-scripts\response.json'
print ("This is json data input", data)

# Reads and converts json to dict.
def js_r(data):
   with open(data) as f_in:
       return(json.load(f_in))

def valuetype(dictionary):
    for key, value in dictionary.items():
        print type(value).__name__
        if(str(type(value).__name__) == 'dict'):
            mydata = convert(key)
            valuetype(mydata)
        else:
            print type(value).__name__ 
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data
if __name__ == "__main__":
    my_dic_data = js_r(data)
    valuetype(my_dic_data)   
    #print("This is my dictionary", my_dic_data)
# keys = my_dic_data.keys()
# print ("The original dict keys",keys)
# # You assign a new dictionary key- SO_users, and make dictionary comprehension = { your_key: old_dict[your_key] for your_key in your_keys }

# instances={'my_instances':my_dic_data['ec2']for key in keys}
# my_keys = instances.keys()

# print("these are my keys", my_keys)
# values={'my_value':instances['instance']for key in instances}

# print("these are my values keys", values.keys())
# print ("This is the dictionary of SO_users", instances)

# df4=pd.DataFrame(values)
# df=pd.DataFrame(instances)
# print ("df:", df)

# #When .apply(pd.Series) method on items column is applied, the dictionaries in items column will be used as column headings
# df2=df['my_instances'].apply(pd.Series)

       
# df2.to_csv('output.csv', index=False)
# print ("df2",df2)
# #df3=pd.concat([df2.drop(['user'],axis=1),df2['user'].apply(pd.Series)],axis=1)
# #df3=df2['user'].apply(pd.Series)

# #print ("df3",df3)