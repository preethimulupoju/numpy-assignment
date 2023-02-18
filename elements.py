n_array = np.array([1,2,0,0,4,0])

print("Original array:")
print(n_array)

# np.nonzero()
print("\nIndices of null elements:")

res = np.nonzero(n_array == 0)
print(res)
