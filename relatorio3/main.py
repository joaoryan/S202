from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()

pokemons = pokedex.getPokemonByName("Pikachu")
print("Name:")
print(pokemons)


writeAJson(pokemons, "Pikachu")

pokemons = pokedex.getPokemonsByWeaknesses(["Fire", "Rock"])
print("Weaknesses:")
print(pokemons)
writeAJson(pokemons, "Weaknesses")

pokemons = pokedex.getPokemonsByType(["Bug", "Flying"])
print("Types:")
print(pokemons)
writeAJson(pokemons, "Types")

pokemons = pokedex.getPokemonsByFire()
print("Fire:")
print(pokemons)
writeAJson(pokemons, "Fire")

pokemons = pokedex.getPokemonsByWeaknessesOne()
print("Weaknesses One:")
print(pokemons)
writeAJson(pokemons, "WeaknessesOne")

