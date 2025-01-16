"""
1. write a function to find the length of the longest common subsequence
#   between two sequences. E.g Given the strings "serendipitious" and 
    "precipitation"; the longest common subsequence is "repito" and its length is 7
"""
# create a counter for 2 different sequences and compute lcs seq1
# if seq1 and seq2 are equal, then char belongs to LCS and the length is tracked
# else we move to next idx in the seq1 and seq2
# recursively calculate the lcs
# return number of char


def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        opt1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        opt2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(opt1, opt2)

