spec = {"backend": "Mongodb", "frontend": "AngularJS"}

# Output 1: Print the value associated with the key 'backend'
print(spec["backend"])

# Output 2: Create a new dictionary with the existing key-value pairs and add a new key 'App' with the value 'website'
output_2 = spec.copy()
output_2['App'] = 'website'
print(output_2)

# Output 3: Create a new dictionary with only the keys 'backend' and 'App'
output_3 = {'backend': spec['backend'], 'App': 'website'}
print(output_3)
    