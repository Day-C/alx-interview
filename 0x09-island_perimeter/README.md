This project is aimed ad calculating the perimeter of an island represened by grids.
Land is represented by 1 and water by 0
To solve this we need to:
-loop through the list of list and each time we find a representation of land we look around it and calculate the representations of water adjecent to it(next to it).


Q1:
Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
