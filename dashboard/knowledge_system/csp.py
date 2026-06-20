import pandas as pd


class ShelterCSP:
    def __init__(self):
        self.shelters = pd.read_csv("utils/shelters.csv")

    def allocate(self, population):
        valid = self.shelters[
            (self.shelters["capacity"] >= population)
            & (self.shelters["road"] == "open")
            & (self.shelters["medical"] == True)
        ]

        if len(valid) == 0:
            return None

        return valid.sort_values("capacity").iloc[0].to_dict()
