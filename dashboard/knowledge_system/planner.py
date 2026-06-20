from knowledge_system.csp import ShelterCSP
from knowledge_system.inference_engine import InferenceEngine


class SeismoGuardPlanner:
    def __init__(self):
        self.engine = InferenceEngine()  # from inference_engine.py
        self.csp = ShelterCSP()

    def generate_plan(self, magnitude, tsunami, population):
        result = self.engine.infer(magnitude, tsunami)

        category = result["category"]

        if category == "MODERATE_RISK":
            path = [
                "Earthquake Detected",
                "Assess Magnitude",
                "Send Public Alert",
                "Monitor Region",
                "Medical Response",
                "Population Safe",
            ]

        elif category == "HIGH_RISK":
            path = [
                "Earthquake Detected",
                "Assess Magnitude",
                "Send Public Alert",
                "Open Emergency Shelters",
                "Allocate Best Shelter",
                "Evacuate Population",
                "Medical Response",
                "Population Safe",
            ]

        elif category == "EXTREME_RISK":
            path = [
                "Earthquake Detected",
                "Assess Magnitude",
                "Send Public Alert",
                "Open Emergency Shelters",
                "Allocate Best Shelter",
                "Deploy Drones",
                "Damage Assessment",
                "Medical Response",
                "Population Safe",
            ]

        else:
            path = [
                "Earthquake Detected",
                "Assess Magnitude",
                "Send Public Alert",
                "Open Emergency Shelters",
                "Allocate Best Shelter",
                "Tsunami Warning",
                "Coastal Evacuation",
                "Medical Response",
                "Population Safe",
            ]

        shelter = self.csp.allocate(population)

        return {
            "category": category,
            "path": path,
            "rules": result["rules"],
            "shelter": shelter,
        }
