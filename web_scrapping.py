import pandas as pd

states = ["California", "Texas", "Florida", "New York"]
population = [15645641321, 546545646465, 7897512374, 897454135464]

dict_states = { 'States' : states, "Populations": population }

for each in states:
    print(each)


# file creation via python 
with open('test.txt', 'w') as file: #with keyword closes the file automatically as soon as write lock is released
    file.write("Data successfully scrapped!")


# file creation via pandas
df_states  = pd.DataFrame.from_dict(dict_states)
print(df_states)
df_states.to_json('states.json')


# handleing exceptions: try-expect

new_list = [2, 4, 6, 'California']
for each in new_list:
    try:
        print(each/2)
    except: 
        print("The element is not a number")


# while break
while 