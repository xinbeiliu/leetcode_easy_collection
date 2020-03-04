# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to
# modify the input 2D matrix directly. DO NOT allocate another 2D
# matrix and do the rotation.

# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

def rotate_img(matrix):
  n = len(matrix[0])
  # transpose matrix
  for i in range(n):
      for j in range(i, n):
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

      # reverse each row
  for i in range(n):
      matrix[i].reverse()

  return matrix

print(rotate_img([[1,2,3],[4,5,6],[7,8,9]]))
# return [[7,4,1],[8,5,2],[9,6,3]]

