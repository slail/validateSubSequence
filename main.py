# Validating Subsequence
'''
Given two non-empty arrays of integers, write a function that determines whether the second array
is a subsequence of the first one. A subsequence of an array is a set of numbers that aren't necessarily
 adjacent in the array but that are in the same order as they appear in the array.
 For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] ,and so do the numbers [2, 4] .
 Note that a single number in an array and the array itself are both valid subsequences of the array.
'''
'''
1. Traverse through both arrays.
2. Keep moving through the main array.
3. Check to see if the current element of the main array equals to the current element of the sequence.
4. If there's a match in step 3, move through the sequence. 
'''
# With While Loop
def validSequence(array, sequence):
    arrayIdx = 0
    seqIdx = 0
    while arrayIdx < len(array) and seqIdx < len(sequence):
        if array[arrayIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrayIdx += 1
    return seqIdx == len(sequence)

# With For Loop
def validSequence1(array, sequence):
    seqIdx = 0
    for values in array:
        if seqIdx == len(sequence):
            break
        if values == sequence[seqIdx]:
            seqIdx += 1
    return seqIdx == len(sequence)

print(validSequence([2, 4, 6, 8, 10, 12], [2, 6, 12]))
print(validSequence1([2, 4, 6, 8, 10, 12], [4, 6, 10]))