from prettytable import PrettyTable

pokemon = PrettyTable()

pokemon.add_column("Pokemon", ["Pikachu", "Squirtle", "Bulbasaur", "Charmendar"])
pokemon.add_column("Type", ["Electric", "Water", "Grass", "Fire"])
pokemon.align = "c"

print(pokemon)