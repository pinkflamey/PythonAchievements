from math import ceil

total_trees = 333

print(total_trees, end="")
print(" trees in our field")

trees_in_mountain_shadow = total_trees / 3 * 2 # Schaduw bomen is 2/3 van alle bomen
trees_in_sun = total_trees - trees_in_mountain_shadow # Zonnige bomen is alle bomen min schaduw bomen

print(trees_in_sun, end="")
print(" trees in the sun")

print(trees_in_mountain_shadow, end="")
print(" trees in the mountain shadow")

apples_when_in_sun = 146
apples_when_in_shadow = apples_when_in_sun / 10 * 8 # Schaduw appels is 80% van de zonnige apples

print(apples_when_in_shadow, end="")
print(" shadow apples")

apples_of_sunnytrees = trees_in_sun * 146
apples_of_shady_trees = trees_in_mountain_shadow * apples_when_in_shadow

total_apples = ceil(apples_of_sunnytrees + apples_of_shady_trees) # Totala appels, naar boven afgerond

one_cut = total_apples // 3
leftover_apples = total_apples - one_cut * 3

print(one_cut, end="")
print(" apples per person")

print(leftover_apples, end="")
print(" leftover apple(s)")

print(total_apples, end="")
print(" total apples")

print("So, I am allowed to sell " + str(one_cut) + " apples, and we share " + str(leftover_apples) + " apple(s) to eat, because we can't divide it equally to sell.")

input("Press enter to quit...")