Version 1: Initial brainstorming + Strategy Research; placed all ships and found out about probability density methods
Version 2: After place_ships function was completed, I settled on using th eprobability density in order to determine which squares to
"hunt". This meant that I'd go through windows of five in all cardinal directions and add 1 for squares that could potentially hold
an opponent's battleship. This meant learning a bit more about for loops like how to iterate through set windows in 2D lists.

Version 3: Worked on "hunt" function, which is the probability mapping. This adds 1 for each slice of 5 and iterates through, adding 1 to each potential location, and ignores / doesn't add to those with adjacent squares that are misses (currently -1; will have to change later). Implementing the diagonals were a little tough, but I figured it out after looking it up online. I also had to find a good way to verify if there was a number in the given square. I found the solution to be the function "isinstance(val, form)"

Version 4: Worked on "target function". If there has been a hit square, this function takes the adjacent squares and adds a high number like 1000 so that it overshadows all other squares, placing immediate priority on them. However, it still ignores values that are -1, or "H" as to not run into repeated errors. Due to there being 8 directions that the next hit could potential be in, I realized that this code could take many more tries to hit the ship than a traditional grid where one may place ships vertically or horizontally. Though, this is also potentially overriden by the number of squares the ship cover (25), which is significantly more board space occupied. This function took some new logic and was slightly more difficult to implement.

Version 5: Make moves function created, combining the hunt and target functions. However, because of inefficient strategy (where it adds 1000 to all 8 directions) instead of going in one direction once finding a hit, it makes the code run longer than it's supposed to, leading to games lasting around roughly 75 moves.

Version 6: FINAL
Due to the mentioned issue in Version 5, where the target function added 1000 to all 8 moves, the code was taking unnecessarily long to function due to it attempting to shoot in all eight cardinal directions, even if unnecessary (e.g. 2 adjacent already found). When attempting to fix this issue, I noticed that maintaining two systems created several compounding problems:

- The initial hunt() function discarded any 5-cell window containing "H" (if grid[row][column] == "H": return). This meant that once the board used hunt, it treated damaged ships as walls rather than the remaining locations of the ship
- In a two-function system, deciding when to switch from targeting back to hunting is not the best way to go about things. For example, if a ship is partially destroyed, or if two ships touch, target() either over-prioritizes unrelated adjacent cells or reverts back to using hunt() before the ship is sunk.
- Lastly, the biggest thing was that I realized both functinos are essentially trying to answer the same quetison: "Given the misses and hits observed so far, which squares are part of the greatest number of remaining valid ship placements?"

So, instead of managing between a target and a hunt state, I asked AI, which told me that a true probability density map would handle both at once. If a 5-cell window contains 0 hits, it adds 1 just like the old hunting function. If a window passes through 1, 2, or 3 existing hits without crossing into a miss, it adds exponentially higher weights such that the end of the line is given a higher priority than the others, limiting the wandering. This fixes target mode without needing two separate functions

"""
