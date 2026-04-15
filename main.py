from pet import Pet

pet = Pet("Milo", 50)

print("Pet name:", pet.name)
print("Energy level:", pet.energy_level)

pet.play_with_pet()
print("Energy level after playing:", pet.energy_level)