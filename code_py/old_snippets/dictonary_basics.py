# Dictionary Basics

# Not sequences, but mappings. That is, stored by key, not relative position.

# Dictionaries are mutable

# Build a dictionary via brackets
unef_org = {'name' : 'UNEF',
            'staff' : 32,
            'url' : 'http://unef.org'}

# View the variable
print(unef_org)

# Build a dict via keys
who_org = {}
who_org['name'] = 'WHO'
who_org['staff'] = '10'
who_org['url'] = 'http://who.org'

# View the variable
print(who_org)

# Nesting in dictionaries

# Build a dictionary via brackets
unitas_org = {'name' : 'UNITAS',
              'staff' : 32,
              'url' : ['http://unitas.org', 'http://unitas.int']}

# View the variable
print(unitas_org)

# Index the nested list

# Index the second item of the list nested in the url key.
print(unitas_org['url'][1])


