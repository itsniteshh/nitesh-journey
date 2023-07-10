dog = {
    "kind": "four legged",
    "name": "tom",
    "owner": "nit"
}

cat = {
    "kind": "four legged",
    "name": "jerry",
    "owner": "prerna"
}

parrot = {
    "kind": "two legged",
    "name": "harry",
    "owner": "purnima"
}

pets = [dog, cat, parrot]

for p in pets:
    for k, v in p.items():
        print(k)
        print(f"{v}\n")