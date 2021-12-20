#!/usr/bin/python

"""

--- Day 20: Trench Map ---

With the scanners fully deployed, you turn their attention to mapping the floor of the ocean trench.

When you get back the image from the scanners, it seems to just be random noise. Perhaps you can combine an image enhancement algorithm and the input image (your puzzle input) to clean it up a little.

For example:

..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###

The first section is the image enhancement algorithm. It is normally given on a single line, but it has been wrapped to multiple lines in this example for legibility. The second section is the input image, a two-dimensional grid of light pixels (#) and dark pixels (.).

The image enhancement algorithm describes how to enhance an image by simultaneously converting all pixels in the input image into an output image. Each pixel of the output image is determined by looking at a 3x3 square of pixels centered on the corresponding input image pixel. So, to determine the value of the pixel at (5,10) in the output image, nine pixels from the input image need to be considered: (4,9), (4,10), (4,11), (5,9), (5,10), (5,11), (6,9), (6,10), and (6,11). These nine input pixels are combined into a single binary number that is used as an index in the image enhancement algorithm string.

For example, to determine the output pixel that corresponds to the very middle pixel of the input image, the nine pixels marked by [...] would need to be considered:

# . . # .
#[. . .].
#[# . .]#
.[. # .].
. . # # #

Starting from the top-left and reading across each row, these pixels are ..., then #.., then .#.; combining these forms ...#...#.. By turning dark pixels (.) into 0 and light pixels (#) into 1, the binary number 000100010 can be formed, which is 34 in decimal.

The image enhancement algorithm string is exactly 512 characters long, enough to match every possible 9-bit binary number. The first few characters of the string (numbered starting from zero) are as follows:

0         10        20        30  34    40        50        60        70
|         |         |         |   |     |         |         |         |
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##

In the middle of this first group of characters, the character at index 34 can be found: #. So, the output pixel in the center of the output image should be #, a light pixel.

This process can then be repeated to calculate every pixel of the output image.

Through advances in imaging technology, the images being operated on here are infinite in size. Every pixel of the infinite output image needs to be calculated exactly based on the relevant pixels of the input image. The small input image you have is only a small region of the actual infinite input image; the rest of the input image consists of dark pixels (.). For the purposes of the example, to save on space, only a portion of the infinite-sized input and output images will be shown.

The starting input image, therefore, looks something like this, with more dark pixels (.) extending forever in every direction not shown here:

...............
...............
...............
...............
...............
.....#..#......
.....#.........
.....##..#.....
.......#.......
.......###.....
...............
...............
...............
...............
...............

By applying the image enhancement algorithm to every pixel simultaneously, the following output image can be obtained:

...............
...............
...............
...............
.....##.##.....
....#..#.#.....
....##.#..#....
....####..#....
.....#..##.....
......##..#....
.......#.#.....
...............
...............
...............
...............

Through further advances in imaging technology, the above output image can also be used as an input image! This allows it to be enhanced a second time:

...............
...............
...............
..........#....
....#..#.#.....
...#.#...###...
...#...##.#....
...#.....#.#...
....#.#####....
.....#.#####...
......##.##....
.......###.....
...............
...............
...............

Truly incredible - now the small details are really starting to come through. After enhancing the original input image twice, 35 pixels are lit.

Start with the original input image and apply the image enhancement algorithm twice, being careful to account for the infinite size of the images. How many pixels are lit in the resulting image?

Your puzzle answer was 5361.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You still can't quite make out the details in the image. Maybe you just didn't enhance it enough.

If you enhance the starting input image in the above example a total of 50 times, 3351 pixels are lit in the final output image.

Start again with the original input image and apply the image enhancement algorithm 50 times. How many pixels are lit in the resulting image?

Your puzzle answer was 16826.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

if __name__ == "__main__":

	lit = set()

	x_min = None
	x_max = None
	y_min = None
	y_max = None
	
	def find_bounds():
		global x_min,x_max,y_min,y_max
		x_min = float('inf')
		x_max = -float('inf')
		y_min = float('inf')
		y_max = -float('inf')
		for x,y in lit:
			x_min = min(x_min,x)
			x_max = max(x_max,x)
			y_min = min(y_min,y)
			y_max = max(y_max,y)
		
	def resolve_px(x,y,t):
		out = ''
		for j in (-1,0,1):
			for i in (-1,0,1):
				if (x+i,y+j) in lit:
					out += '1'
				elif (x+i < x_min or x+i > x_max or y+j < y_min or y+j > y_max) and t%2 == 1:
					out += '1'
				else:
					out += '0'
		return int(out,2)

	# Part 1 Solution
	
	with open("day20_input","r") as infile:
		kernel = infile.readline().strip()
		throw  = infile.readline()
		y = 0
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == "#":
					lit.add((x,y))
			y += 1
	
	find_bounds()
	orig_x_min = x_min
	orig_x_max = x_max
	orig_y_min = y_min
	orig_y_max = y_max

	for _ in range(2):
		next_lit = set()
		find_bounds()
		for y in range(y_min-4,y_max+4):
			for x in range(x_min-4,x_max+4):
				if kernel[resolve_px(x,y,_)] == "#":
					next_lit.add((x,y))
		lit = next_lit
	lit = { x for x in lit if x[0] >= orig_x_min-2 and x[0] <= orig_x_max +2 }
	lit = { x for x in lit if x[1] >= orig_y_min-2 and x[1] <= orig_y_max +2 }
	print(len(lit))

	# Part 2 Solution

	lit = set()
	with open("day20_input","r") as infile:
		kernel = infile.readline().strip()
		throw  = infile.readline()
		y = 0
		for line in infile.readlines():
			for x,char in enumerate(line.strip()):
				if char == "#":
					lit.add((x,y))
			y += 1
	
	find_bounds()
	orig_x_min = x_min
	orig_x_max = x_max
	orig_y_min = y_min
	orig_y_max = y_max

	for _ in range(50):
		next_lit = set()
		find_bounds()
		for y in range(y_min-3,y_max+3):
			for x in range(x_min-3,x_max+3):
				if kernel[resolve_px(x,y,_)] == "#":
					next_lit.add((x,y))
		lit = next_lit
	lit = { x for x in lit if x[0] >= orig_x_min-50 and x[0] <= orig_x_max +50 }
	lit = { x for x in lit if x[1] >= orig_y_min-50 and x[1] <= orig_y_max +50 }
	print(len(lit))

