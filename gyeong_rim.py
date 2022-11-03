import pandas as pd 
import ast
from random import randint
from random import seed
dic_str = []
#reset random number
seed(1)
for i in range(990):
    dic_str.append("{'a':"+str(randint(0, 100))+",'aa':"+str(randint(0, 100))+",'bb':"+str(randint(0, 100))+"}")   
# Create pandas DataFrame
datas = pd.DataFrame({'x1':range(0, 990),'x2':range(0, 990),'x3':dic_str,'x4':range(990, 0, - 1)})
print(datas)
# dictionary to hold all values 
main_dic = {}
#loop thru rows with string type dictionary values
for ind in datas.index:
    str_dic = datas['x3'][ind]
    #convert string to dictionary
    a_dic = ast.literal_eval(str_dic)
    #add dictory key value array
    for key in a_dic:
        if key in main_dic:
            main_dic[key].append(a_dic[key])
        else:
            main_dic[key] = []
            main_dic[key].append(a_dic[key])
#convert dictionary to datafram
df_main_dic = pd.DataFrame.from_dict(main_dic)
print(df_main_dic)
        
    

