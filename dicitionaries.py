"""Python Dictionaries"""

dict1 = {

    "name": "Nickson",
    "age": 31,
    "city": "Berlin",
    "town": None
}

for x in dict1.values():
    print(x)

print(dict1.get("city"))
print(dict1)
print(dict1["name"])
print(dict1["age"])

# changing values
dict1["age"] = 52
print(dict1)

dict1["city"] = "Vienna"
print(dict1)

# removing items
dict1.pop("age")
print(dict1)

f1_teams = {

    "team_1": {
        "name": "Mercedes",
        "drivers": ['Lewis', 'George']
    },

    "team_2": {
        "name": "Ferrari",
        "drivers": ['Charles', 'Sainz']
    }

}

"""Playing with dictionaries"""
print(f1_teams)
print(f1_teams.keys())
print(f1_teams['team_1'])
print(f1_teams['team_1']['drivers'][0])
print(f1_teams['team_1']['drivers'][1])
print(f1_teams['team_2'])
print(f1_teams.get('ye', 'Not Found'))

f1_teams['team_3'] = {'name': 'Aston Martin', 'drivers': ['Stroll', 'Alonso']}

print(f1_teams['team_3'])


print(f1_teams.values())
print(f1_teams.keys())

print(f1_teams.items())
for keys, values in f1_teams.items():
    print(keys, values)