#!/usr/bin/python

"""

--- Day 9: Smoke Basin ---

These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

Your puzzle answer was 504.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

Your puzzle answer was 1558722.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

if __name__ == "__main__":

	# Part 1 Solution

	adj_points = [(1,0),(-1,0),(0,1),(0,-1)]
	map_points = dict()
	low_points = []
	with open("day09_input","r") as infile:
		cavemap = infile.read().strip()
	cavemap = cavemap.split('\n')
	for j,line in enumerate(cavemap):
		for i,point in enumerate(line):
			map_points[(i,j)] = int(point)
	low_total = 0
	for a,b in map_points:
		lowest = True
		for x,y in adj_points:
			if (a+x,b+y) in map_points and map_points[(a+x,b+y)] <= map_points[(a,b)]:
				lowest = False
		if lowest:
			low_total += (map_points[(a,b)]+1)
			low_points.append((a,b))
	print(low_total)


	# Part 2 Solution
	basins = []
	for x,y in low_points:
		basin = set()
		basin.add((x,y))
		q = [(x,y)]
		while len(q) > 0:
			x,y = q.pop(0)
			for dx,dy in adj_points:
				if (x+dx,y+dy) not in basin and (x+dx,y+dy) in map_points and map_points[(x+dx,y+dy)] != 9:
					q.append((x+dx,y+dy))
					basin.add((x+dx,y+dy))
		basins.append(basin)
	for j,b1 in enumerate(basins):
		for i in range(j+1,len(basins)):
			if len(b1.intersection(basins[i])) > 0:
				b1 += basins[i]
				basin[i] = set()
	sizes = sorted([ len(x) for x in basins if len(x) > 0 ], reverse = True)
	print(sizes[0]*sizes[1]*sizes[2])

		
	
