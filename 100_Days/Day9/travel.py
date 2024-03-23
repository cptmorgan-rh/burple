country = input()
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin"]
    },
]


def add_new_country(name, time_visited, cities_visited) -> None:
    travel_log.append({
        "country": name,
        "visits": time_visited,
        "cities": cities_visited
    })


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']}.")

print(travel_log)
