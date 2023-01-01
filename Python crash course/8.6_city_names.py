def city_country(city_name, country):
    #returns a formatted city and country name
    details = f"{city_name}, {country}"
    return details.title()

info = city_country("mumbai", "india")
print(info)