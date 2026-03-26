class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)
        
        def can_partition(g: List[List[int]], is_horizontal: bool) -> bool:
            if len(g) < 2:
                return False
            rows = len(g)
            cols = len(g[0])
            
            top = 0
            seen = set()             
            for i in range(rows - 1):  
                for val in g[i]:
                    top += val
                    seen.add(val)
                
                bot = total - top
                diff = top - bot
                
                if diff == 0:
                    return True
                
                # Determine which side is larger
                if diff > 0:
                    # Try remove from top (larger)
                    larger_rows = i + 1
                    larger_cols = cols
                    if diff in seen:
                        # Safe to remove if section is thick enough or from end
                        if larger_rows > 1 and larger_cols > 1:
                            return True
                        # For thin sections (1 row or 1 col), only allow end cells
                        # But since we don't know *which* cell, we allow only if diff matches first/last in the strip
                        # For simplicity and speed: for 1-row top we allow any (but in practice we check ends below)
                        if larger_rows == 1 or larger_cols == 1:
                            # Check if we can remove an end cell
                            if i == 0 and diff in {g[0][0], g[0][-1]}:   # top is single row
                                return True
                            # For multi-row 1-col, ends are first and last row
                            if larger_cols == 1 and diff in {g[0][0], g[i][0]}:
                                return True
                else:
                    # Try remove from bottom (larger)
                    bot_start_row = i + 1
                    larger_rows = rows - bot_start_row
                    larger_cols = cols
                    
                    if -diff in g[i + 1]:  # at least check the boundary row
                        if larger_rows > 1 and larger_cols > 1:
                            return True
                        # Thin bottom section
                        if larger_rows == 1:  # bottom is single row
                            if -diff in {g[i+1][0], g[i+1][-1]}:
                                return True
                        elif larger_cols == 1:  # bottom is single column
                            if -diff in {g[bot_start_row][0], g[-1][0]}:
                                return True
            
            return False
        
        # 1. Horizontal cuts
        if can_partition(grid, True):
            return True
        if can_partition(grid[::-1], True):   # flip vertically
            return True
        
        # 2. Vertical cuts → transpose
        transposed = [list(col) for col in zip(*grid)]
        if can_partition(transposed, False):
            return True
        if can_partition(transposed[::-1], False):
            return True
        
        return False