RULES = [
    {
        "name": "TSUNAMI_RISK",
        "description": "Tsunami detected",
        "condition": lambda magnitude, tsunami: tsunami == 1,
    },
    {
        "name": "EXTREME_RISK",
        "description": "Extreme earthquake",
        "condition": lambda magnitude, tsunami: magnitude >= 8,
    },
    {
        "name": "HIGH_RISK",
        "description": "High magnitude earthquake",
        "condition": lambda magnitude, tsunami: 8 > magnitude >= 7,
    },
    {
        "name": "MODERATE_RISK",
        "description": "Moderate earthquake risk",
        "condition": lambda magnitude, tsunami: 6.5 <= magnitude < 7,
    },
]
