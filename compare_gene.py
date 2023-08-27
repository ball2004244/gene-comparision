from typing import Tuple, List

#* Description: find the positions of mismatches between s1 and s2
#* Provide that 2 genes have same length
#! Time complexity: O(n)
#! Space complexity: O(n)
def find_mismatch(s1: str, s2: str) -> List[int]:
    mismatch_pos = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatch_pos.append(i)
    return mismatch_pos

#* Description: find the number of changes to convert s1 to s2
#! Time complexity: O(mn)
#! Space complexity: O(mn)
def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    
    # initialize the matrix
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # initialize the first row
    for j in range(n + 1):
        dp[0][j] = j
        
    # initialize the first column
    for i in range(m + 1):
        dp[i][0] = i
        
    # fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]: # same character
                dp[i][j] = dp[i-1][j-1]
            else: # different character
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                
    return dp[m][n]

#* Description: return the difference positions between s1 and s2
#* provide that 2 genes has same length
def compare(s1: str, s2: str) -> Tuple[int, List[int]]:
    # check if 2 genes have different length
    if not len(s1) == len(s2):
        return -1, []
    
    # check if 2 genes are exactly the same
    if s1 == s2:
        return 0, []
    
    # find mismatches
    mismatch_pos = find_mismatch(s1, s2)
    return len(mismatch_pos), mismatch_pos
    
if __name__ == '__main__':
    s1 = 'ATCCCAA'
    s2 = 'ATCCCA'
    
    num_mismatch, mismatch_pos = compare(s1, s2)
    
    print('s1:', s1)
    print('s2:', s2)
    if num_mismatch == -1:
        print('Two genes have different length')
    elif num_mismatch == 0:
        print('Two genes are exactly the same')
    else:
        print('Number of mismatches:', num_mismatch)
        print('Mismatch positions:', mismatch_pos)
        
    print('Edit distance:', edit_distance(s1, s2))
    print('Done!')
    