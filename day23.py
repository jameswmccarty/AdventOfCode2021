#!/usr/bin/python

"""

--- Day 23: Amphipod ---

A group of amphipods notice your fancy submarine and flag you down. "With such an impressive shell," one amphipod says, "surely you can help us with a question that has stumped our best scientists."

They go on to explain that a group of timid, stubborn amphipods live in a nearby burrow. Four types of amphipods live there: Amber (A), Bronze (B), Copper (C), and Desert (D). They live in a burrow that consists of a hallway and four side rooms. The side rooms are initially full of amphipods, and the hallway is initially empty.

They give you a diagram of the situation (your puzzle input), including locations of each amphipod (A, B, C, or D, each of which is occupying an otherwise open space), walls (#), and open space (.).

For example:

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

The amphipods would like a method to organize every amphipod into side rooms so that each side room contains one type of amphipod and the types are sorted A-D going left to right, like this:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

Amphipods can move up, down, left, or right so long as they are moving into an unoccupied open space. Each type of amphipod requires a different amount of energy to move one step: Amber amphipods require 1 energy per step, Bronze amphipods require 10 energy, Copper amphipods require 100, and Desert ones require 1000. The amphipods would like you to find a way to organize the amphipods that requires the least total energy.

However, because they are timid and stubborn, the amphipods have some extra rules:

    Amphipods will never stop on the space immediately outside any room. They can move into that space so long as they immediately continue moving. (Specifically, this refers to the four open spaces in the hallway that are directly above an amphipod starting position.)
    Amphipods will never move from the hallway into a room unless that room is their destination room and that room contains no amphipods which do not also have that room as their own destination. If an amphipod's starting room is not its destination room, it can stay in that room until it leaves the room. (For example, an Amber amphipod will not move from the hallway into the right three rooms, and will only move into the leftmost room if that room is empty or if it only contains other Amber amphipods.)
    Once an amphipod stops moving in the hallway, it will stay in that spot until it can move into a room. (That is, once any amphipod starts moving, any other amphipods currently in the hallway are locked in place and will not move again until they can move fully into a room.)

In the above example, the amphipods can be organized using a minimum of 12521 energy. One way to do this is shown below.

Starting configuration:

#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########

One Bronze amphipod moves into the hallway, taking 4 steps and using 40 energy:

#############
#...B.......#
###B#C#.#D###
  #A#D#C#A#
  #########

The only Copper amphipod not in its side room moves there, taking 4 steps and using 400 energy:

#############
#...B.......#
###B#.#C#D###
  #A#D#C#A#
  #########

A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy, and then the Bronze amphipod takes its place, taking 3 steps and using 30 energy:

#############
#.....D.....#
###B#.#C#D###
  #A#B#C#A#
  #########

The leftmost Bronze amphipod moves to its room using 40 energy:

#############
#.....D.....#
###.#B#C#D###
  #A#B#C#A#
  #########

Both amphipods in the rightmost room move into the hallway, using 2003 energy in total:

#############
#.....D.D.A.#
###.#B#C#.###
  #A#B#C#.#
  #########

Both Desert amphipods move into the rightmost room using 7000 energy:

#############
#.........A.#
###.#B#C#D###
  #A#B#C#D#
  #########

Finally, the last Amber amphipod moves into its room, using 8 energy:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########

What is the least energy required to organize the amphipods?

What is the least energy required to organize the amphipods?

Your puzzle answer was 14350.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

As you prepare to give the amphipods your solution, you notice that the diagram they handed you was actually folded up. As you unfold it, you discover an extra part of the diagram.

Between the first and second lines of text that contain amphipod starting positions, insert the following lines:

  #D#C#B#A#
  #D#B#A#C#

So, the above example now becomes:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

The amphipods still want to be organized into rooms similar to before:

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

In this updated example, the least energy required to organize these amphipods is 44169:

#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#..........D#
###B#C#B#.###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A.........D#
###B#C#B#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A........BD#
###B#C#.#.###
  #D#C#B#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#A......B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#A#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#C#.#.###
  #D#C#.#.#
  #D#B#.#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#C#.#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA.....B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#D#C#A#
  #########

#############
#AA...B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#D#C#A#
  #########

#############
#AA.D.B.B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#.#C#A#
  #########

#############
#AA.D...B.BD#
###B#.#.#.###
  #D#.#C#.#
  #D#.#C#C#
  #A#B#C#A#
  #########

#############
#AA.D.....BD#
###B#.#.#.###
  #D#.#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#.#.###
  #D#B#C#.#
  #D#B#C#C#
  #A#B#C#A#
  #########

#############
#AA.D......D#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#A#
  #########

#############
#AA.D.....AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#.#
  #########

#############
#AA.......AD#
###B#.#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #D#B#C#.#
  #D#B#C#.#
  #A#B#C#D#
  #########

#############
#AA.......AD#
###.#B#C#.###
  #.#B#C#.#
  #D#B#C#D#
  #A#B#C#D#
  #########

#############
#AA.D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #.#B#C#D#
  #A#B#C#D#
  #########

#############
#A..D.....AD#
###.#B#C#.###
  #.#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...D.....AD#
###.#B#C#.###
  #A#B#C#.#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#.........AD#
###.#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#..........D#
###A#B#C#.###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########

Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?

Your puzzle answer was 49742.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

if __name__ == "__main__":

	import heapq
	from collections import deque
	
	# index map
	
	"""
	  0123456789012
	0 #############
	1 #...........#
	2 ###A#B#C#D###
	3   #A#B#C#D#
	4   #########
	"""

	walls = set()

	hall_spots = [(1,1),(2,1),(4,1),(6,1),(8,1),(10,1),(11,1)]

	stack_depth = 2

	goals_idx = {'A' : 3,
		 'B' : 5,
		 'C' : 7,
		 'D' : 9}

	goals_y_idx = {'A':0,'B':1,'C':2,'D':3}

	costs = {'A' : 1,
		 'B' : 10,
		 'C' : 100,
		 'D' : 1000}

	def set_goals(posits):
		goals = [2,2,2,2]
		for letter in ['A','B','C','D']:
			for j in range(1+stack_depth,1,-1):
				if (letter,goals_idx[letter],j) not in posits:
					goals[goals_y_idx[letter]] = j
					break
		return goals

	def letter_sat(char,occupied):
		fills = 0
		for y in range(2,2+stack_depth):
			if (char,goals_idx[char],y) in occupied:
				fills += 1
		if fills == stack_depth:
			return True
		return False

	def hall_blocked(char,occupied):
		for i,x,y in occupied:
			if i != char and x == goals_idx[char]:
				return True
		return False

	def spot_reachable(char,current_pos,goal_pos,occupied):
		if goal_pos in occupied and current_pos != goal_pos:
			return (False,float('inf'))
		if goal_pos == current_pos:
			return (True,0)
		seen = set()
		seen.add(current_pos)
		q = [(0,current_pos)]
		while len(q) > 0:
			steps,pos = q.pop(0)
			if pos == goal_pos:
				return (True,steps)
			x,y = pos
			for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
				nx,ny = x+dx,y+dy
				if (nx,ny) not in walls and (nx,ny) not in occupied and (nx,ny) not in seen:
					q.append((steps+1,(nx,ny)))
					seen.add((nx,ny))
		return (False,float('inf'))
	
	def goal_reachable(char,current_pos,occupied,goals):
		# is hallway blocked by another type of char?
		if hall_blocked(char,occupied):
			return (False,float('inf'))
		x,y = current_pos
		if x == goals_idx[char] and y >= goals[goals_y_idx[char]]:
			return (False,float('inf'))
		blocked_set = { (x,y) for i,x,y in occupied }
		seen = set()
		seen.add(current_pos)
		q = deque()
		q.append((current_pos,0))
		while len(q) > 0:
			pos,steps = q.popleft()
			x,y = pos
			# reached a goal, already verified hall not blocked
			if x == goals_idx[char] and y == goals[goals_y_idx[char]]:
				return(True,steps)
			else:
				for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
					nx,ny = x+dx,y+dy
					if (nx,ny) not in walls and (nx,ny) not in blocked_set and (nx,ny) not in seen:
						q.append(((nx,ny),steps+1))
						seen.add((nx,ny))
		return (False,float('inf'))
	
	def heap_search(posits,goals):

		seen_configs = { hash(frozenset(posits)) }
		q = []
		heapq.heapify(q)
		heapq.heappush(q,(0,goals[:],posits[:]))
		while len(q) > 0:
			cost, goals, elements = heapq.heappop(q)
			#print(cost,elements)
			all_sat = True
			for letter in ['A','B','C','D']:
				if not letter_sat(letter,elements):
					all_sat = False
			if all_sat:
				return cost
			for element in elements:
				char,x,y = element
				# don't continue if this letter is solved or if this
				# current letter is in the goal position
				if not letter_sat(char,elements):
					rest_elements = [ j for j in elements if j != element ]
					success,steps = goal_reachable(char,(x,y),rest_elements,goals)
					# can we move this letter to a goal position?
					if success:
						gy = goals[goals_y_idx[char]]
						new_goals = goals[:]
						new_goals[goals_y_idx[char]] = max(2,goals[goals_y_idx[char]]-1)
						config = { p for p in rest_elements }
						config.add((char,goals_idx[char],gy))
						heapq.heappush(q,(cost+costs[char]*steps,new_goals,rest_elements+[(char,goals_idx[char],gy)]))
						seen_configs.add(hash(frozenset(config)))
					elif y != 1:
						blocked_set = { (p,q) for i,p,q in elements }
						for spot in hall_spots:
							reachable,steps = spot_reachable(char,(x,y),spot,blocked_set)
							if reachable:
								config = { p for p in rest_elements }
								nx,ny = spot
								config.add((char,nx,ny))
								if hash(frozenset(config)) not in seen_configs:
									heapq.heappush(q,(cost+costs[char]*steps,goals,rest_elements+[(char,nx,ny)]))
									seen_configs.add(hash(frozenset(config)))
		return float('inf')

	# Part 1 Solution

	posits = []

	with open("day23_input","r") as infile:
		y = 0
		for line in infile.readlines():
			for idx,char in enumerate(line.rstrip()):
				if char == '#':
					walls.add((idx,y))
				elif char in ['A','B','C','D']:
					posits.append((char,idx,y))
			y += 1
	goals = set_goals(posits)
	print(heap_search(posits,goals))

	# Part 2 Solution

	posits = []
	walls = set()
	add1='  #D#C#B#A#'
	add2='  #D#B#A#C#'
	lines = []
	with open("day23_input","r") as infile:
		for line in infile.readlines():
			lines.append(line.rstrip())
	lines.insert(3,add1)
	lines.insert(4,add2)
	stack_depth = 4
	y = 0
	for line in lines:
		for idx,char in enumerate(line.rstrip()):
			if char == '#':
				walls.add((idx,y))
			elif char in ['A','B','C','D']:
				posits.append((char,idx,y))
		y += 1
	goals = set_goals(posits)
	print(heap_search(posits,goals))

