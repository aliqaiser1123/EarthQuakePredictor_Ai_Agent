from collections import deque

MASTER_GRAPH = {
    "Earthquake Detected": ["Assess Magnitude"],
    "Assess Magnitude": ["Send Public Alert"],
    "Send Public Alert": ["Open Emergency Shelters", "Monitor Region"],
    "Open Emergency Shelters": ["Allocate Best Shelter"],
    "Allocate Best Shelter": [
        "Monitor Region",
        "Evacuate Population",
        "Deploy Drones",
        "Tsunami Warning",
    ],
    "Monitor Region": ["Population Safe", "Medical Response"],
    "Evacuate Population": ["Medical Response"],
    "Deploy Drones": ["Damage Assessment"],
    "Damage Assessment": ["Medical Response"],
    "Tsunami Warning": ["Coastal Evacuation"],
    "Coastal Evacuation": ["Medical Response"],
    "Medical Response": ["Population Safe"],
}


class BFSAgent:
    def search(self, graph, start, goal):
        queue = deque()

        queue.append((start, [start]))

        visited = set()

        visited_order = []

        while queue:
            node, path = queue.popleft()

            if node not in visited:
                visited.add(node)

                visited_order.append(node)

                if node == goal:
                    return path, visited_order

                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return [], visited_order
