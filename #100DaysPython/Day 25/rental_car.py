def rental_car_cost(d):
    day_cost = 40
    if d >= 7:
        return (day_cost * d)- 50
    elif d >= 3:
        return (day_cost * d ) - 20
    
    else:
        return day_cost * d