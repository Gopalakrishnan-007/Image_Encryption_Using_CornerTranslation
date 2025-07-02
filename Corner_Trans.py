import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img




def logistic_key(x, r, size):
    """
    Generate a list of pseudo-random keys using the logistic equation.
    """
    key = []
    for i in range(size):   
        x = r * x * (1 - x)  # The logistic equation
        key.append(int((x * pow(10, 16)) % 256))  # Map to 0-255
    return key

# Accepting an image
path = str(input('Enter the path of the image:\n'))
image = img.imread(path)

# Displaying the original image
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Generating dimensions of the image
height, width = image.shape[0], image.shape[1]
print(f"Image Dimensions: Height = {height}, Width = {width}")

# Generating keys
# Call logistic_key and provide r values such that the keys are pseudo-random
# Generate a key for every pixel of the image
X = logistic_key(0.01, 3.95, height * width)
Y = logistic_key(0.02, 3.99, height * width)

# Encryption using XOR
z = 0
# Initialize the encrypted image
encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# Substitute all the pixels in the original image
for i in range(height):
    for j in range(width):
        # XOR operation between image pixels and keys
        encryptedImage[i, j] = image[i, j].astype(int) ^ (X[z] * Y[z])
        z += 1



'''
1 2  3  4
5 6  7  8
9 10 11 12
13 14 15 16
'''
'''
1 13 16 4 5 14 12 3 9 15 8 2 6 10 11 7
'''

def transpose_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    # Number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize an empty transposed matrix with dimensions cols x rows
    transposed = [[0] * rows for _ in range(cols)]

    # Populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed





def spiral_layers(matrix):

    rows, cols = len(matrix), len(matrix[0])
    layers = []
    left, right, top, bottom = 0, cols - 1, 0, rows - 1

    while left <= right and top <= bottom:
        current_layer = []

        # Traverse down along the left column
        for i in range(top, bottom + 1):
            current_layer.append(matrix[i][left])
        left += 1

        # Traverse right along the bottom row
        for i in range(left, right + 1):
            current_layer.append(matrix[bottom][i])
        bottom -= 1

        # Traverse up along the right column (if within bounds)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                current_layer.append(matrix[i][right])
            right -= 1

        # Traverse left along the top row (if within bounds)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                current_layer.append(matrix[top][i])
            top += 1

        # Add the current layer to the layers list
        layers.append(current_layer)

    return layers



def reconstruct_matrix(layers, rows, cols):
    
    # Initialize an empty matrix
    matrix = [[0] * cols for _ in range(rows)]

    left, right, top, bottom = 0, cols - 1, 0, rows - 1

    layer_index = 0
    while left <= right and top <= bottom:
        current_layer = layers[layer_index]
        index = 0

        # Fill down the left column
        for i in range(top, bottom + 1):
            matrix[i][left] = current_layer[index]
            index += 1
        left += 1

        # Fill right along the bottom row
        for i in range(left, right + 1):
            matrix[bottom][i] = current_layer[index]
            index += 1
        bottom -= 1

        # Fill up the right column (if within bounds)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][right] = current_layer[index]
                index += 1
            right -= 1

        # Fill left along the top row (if within bounds)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[top][i] = current_layer[index]
                index += 1
            top += 1

        layer_index += 1

    return matrix












def find(arr,k,ss):
  anss=[]
  size=len(arr[k])
  for i in range(ss):
    j=0
    for _ in range(4):
      anss.append(arr[k][j])
      j = (j+ss)%size
    arr[k] = arr[k][size-1:]+arr[k][:size-1]
  if anss:
      ans.append(anss)













# Example usage:
'''
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13 ,14, 15],
    [16, 17, 18, 19, 20],
    [21, 22 , 23,24,25]
]
'''
#1 21 25 5 6 22 20 4 11 23 15 3 16 24 10 2

'''
matrix = [
    [1, 2, 3, 4],
    [5,6, 7, 8],
    [9,10,11, 12],
    [13, 14, 15, 16],
]

'''


'''
matrix = [
    [1, 2, 3, 4, 5,6],
    [7, 8, 9, 10,11,12],
    [13, 14, 15 ,16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26 , 27,28,29, 30],
    [31,32,33,34,35,36]
]
'''


matrix = encryptedImage

arr = spiral_layers(matrix)
#print(arr)
n = len(matrix)-1
ans = []
for i in range(len(arr)):
  find(arr,i,n)
  n-=2
if len(arr[-1]) == 1:
  ans.append(arr[-1])





def convert_to_2d(array):
    n = int(len(array) ** 0.5)  # Calculate the size of the 2D array (n x n)
    if n * n != len(array):
        raise ValueError("The input array does not have n^2 elements.")
    return [array[i * n:(i + 1) * n] for i in range(n)]

dec = []

def decrypt_to_corner(array,n,i):
  #array is 1D array input
  temp = []
  for k in range(4*n-4):
    temp.append(array[k])
  dec.append(temp)

def convert_to_1d(matrix):
    return [element for row in matrix for element in row]



array = convert_to_1d(ans)
encr = convert_to_2d(array)

# Displaying the encrypted image
plt.imshow(encr)
plt.title("Encrypted Image")
plt.axis("off")
plt.show()


array = convert_to_1d(encr)




n = height
i=0
while n > 1:
  decrypt_to_corner(array,n,i)
  i+=1
  array = array[4*n-4:]
  n-=2
if len(array) == 1:
  dec.append(array)












ans=dec











Final_decrypted_matrix = []
def decrypt_corner(ans,n,i):
  a=[]
  b=[]
  c=[]
  d=[]
  arr_num = 0
  temp = ans[i]
  for i in temp:
    if arr_num == 0:
      a = [i]+a
      arr_num = (arr_num+1)%4
    elif arr_num == 1:
      b = [i]+b
      arr_num = (arr_num+1)%4
    elif arr_num == 2:
      c = [i]+c
      arr_num = (arr_num+1)%4
    elif arr_num == 3:
      d = [i]+d
      arr_num = (arr_num+1)%4
  res = a+b+c+d
  res = res[n-2:]+res[:n-2]
  Final_decrypted_matrix.append(res)
  
n = len(matrix)
for i in range(len(ans)):
  decrypt_corner(ans,n,i)
  n-=2

if(len(ans[-1]) == 1):
  Final_decrypted_matrix.append(ans[-1])









reconstructed_matrix = reconstruct_matrix(Final_decrypted_matrix, len(matrix), len(matrix[0]))
res = []
for i in range(len(matrix)):
    res.append(reconstructed_matrix[i])


encryptedImage = np.array(res, dtype=np.uint8)



# Decryption using XOR
z = 0
# Initialize the decrypted image
decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# Substitute all the pixels in the encrypted image
for i in range(height):
    for j in range(width):
        # XOR operation between encrypted image pixels and keys
        decryptedImage[i, j] = encryptedImage[i, j].astype(int) ^ (X[z] * Y[z])
        z += 1

# Displaying the decrypted image
plt.imshow(decryptedImage)
plt.title("Decrypted Image")
plt.axis("off")
plt.show()

# Verifying the decryption
if np.array_equal(image, decryptedImage):
    print("Decryption successful! The decrypted image matches the original.")
else:
    print("Decryption failed! The decrypted image does not match the original.")
