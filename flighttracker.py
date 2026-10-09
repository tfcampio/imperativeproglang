flight_route = [
    ("new york", "london"),("london", "paris"),("paris", "tokyo"), ("tokyo", "sydney")
]
def print_itinerary(route_list):
    print("flight itinerary schedule")
    for departure_city, arrival_city in route_list:
        print("departure:", departure_city, "--> arrival:", arrival_city)
print_itinerary(flight_route)
