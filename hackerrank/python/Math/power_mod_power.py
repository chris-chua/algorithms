# Read inputs
a = int(input())
b = int(input())
m = int(input())

# Calculate a^b and a^b mod m
a_to_power_of_b = pow(a, b)
a_to_power_of_b_mod_m = pow(a, b, m)

# Print results
print(a_to_power_of_b)
print(a_to_power_of_b_mod_m)