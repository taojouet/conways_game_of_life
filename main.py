import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute 3x3 sum
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)
            # Apply Conway's rules
            if grid[i, j] == ON:  # Cell currently alive
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:  # Cell currently dead
                if total == 3:
                    newGrid[i, j] = ON
    # Update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Parameters
ON = 255  # Alive cell
OFF = 0  # Dead cell
vals = [ON, OFF]

N = 100
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='gray')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames=10, save_count=50)

plt.show()
