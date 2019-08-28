# using two methods write the expected outout:


attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# # expected outout:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

ans1 = [{attr:value for attr,value in zip(attributes,person)} for person in values]

ans2 = []

for value in values :
    temp = dict(zip(attributes,value))
    ans2.append(temp)

print(ans1)
print(ans2)


