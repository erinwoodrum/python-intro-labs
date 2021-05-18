print('Can a swallow carry a coconut?')
swallow_limit = 60 / 3
print("swallow limit:", swallow_limit)

swallows_per_coconut = 1450/ swallow_limit
print("It takes ", swallows_per_coconut, "swallows to carry a coconut.")

swallows_per_apple = 128 / swallow_limit
print("It takes", swallows_per_apple, "swallows to carry an apple.")

swallows_per_cherry = 8 / swallow_limit
print("It takes", swallows_per_cherry, "swallows to carry a cherry.")
print("A swallow can carry a cherry!"
)
print('\n\n')
print('Can a Macaw carry a coconut?')
macaw_percent = 1/3
coconut_weight = 1450
macaw_weight = 900
macaws_per_coconut = coconut_weight / (macaw_weight * macaw_percent)
print("It takes", macaws_per_coconut, "to carry a coconut")

print('-----------------')
import math
print("Total whole macaws needed to carray coconut: ", math.ceil(macaws_per_coconut))