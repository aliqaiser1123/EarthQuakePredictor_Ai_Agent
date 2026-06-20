from knowledge_system.knowledge_base import RULES


class InferenceEngine:
    def infer(self, magnitude, tsunami):
        triggered_rules = []

        selected_category = None

        for rule in RULES:
            if rule["condition"](magnitude, tsunami):
                triggered_rules.append(rule["description"])

                selected_category = rule["name"]

                break

        return {"category": selected_category, "rules": triggered_rules}
