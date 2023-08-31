import copy

# Spot class to store coordinates, value and possible values (for empty spots) 
class Spot:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.possible = []

# process file and generate grid of spots
def get_grid(filename):
    all_grids = []
    
    with open(filename, "r") as grid_file:
        for line in grid_file:
            line = line.strip()
            grid = []
            for i in range(9):
                row = []
                for j in range(9):
                    newSpot = Spot(i, j, int(line[9*i+j]))
                    row.append(newSpot)
                grid.append(row)
            
            all_grids.append(grid)
    
    return all_grids

# function to print formatted grid
def print_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0:
            print(19*"-")
            
        for j, spot in enumerate(row):
            if j % 3 == 0:
                print("|", end="")
            else:
                print("!", end="")
            print(spot.val, end="")
        print("|")
            
    print(19*"-")
    return

# function to extract all possible values that can be placed at a certain spot in the grid
def get_possible(i, j, grid):
    possible = [True] * 10
    # check row
    for spot in grid[i]:
        possible[spot.val] = False
        
    # check col
    for row in range(9):
        possible[grid[row][j].val] = False
        
    # check box
    for row in range(i - i%3, i - i%3 + 3):
        for col in range(j - j%3, j - j%3 + 3):
            possible[grid[row][col].val] = False
    
    # check numbers from 1 to 9 to see if they are possible
    possible_nums = []
    for num in range(1, 10):
        if possible[num] == True:
            possible_nums.append(num)
    
    return possible_nums

def solve(grid):   
    # print_grid(grid)  # for debugging purposes
     
    # get box with minimum moves
    minMoves = float('inf')
    minSpot = None
    
    for row in grid:
        for spot in row:
            if spot.val != 0:  # skips filled spots
                continue
                
            if len(spot.possible) < minMoves:
                minMoves = len(spot.possible)
                minSpot = spot
    
    if minMoves == float('inf'):  # completed grid
        return grid
    elif minMoves == 0:  # invalid grid
        return None
    else:
        # recursive process
        for num in minSpot.possible:
            newGrid = copy.deepcopy(grid)  # deepcopy of grid to retain original state
            
            # update grid after filling num in spot
            newGrid[minSpot.i][minSpot.j].val = num
            newGrid[minSpot.i][minSpot.j].possible = []
            
            # row
            for j in range(9):
                if j == minSpot.j:
                    continue
                
                newGrid[minSpot.i][j].possible = get_possible(minSpot.i, j, newGrid)
                
            # col
            for i in range(9):
                if i == minSpot.i:
                    continue
                
                newGrid[i][minSpot.j].possible = get_possible(i, minSpot.j, newGrid)
            
            # box
            for i in range(minSpot.i - minSpot.i%3, minSpot.i - minSpot.i%3 + 3):
                for j in range(minSpot.j - minSpot.j%3, minSpot.j - minSpot.j%3 + 3):
                    if i == minSpot.i or j == minSpot.j:
                        continue
                    
                    newGrid[i][j].possible = get_possible(i, j, newGrid)
                    
            result = solve(newGrid)
            if result != None:
                return result
            
            del newGrid  # ensure unused space is removed
    
    return None
            
            

if __name__ == '__main__':
    # read from input file
    all_grids = get_grid("./grids/hardest.txt")
    print("Number of grids:", len(all_grids))
    
    # iterate for all grids
    for grid_num, grid in enumerate(all_grids, 1):
        print(30*"=")
        print(f"Grid {grid_num} (Before Solving):")
        print_grid(grid)
        
        # initialise possible values in empty spots
        for i in range(9):
            for j in range(9):
                if grid[i][j].val == 0:
                    grid[i][j].possible = get_possible(i, j, grid)
        
        print(f"Grid {grid_num} (After solving):")
        
        solved_grid = solve(grid)
        print_grid(solved_grid)
        
        print(30*"=")
    
    print("Completed.")