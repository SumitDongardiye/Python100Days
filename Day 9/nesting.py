"""
Nesting list and dictionaries

{   
    Key: [List],
    Key2: {Dict}
}
"""

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# travel_log={
#     "France": ["Paries","Lille","Dijon"],
#     "Germany": ["Stuttgart","Berlin"]
# }

# print(travel_log["France"][1])

# nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

travel_log={
    "France": {
        "cities_visited": ["Paries","Lille","Dijon"],
        "total_visits":12
    },
    "Germany": {
        "cities_visited": ["Stuttgart","Berlin"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][1])