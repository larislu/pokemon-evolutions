def branched_evolution(pokedex):
	pokedex[1][29] = 'Level 16'
	pokedex[1][30] = 'Moon Stone'
	pokedex[1][31] = 'Final'
	pokedex[1][32] = 'Level 16'
	pokedex[1][33] = 'Moon Stone'
	pokedex[1][34] = 'Final'

	pokedex[1][43] = 'Level 21'
	pokedex[1][44] = 'Leaf Stone'
	pokedex[2][44] = 'Sun Stone'
	pokedex[1][45] = 'Final'
	pokedex[2][182] = 'Final'

	pokedex[1][60] = 'Level 25'
	pokedex[1][61] = 'Water Stone'
	pokedex[2][61] = "Trade with King's Rock"
	pokedex[1][62] = 'Final'
	pokedex[2][186] = 'Final'

	pokedex[1][79] = 'Level 37'
	pokedex[2][79] = "Trade with King's Rock"
	pokedex[1][80] = 'Final'
	pokedex[2][199] = 'Final'

	pokedex[1][102] = 'Leaf Stone'
	pokedex[7][102] = 'Leaf Stone'
	pokedex[1][103] = 'Final'

	pokedex[1][104] = 'Level 28'
	pokedex[7][104] = 'Level 28 (Night)'
	pokedex[1][105] = 'Final'

	pokedex[1][133] = ['Water Stone', 'Thunder Stone', 'Fire Stone']
	pokedex[2][133] = ['Friendship (Day)', 'Friendship (Night)']
	pokedex[4][133] = ['Level up near Moss Rock', 'Level up near Ice Rock']
	pokedex[6][133] = 'Level up with 2 levels of Affection and knowing a Fairy-type move'
	pokedex[1][134] = 'Final'
	pokedex[1][135] = 'Final'
	pokedex[1][136] = 'Final'
	pokedex[2][196] = 'Final'
	pokedex[2][197] = 'Final'
	pokedex[4][470] = 'Final'
	pokedex[4][471] = 'Final'
	pokedex[6][700] = 'Final'

	pokedex[2][172] = 'Friendship'
	pokedex[1][25] = 'Thunder Stone'
	pokedex[7][25] = 'Thunder Stone'
	pokedex[1][26] = 'Final'

	pokedex[2][236] = ['Level 20 (Attack > Defense)', 'Level 20 (Attack < Defense)', 'Level 20 (Attack = Defense)']
	pokedex[1][106] = 'Final'
	pokedex[1][107] = 'Final'
	pokedex[2][237] = 'Final'

	pokedex[3][265] = ['Level 7 (Personality value mod 10 < 5)', 'Level 7 (Personality value mod 10 >= 5)']
	pokedex[3][266] = 'Level 10'
	pokedex[3][267] = 'Final'
	pokedex[3][268] = 'Level 10'
	pokedex[3][269] = 'Final'

	pokedex[3][280] = 'Level 20'
	pokedex[3][281] = 'Level 30'
	pokedex[4][281] = 'Dawn Stone (male)'
	pokedex[3][282] = 'Final'
	pokedex[4][475] = 'Final'

	pokedex[3][290] = ['Level 20', 'Appears if there is a Poke Ball in the bag and an empty space in the party']
	pokedex[3][291] = 'Final'
	pokedex[3][292] = 'Final'

	pokedex[3][361] = 'Level 42'
	pokedex[4][361] = 'Dawn Stone (female)'
	pokedex[3][362] = 'Final'
	pokedex[4][478] = 'Final'

	pokedex[3][366] = ['Trade holding Deep Sea Tooth', 'Trade holding Deep Sea Scale']
	pokedex[3][367] = 'Final'
	pokedex[3][368] = 'Final'

	pokedex[4][412] = ['Level 20 (female, Plant Cloak)', \
					   'Level 20 (female, Sandy Cloak)', \
					   'Level 20 (female, Trash Cloak)', \
					   'Level 20 (male)']
	pokedex[4][413] = 'Final'

	pokedex[7][744] = ['Level 25 in Pokemon Sun and Ultra Sun during the day', \
					   'Level 25 in Pokemon Moon and Ultra Moon at night', \
					   'Level 25 between 5:00 and 5:59 PM (special Rockrull with Own Tempo only)']
	pokedex[7][745] = 'Final'

	pokedex[7][789] = 'Level 43'
	pokedex[7][790] = ['Level 53 in Pokemon Sun and Ultra Sun', 'Level 53 in Pokemon Moon and Ultra Moon']
	pokedex[7][791] = 'Final'
	pokedex[7][792] = 'Final'

def galar(pokedex):
	pokedex[1][77] = 'Level 40'
	pokedex[1][78] = 'Final'

	pokedex[1][83] = 'Final'

	pokedex[1][109] = 'Level 35'
	pokedex[1][110] = 'Final'

	pokedex[3][263] = 'Level 20'
	pokedex[3][264] = 'Final'

	return

def edge_cases(pokedex):
	pokedex[4][422] = 'Level 30'
	pokedex[4][489] = 'Does not evolve'
	pokedex[5][585] = 'Level 34'
