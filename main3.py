import json
import pickle


class Stadium:
    def __init__(self, name, age, capacity):
        self.name = name
        self.age = age
        self.capacity = capacity

    def __str__(self):
        return f"{self.name}, {self.age}, {self.capacity}"


st1 = Stadium("Old Trafford", 100, 12000)

java_format = json.dumps(st1.__dict__, indent=4)

with open("stadium_file.pickle", "wb") as file:
    pickle.dump(java_format, file)

with open("stadium_file.pickle", "rb") as file:
    new_java = pickle.load(file)

data = json.loads(new_java)

st2 = Stadium(data["name"], data["age"], data["capacity"])

print(st2)
