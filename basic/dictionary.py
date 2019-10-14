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

## extras
print(heroes.keys())
print(heroes.values())
print(heroes.items())

## remove dict item
print(heroes.pop('agility'))
print(heroes)
print(heroes.popitem())
print(heroes)
heroes.clear()

a = {'kode':'a',
    'nama':'bambang',
    'alamat':'jekardah'}
b = {'kode':'b',
    'nama':'jaka',
    'alamat':'semarang'}
grouplist = {'a':a,
            'b':b}
print(grouplist['a'])