# 3) Slice list into 3 equal chunks and reverse each chunk.

# Given:
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Expected Outcome:

# Chunk 1 [11, 45, 8]
# After reversing it [8, 45, 11]
# Chunk 2 [23, 14, 12]
# After reversing it [12, 14, 23]
# Chunk 3 [78, 45, 89]
# After reversing it [89, 45, 78]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunks = int(len(sample_list)/3)

print("Chunk 1:", sample_list[chunks-1 : : -1])
print("Chunk 2:", sample_list[2*chunks-1 : chunks-1 : -1])
print("Chunk 3:", sample_list[3*chunks-1 : 2*chunks-1 : -1])
