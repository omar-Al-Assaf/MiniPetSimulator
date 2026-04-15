from pet import Pet

pet = Pet("Milo", 50)

print("Pet name:", pet.name)
print("Initial energy level:", pet.energy_level)

pet.feed_pet()
print("Energy after feeding:", pet.energy_level)

pet.play_with_pet()
print("Energy after playing:", pet.energy_level)