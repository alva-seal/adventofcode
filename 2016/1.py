import matplotlib.pyplot as plt

input = "R3, L2, L2, R4, L1, R2, R3, R4, L2, R4, L2, L5, L1, R5, R2, R2, L1, R4, R1, L5, L3, R4, R3, R1, L1, L5, L4, L2, R5, L3, L4, R3, R1, L3, R1, L3, R3, L4, R2, R5, L190, R2, L3, R47, R4, L3, R78, L1, R3, R190, R4, L3, R4, R2, R5, R3, R4, R3, L1, L4, R3, L4, R1, L4, L5, R3, L3, L4, R1, R2, L4, L3, R3, R3, L2, L5, R1, L4, L1, R5, L5, R1, R5, L4, R2, L2, R1, L5, L4, R4, R4, R3, R2, R3, L1, R4, R5, L2, L5, L4, L1, R4, L4, R4, L4, R1, R5, L1, R1, L5, R5, R1, R1, L3, L1, R4, L1, L4, L4, L3, R1, R4, R1, R1, R2, L5, L2, R4, L1, R3, L5, L2, R5, L4, R5, L5, R3, R4, L3, L3, L2, R2, L5, L5, R3, R4, R3, R4, R3, R1"
# input = "R2, L3"
# input = "R2, R2, R2"
# input = "R5, L5, R5, R3"
# input = "R8, R4, R4, R8"
inputlist = input.split(", ")

position = [0, 0]
positions = [[0,0]]
direction = 0
for movement in inputlist:
    rotation = movement[0]
    blocks = int(movement[1:])
    if rotation == "L":
        direction -= 1
    else:
        direction += 1
    direction = direction % 4
    print(direction)
    if (direction % 2) == 0:
        if direction < 2:
            position[0] += blocks
        else:
            position[0] -= blocks
    else:
        if direction < 2:
            position[1] += blocks
        else:
            position[1] -= blocks
    positions.append(position[:])

print(inputlist)
print(position)
print(positions)
print(abs(sum(position)))
x, y = zip(*positions)
plt.plot(x,y)
plt.show()
