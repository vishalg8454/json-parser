import my_json

json_str = '''
{
    "name": "Jane",
    "age": 27,
    "salary": 5.6e4,
    "skills": ["Python", "JavaScript", "SQL"],
    "married": false,
    "address": {
        "city": "New York",
        "zip": "10001"
    },
    "pets": null
}
'''

user = my_json.loads(json_str)
print("Name:", user['name'])
print("Age:", user['age'])
print("Salary:", user['salary'])
print("Number of skills:", len(user['skills']))
print("Lives in city:", user['address']['city'])