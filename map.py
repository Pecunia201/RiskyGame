# Adjacency List for game map
adjacency_list = {
	# North America
	'Alaska': ['Northwest Territory', 'Alberta', 'Kamchatka'],
	'Alberta': ['Alaska', 'Northwest Territory', 'Ontario', 'Western US'],
	'Central America': ['Western US', 'Eastern US', 'Venezuela'],
	'Eastern US': ['Central America', 'Western US', 'Ontario', 'Quebec'],
	'Greenland': ['Quebec', 'Ontario', 'Northwest Territory', 'Iceland'],
	'Northwest Territory': ['Greenland', 'Ontario', 'Alberta', 'Alaska'],
	'Ontario': ['Northwest Territory', 'Alberta', 'Western US', 'Eastern US', 'Quebec', 'Greenland'],
	'Quebec': ['Greenland', 'Eastern US', 'Ontario'],
	'Western US': ['Central America', 'Eastern US', 'Ontario', 'Alberta'],

	# South America
	'Argentina': ['Peru', 'Brazil'],
	'Brazil': ['Argentina', 'Peru', 'Venezuela', 'North Africa'],
	'Venezuela': ['Brazil', 'Peru', 'Central America'],
	'Peru': ['Venezuela', 'Brazil', 'Argentina'],
	
	# Africa
	'Congo': ['South Africa', 'East Africa', 'North Africa'],
	'East Africa': ['Congo', 'South Africa', 'Egypt', 'North Africa', 'Madagascar'],
	'Egypt': ['North Africa', 'East Africa', 'Middle East', 'Southern Europe'],
	'Madagascar': ['South Africa', 'East Africa'],
	'North Africa': ['Congo', 'East Africa', 'Egypt', 'Southern Europe', 'Western Europe', 'Brazil'],
	'South Africa': ['Madagascar', 'Congo', 'East Africa'],

	# Europe
	'Great Britain': ['Iceland', 'Scandinavia', 'Northern Europe', 'Western Europe'],
	'Iceland': ['Great Britain', 'Scandinavia', 'Greenland'],
	'Northern Europe': ['Scandinavia', 'Great Britain', 'Western Europe', 'Southern Europe', 'Ukraine'],
	'Scandinavia': ['Ukraine', 'Northern Europe', 'Great Britain', 'Iceland'],
	'Southern Europe': ['Western Europe', 'Northern Europe', 'Ukraine', 'Middle East', 'Egypt', 'North Africa'],
	'Ukraine': ['Scandinavia', 'Northern Europe', 'Southern Europe', 'Middle East', 'Afghanistan', 'Ural'],
	'Western Europe': ['Southern Europe', 'Northern Europe', 'Great Britain', 'North Africa'],
	
	# Asia
	'Afghanistan': ['Middle East', 'India', 'China', 'Ural', 'Ukraine'],
	'China': ['Siam', 'India', 'Afghanistan', 'Ural', 'Siberia', 'Mongolia'],
	'India': ['Siam', 'China', 'Afghanistan', 'Middle East'],
	'Irkutsk': ['Mongolia', 'Siberia', 'Yakutsk', 'Kamchatka'],
	'Japan': ['Kamchatka', 'Mongolia'],
	'Kamchatka': ['Japan', 'Mongolia', 'Irkutsk', 'Yakutsk', 'Alaska'],
	'Middle East': ['India', 'Afghanistan', 'Ukraine', 'Southern Europe', 'Egypt'],
	'Mongolia': ['China', 'Japan', 'Kamchatka', 'Irkutsk', 'Siberia'],
	'Siam': ['China', 'India', 'Indonesia'],
	'Siberia': ['Ural', 'China', 'Mongolia', 'Irkutsk', 'Yakutsk'],
	'Ural': ['Siberia', 'China', 'Afghanistan', 'Ukraine'],
	'Yakutsk': ['Siberia', 'Irkutsk', 'Kamchatka'],

	# Oceania
 	'Eastern Australia': ['New Guinea', 'Western Australia'],
	'New Guinea': ['Eastern Australia', 'Western Australia', 'Indonesia'],
	'Indonesia': ['New Guinea', 'Western Australia', 'Siam'],
	'Western Australia': ['Eastern Australia', 'Indonesia', 'New Guinea'],
}

# Node positions on map
node_positions = {
	# North America
	'Alaska': (70, 200),
	'Alberta': (170, 300),
	'Central America': (270, 500),
	'Eastern US': (320, 400),
	'Greenland': (420, 150),
	'Northwest Territory': (270, 200),
	'Ontario': (270, 300),
	'Quebec': (370, 300),
	'Western US': (220, 400),

	# South America
	'Argentina': (300, 1000),
	'Brazil': (600, 800),
	'Venezuela': (400, 600),
	'Peru': (250, 750),

	# Africa
	'Congo': (900, 900),
	'East Africa': (1200, 800),
	'Egypt': (1200, 600),
	'Madagascar': (1240, 970),
	'North Africa': (800, 600),
	'South Africa': (1100, 1100),

	# Europe
	'Great Britain': (800, 300),
	'Iceland': (850, 150),
	'Northern Europe': (1100, 300),
	'Scandinavia': (1100, 170),
	'Southern Europe': (1150, 400),
	'Ukraine': (1300, 250),
	'Western Europe': (900, 400),

	# Asia
	'Afghanistan': (1500, 400),
	'China': (1700, 500),
	'India': (1500, 600),
	'Irkutsk': (1800, 300),
	'Japan': (1900, 500),
	'Kamchatka': (1920, 240),
	'Middle East': (1300, 500),
	'Mongolia': (1750, 400),
	'Siam': (1700, 700),
	'Siberia': (1700, 160),
	'Ural': (1550, 210),
	'Yakutsk': (1800, 180),

	# Oceania
	'Eastern Australia': (1850, 1000),
	'New Guinea': (1800, 900),
	'Indonesia': (1600, 950),
	'Western Australia': (1650, 1100),
}

# Territory atrributes
player1 = 'Player1'

territory_owned = {
	# North America
	'Alaska': [None, 0],
	'Alberta': [None, 0],
	'Central America': [player1, 0],
	'Eastern US': [player1, 0],
	'Greenland': [None, 0],
	'Northwest Territory': [None, 0],
	'Ontario': [None, 0],
	'Quebec': [None, 0],
	'Western US': [None, 0],

	# South America
	'Argentina': [None, 0],
	'Brazil': [None, 0],
	'Venezuela': [None, 0],
	'Peru': [None, 0],
	
	# Africa
	'Congo': [None, 0],
	'East Africa': [None, 0],
	'Egypt': [None, 0],
	'Madagascar': [None, 0],
	'North Africa': [None, 0],
	'South Africa': [None, 0],

	# Europe
	'Great Britain': [None, 0],
	'Iceland': [None, 0],
	'Northern Europe': [None, 0],
	'Scandinavia': [None, 0],
	'Southern Europe': [None, 0],
	'Ukraine': [None, 0],
	'Western Europe': [None, 0],
	
	# Asia
	'Afghanistan': [None, 0],
	'China': [None, 0],
	'India': [None, 0],
	'Irkutsk': [None, 0],
	'Japan': [None, 0],
	'Kamchatka': [None, 0],
	'Middle East': [None, 0],
	'Mongolia': [None, 0],
	'Siam': [None, 0],
	'Siberia': [None, 0],
	'Ural': [None, 0],
	'Yakutsk': [None, 0],

	# Oceania
 	'Eastern Australia': [player1, 0],
	'New Guinea': [player1, 0],
	'Indonesia': [player1, 0],
	'Western Australia': [player1, 0],
}