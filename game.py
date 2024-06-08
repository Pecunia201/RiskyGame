import pygame
from map import adjacency_list, node_positions, player1, territory_owned
from bfs import BreadthFirstSearch
from render import render_all

# Initialise Pygame
pygame.init()


# Set up the display
WIDTH, HEIGHT = 2000, 1200

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Risky Game")

selected_node = None
destination_node = None
attacking_node = False

# Update node positions based on the current screen size
original_width, original_height = 2000, 1200
scale_x = WIDTH / original_width
scale_y = HEIGHT / original_height

scaled_node_positions = { # dict of new scaled node positions
	node: (int(pos[0] * scale_x), int(pos[1] * scale_y))
	for node, pos in node_positions.items()
}

render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y)

last_screen_size = (WIDTH, HEIGHT)

# Main loop
running = True
while running:
	# Event handlers
	for event in pygame.event.get():
		# Quit application
		if event.type == pygame.QUIT:
			running = False

		# Handle resizing
		elif event.type == pygame.VIDEORESIZE:
			WIDTH, HEIGHT = event.size
			screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

		# Mouse click
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: # Left mouse button
				mouse_x, mouse_y = event.pos
				# Check if the mouse click is within proximity of any nodes
				for node_name, (node_x, node_y) in scaled_node_positions.items():
					node_radius = int(30 * min(scale_x, scale_y)) # Hit box for selecting a node ( ! NEEDS SCALING ! )
					if (mouse_x - node_x)**2 + (mouse_y - node_y)**2 <= node_radius**2:
						
						# If the territory clicked on is owned by the player
						if territory_owned[node_name][0] == player1:
							# Select a node
							if selected_node == None:
								selected_node = node_name
								render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y)
							# Unselect a node
							elif selected_node == node_name:
								selected_node = None
								destination_node = None
								render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y)

						# If a node has been selected, select a destination
						if selected_node != None and node_name != selected_node:
							# If an ubstructed path can be established between the selected node and the proposed destination
							if territory_owned[node_name][0] == player1:
								# Verify path using Breadth First Search (BFS)
								is_reachable = BreadthFirstSearch(selected_node, node_name)
								if is_reachable:
									attacking_node = False
									print('Destination set to ' + node_name)
									destination_node = node_name
									render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y)
								else:
									print("Unreachable! Select another location.")

							# If the proposed destination is not owned by the player but is adjacent to the selected player owned node
							elif territory_owned[node_name][0] != player1 and node_name in adjacency_list[selected_node]:
								print('Attacking ' + node_name)
								destination_node = node_name
								attacking_node = True
								render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y)

	# Handle scaling of objects during screen resizing
	if (WIDTH, HEIGHT) != last_screen_size:
		# Update node positions based on the current screen size
		scale_x = WIDTH / original_width
		scale_y = HEIGHT / original_height

		scaled_node_positions = { # dict of new scaled node positions
			node: (int(pos[0] * scale_x), int(pos[1] * scale_y))
			for node, pos in node_positions.items()
		}
		
		# Update last known screen size
		last_screen_size = (WIDTH, HEIGHT)

		# Render everything
		render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y)


# Quit Pygame
pygame.quit()
