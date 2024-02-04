import json


class Surveys:
    _surveys = {}

    def _get_dict(self):
        return self._surveys

    def add_survey(self):
        print(self.Survey)

        survey = {}

        while True:
            name = input("Enter your name: ")
            if not name:
                break

            survey[name] = input("Enter your opinion: ")

        self._surveys[input("Enter name of survey: ")] = survey

    def del_survey(self):
        print(self.Survey)
        self._surveys.pop(input("Enter name of survey to delete: "))

    def load_data_in_file(self):
        with open("surveys_file.json", "w") as file:
            json.dump(self._surveys, file)

    def load_data_from_file(self):
        try:
            with open("surveys_file.json", "r") as file:
                self._surveys = json.load(file)

        except:
            raise Exception("There no surveys")

    Survey = property(fget=_get_dict)


obj = Surveys()

obj.add_survey()
obj.add_survey()

print(obj.Survey)

obj.load_data_in_file()
