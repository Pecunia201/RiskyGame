import pygame
from map import adjacency_list, player1, territory_owned

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def draw_line(screen, color, start_pos, end_pos, thickness=2):
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

def draw_circle(screen, color, pos, radius, thickness=0):
    pygame.draw.circle(screen, color, pos, radius, thickness)



def render_connections_between_nodes(scaled_node_positions, screen, selected_node, destination_node, attacking_node):
	# Draw connections between nodes
	for node in adjacency_list:
		node_pos = scaled_node_positions[node]
		for neighbour in adjacency_list[node]:
			# Draw a unique Alaska <-> Kamchatka connection line
			if (node == 'Kamchatka') and (neighbour == 'Alaska'):
				end_pos = 1850, 70
				pygame.draw.line(screen, BLACK, (200, 70), end_pos, 2) # ( ! NEEDS SCALING ! )
				pygame.draw.line(screen, BLACK, end_pos, node_pos, 2)
			elif (node == 'Alaska') and (neighbour == 'Kamchatka'):
				pygame.draw.line(screen, BLACK, (200, 70), node_pos, 2)
			
			# Draw black line between node and neighbour of thickness 2
			else:
				neighbour_pos = scaled_node_positions[neighbour]
				# Set all lines in path red for moving to attack
				if (node == selected_node and neighbour == destination_node or neighbour == selected_node and node == destination_node) and attacking_node == True:
					# Get most efficient path & make ever line on path green
					pygame.draw.line(screen, RED, node_pos, neighbour_pos, 2)
				
				# Set all lines in path green for moving between territory
				elif (node == selected_node and neighbour == destination_node or neighbour == selected_node and node == destination_node) and attacking_node == False:
					pygame.draw.line(screen, GREEN, node_pos, neighbour_pos, 2)
				# Otherwise set line to black [default]
				else:
					pygame.draw.line(screen, BLACK, node_pos, neighbour_pos, 2)

def render_nodes(scale_x, scale_y, scaled_node_positions, screen, selected_node, destination_node):
	# Draw nodes
	node_radius = int(30 * min(scale_x, scale_y)) # Scale size of circle
	for node, pos in scaled_node_positions.items():
		# Colour nodes owned by player1 red
		if territory_owned[node][0] == player1:
			pygame.draw.circle(screen, RED, pos, node_radius)
		# Colour unowned nodes grey
		else:
			pygame.draw.circle(screen, GREY, pos, node_radius)

		# Selected node
		if node == selected_node:
				pygame.draw.circle(screen, BLACK, pos, node_radius - 5, 3)
		
		if node == destination_node:
				pygame.draw.circle(screen, BLACK, pos, node_radius + 5, 3)
		
		# Display territory text
		font = pygame.font.Font(None, int(24 * min(scale_x, scale_y))) # Scale font size
		text_surface = font.render(str(territory_owned[node][1]), True, BLACK)
		text_rect = text_surface.get_rect(center=pos)
		screen.blit(text_surface, text_rect)

def render_all(scaled_node_positions, screen, selected_node, destination_node, attacking_node, scale_x, scale_y):
	print("Rendering...")

	# Clear the screen
	screen.fill(WHITE)

	render_connections_between_nodes(scaled_node_positions, screen, selected_node, destination_node, attacking_node)
	render_nodes(scale_x, scale_y, scaled_node_positions, screen, selected_node, destination_node)
	
	# Update the display
	pygame.display.flip()