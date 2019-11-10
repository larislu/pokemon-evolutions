from hardcoded import branched_evolution, galar, edge_cases

ROMAN_NUMERALS = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7}
POKEDEX = {1: dict(), 2: dict(), 3: dict(), 4: dict(), 5: dict(), 6: dict(), 7: dict()}
CROSS_GEN = []

def which_gen(num):
	if num >= 1 and num <= 151:
		return 1
	elif num >= 152 and num <= 251:
		return 2
	elif num >= 252 and num <= 386:
		return 3
	elif num >= 387 and num <= 493:
		return 4
	elif num >= 494 and num <= 649:
		return 5
	elif num >= 650 and num <= 721:
		return 6
	elif num >= 722 and num <= 807:
		return 7

	'''
	GEN1 = (1, 151)
	GEN2 = (152, 251)
	GEN3 = (252, 386)
	GEN4 = (387, 493)
	GEN5 = (494, 649)
	GEN6 = (650, 721)
	GEN7 = (722, 807)
	'''


def two_pokemon(pokemon):

	first_evol = pokemon[0].split('|')
	first_num = int(first_evol[4][6:9])

	second_evol = pokemon[1].split('|')
	second_num = int(second_evol[4][6:9])
	method = second_evol[3][5:]

	first_gen = ROMAN_NUMERALS[first_evol[2]]
	second_gen = ROMAN_NUMERALS[second_evol[2]]
	gen = max(first_gen, second_gen)

	POKEDEX[gen][first_num] = method

	if which_gen(first_num) != which_gen(second_num):
		if gen != which_gen(first_num):
			POKEDEX[which_gen(first_num)][first_num] = 'Final'
		if gen != which_gen(second_num):
			POKEDEX[which_gen(second_num)][second_num] = 'Final'


def three_pokemon(pokemon):

	two_pokemon(pokemon[0:2])
	two_pokemon(pokemon[1:3])
		

def cross_gen():
	#read stuff
	with open('cross_gen.source') as f:
		source = f.read()

	families = source.split('|}')

	#hard coded ratata, it's easier this way
	POKEDEX[1][19] = 'Level 20'
	POKEDEX[1][20] = 'Final'

	for f in range(1, len(families)):
		pokemon = []
		if 'rowspan="2"' in families[f] or 'Galar' in families[f]:
			continue

		for line in families[f].split('\n'):
			if 'image=' in line:
				pokemon.append(line)
		if len(pokemon) == 2:
			two_pokemon(pokemon)
		elif len(pokemon) == 3:
			three_pokemon(pokemon)


def parse_families():
	with open('evolution_family.source') as f:
		source = f.read()

	families = source.split('{{')
	families = families[1:]

	for family in families:
		try:
			data = family.split('|')
			data = data[3:]
			data[-1] = data[-1].split('}}')[0]

			# one evolution
			if len(data) == 5:
				first_num = int(data[0])
				second_num = int(data[3])

				method = data[2]
				first_gen = which_gen(first_num)
				second_gen = which_gen(second_num)

				if first_num not in POKEDEX[first_gen]:
					POKEDEX[first_gen][first_num] = method
				if second_num not in POKEDEX[second_gen]:
					POKEDEX[second_gen][second_num] = 'Final'

			# two evolutions
			if len(data) == 8:
				first_num = int(data[0])
				second_num = int(data[3])
				third_num = int(data[6])

				first_method = data[2]
				second_method = data[5]

				first_gen = which_gen(first_num)
				second_gen = which_gen(second_num)
				third_gen = which_gen(third_num)

				if first_num not in POKEDEX[first_gen]:
					POKEDEX[first_gen][first_num] = first_method
				if second_num not in POKEDEX[second_gen]:
					POKEDEX[second_gen][second_num] = second_method
				if third_num not in POKEDEX[third_gen]:
					POKEDEX[third_gen][third_num] = 'Final'

			# no evolutions
			if len(data) == 2:
				num = int(data[0])
				gen = which_gen(num)
				
				if num not in POKEDEX[gen]:
					POKEDEX[gen][num] = 'Final'

		except:
			# I'll deal with it later
			continue

def fill_missing():
	for i in range(1, 152):
		if i not in POKEDEX[1]:
			POKEDEX[1][i] = 'Final'
	for i in range(152, 252):
		if i not in POKEDEX[2]:
			POKEDEX[2][i] = 'Final'
	for i in range(252, 387):
		if i not in POKEDEX[3]:
			POKEDEX[3][i] = 'Final'
	for i in range(387, 494):
		if i not in POKEDEX[4]:
			POKEDEX[4][i] = 'Final'
	for i in range(494, 650):
		if i not in POKEDEX[5]:
			POKEDEX[5][i] = 'Final'
	for i in range(650, 722):
		if i not in POKEDEX[6]:
			POKEDEX[6][i] = 'Final'
	for i in range(722, 808):
		if i not in POKEDEX[7]:
			POKEDEX[7][i] = 'Final'


def main():
	cross_gen()
	branched_evolution(POKEDEX)
	galar(POKEDEX)
	edge_cases(POKEDEX)

	parse_families()
	fill_missing()

	# Write out
	for gen, gen_data in POKEDEX.items():
		with open('gen{0}.csv'.format(gen), 'w') as file:
			for num in sorted(gen_data.keys()):
				if isinstance(gen_data[num], list):
					for method in gen_data[num]:
						file.write(str(num) + ',' + method + '\n')
				else:
					file.write(str(num) + ',' + gen_data[num] + '\n')


main()
#https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_with_branched_evolutions
#https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_evolution_family