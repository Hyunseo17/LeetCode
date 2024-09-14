def blur_image(image, radius):
    # Dimensions of the image
    m, n = len(image), len(image[0])
    
    # Initialize the result matrix with the same dimensions as the input image
    result = [[0] * n for _ in range(m)]
    
    # Function to calculate the mean of neighbors within the radius
    def calculate_mean(i, j):
        total_sum = 0
        count = 0
        
        # Iterate through the potential neighbors within the radius
        for di in range(-radius, radius + 1):
            for dj in range(-radius, radius + 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    total_sum += image[ni][nj]
                    count += 1
        
        return total_sum // count
    
    # Apply blur effect to each pixel
    for i in range(m):
        for j in range(n):
            mean_neighbors = calculate_mean(i, j)
            result[i][j] = (image[i][j] + mean_neighbors) // 2
    
    return result

# Example Usage
image = [
  [9, 6],
  [3, 0]
]
radius = 1
print(blur_image(image, radius))

"""
You are given a two-dimensional matrix of integers image representing a black and white image, with image[i][j] containing an integer from 0 to 255 to represent the intensity of a pixel at coordinate (i, j). You are also given a non-negative integer parameter radius. Your task is to apply a blur effect to this image.

To apply a blur effect to the image, replace the intensity of each pixel (i, j) with the average value of its original intensity image[i][j] and the mean intensity of its neighboring pixels (defined as neighbors(i, j)). Pixel (k, l) is included in neighbors(i, j) if it satisfies the conditions abs(i - k) <= radius and abs(j - l) <= radius.

Expand to see the example pictures.
The neighbors of pixel at coordinate (2, 2) for radius == 1


The neighbors of pixel at coordinate (2, 2) for radius == 2


The mean intensity is defined as mean(values) = sum(values) // values.length where // is an integer division operator.
The integer division operator // is equivalent to taking an integer part of a real division: a // b = int(a / b).

So, the formula for replacing the intensity of each pixel is:

updated_intensity[i][j] = (intensity[i][j] + mean(neighbors(i, j))) // 2
Please note that some of the 8 possible neighbors might be missing, and the mean function should only take existing neighbors into account. If a pixel doesn't have any neighbors, its intensity should not change after blurring.

Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(image.length2 · image[0].length2) will fit within the execution time limit.

Example

For

image = [
  [9, 6],
  [3, 0]
]
and radius = 1, the output should be

solution(image, radius) = [
  [6, 5],
  [4, 3]
]
Explanation:

All pixels in the original image have 3 neighbors.
image[0][0] = 9, and its neighbors are [6, 3, 0] with a mean of (6 + 3 + 0) // 3 = 3. So, it should be updated to mean(9, 3) = (9 + 3) // 2 = 6.
image[0][1] = 6, and its neighbors are [9, 3, 0] with a mean of 12 // 3 = 4. So, it should be updated to mean(6, 4) = 10 // 2 = 5.
image[1][0] = 3, and its neighbors are [9, 6, 0] with a mean of 5. So, it should be updated to mean(3, 5) = 4.
image[1][1] = 0, and its neighbors are [9, 6, 3] with a mean of 6. So, it should be updated to mean(0, 6) = 3.
For

image = [
  [0, 0, 0],
  [0, 255, 0],
  [0, 0, 0]
]
and radius = 2, the output should be

solution(image, radius) = [
  [15, 15, 15],
  [15, 127, 15],
  [15, 15, 15]
]
Explanation:

radius is equal to 2, so, all the pixels in this example are the neighbors of each other.
For the central pixel image[1][1] = 255, there are 8 neighbors [0, 0, 0, 0, 0, 0, 0, 0] with a mean of 0 // 8 = 0. So, it should be updated to mean(255, 0) = 255 // 2 = 127.
For all 8 border pixels, there are 8 neighbors with a mean of 255 // 8 = 255 // 8 = 31. So, they should be updated to mean(0, 31) = 31 // 2 = int(15.5) = 15.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer image

A matrix of integers representing the pixels of an image to be blurred.

Guaranteed constraints:
1 ≤ image.length ≤ 50,
1 ≤ image[i].length ≤ 50,
0 ≤ image[i][j] ≤ 255.

[input] integer radius

A number representing the distance from a pixel coordinate, which defines the coordinates that are considered neighbors.

Guaranteed constraints:
1 ≤ radius ≤ 5.

[output] array.array.integer

A matrix of integers representing the pixels of a blurred image.
"""