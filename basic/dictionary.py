## Initial dictionary

heroes = {'strength':'axe', 'agility':'monkey king'}
pahlawan = dict()

print(type(heroes))
print(type(pahlawan))

print(heroes)
print(heroes['strength'])

heroes['intelegence'] = 'tinker'
strength = heroes.get('strength')
print(heroes)
print(strength)

## remove dict item
print(heroes.pop('agility'))
print(heroes)