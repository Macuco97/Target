import json

# Sample data
data = {
    "faturamento": [
        {
            "dia": "2023-04-01",
            "valor": 500.0
        },
        {
            "dia": "2023-04-02",
            "valor": 800.0
        },
        {
            "dia": "2023-04-03",
            "valor": 1000.0
        },
        {
            "dia": "2023-04-04",
            "valor": 700.0
        },
        {
            "dia": "2023-04-05",
            "valor": 600.0
        },
        {
            "dia": "2023-04-06",
            "valor": 900.0
        },
        {
            "dia": "2023-04-07",
            "valor": 0.0
        },
        {
            "dia": "2023-04-08",
            "valor": 0.0
        },
        {
            "dia": "2023-04-09",
            "valor": 0.0
        },
        {
            "dia": "2023-04-10",
            "valor": 1200.0
        }
    ]
}

# Extracting values
values = [day["valor"] for day in data["faturamento"] if day["valor"] != 0]
minimum = min(values)
maximum = max(values)
mean = sum(values) / len(values)
above_mean = sum(1 for value in values if value > mean)

# Printing results
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
print(f"Days above average: {above_mean}")
