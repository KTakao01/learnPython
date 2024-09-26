# Create 2 new lists height and weight
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)
print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height**2

# Print the result
print(bmi)  # [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]

# For a boolean response
print(bmi > 23)  # [ True  True  True  True  True  True]
print(bmi > 24)  # [False  True  True  True False  True]

# Print only those observations above 23

bmi_view = bmi[bmi > 24]
print(bmi_view)  # [27.88755755 28.75558507 25.48723993 25.84368152]
print(bmi)  # [23.34925219 27.88755755 28.75558507 25.48723993 23.87257618 25.84368152]

# 値を変更
bmi_view = bmi[bmi > 24] = 24.0
print(bmi_view)  # 24.0
print(bmi)  # [23.34925219 24.         24.         24.         23.87257618 24.        ]

# 値が変更されない
# 　インデキシング（ブールインデキシング）
bmi_view2 = bmi[bmi == 24]
print(bmi_view2)  # [24. 24. 24. 24.]
bmi_view2[:] = 29.0
print(bmi_view2)  # [29. 29. 29. 29.]
print(bmi)  # [23.34925219 24.         24.         24.         23.87257618 24.        ]
