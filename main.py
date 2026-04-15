from pet import Pet

pet = Pet("Milo", 50)

print("Pet name:", pet.name)
print("Energy level:", pet.energy_level)

pet.feed_pet()
print("Energy level after feeding:", pet.energy_level)