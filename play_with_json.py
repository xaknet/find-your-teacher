import json

with open("teachers.json", "r") as json_file:
    context = json.loads(json_file.read())

for teacher in context["teachers"]:
    print(teacher.get("free"))
