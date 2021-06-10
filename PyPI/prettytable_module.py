from prettytable import PrettyTable

table = PrettyTable()

# table.field_names = ['Pokemons', 'Type']
# table.add_row(['Pikachu', 'Electric'])
# table.add_row(['Squirtle', 'water'])
# table.add_row(['Charamander', 'Fire'])

# 別解
table.add_column("Pokemon Name", ["Pikachuu", "Squirtle", "Charamander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# 左揃え
table.align = "l"

print(table)
