def reverseWords(s: str) -> str:
    """
    - keep an answer list where you can keep adding words
    - start from i
    - find the next occurrence index of a space or string end, call it j
    - run iteration from j to i, in reverse, and add the characters in that order
    - at the end, join the answer list into a string 
    """

    ans = []
    n = len(s)
    
    i, j = 0, 0
    while i < n:
        
        #iterate till we find a space or the end of the list
        while i < n and s[i] != " ":
            print(f"At i={i}")
            i += 1
        
        revWord = []
        #run loop in reverse order

        print(i-1, j-1)
        for k in range(i-1, j-1, -1):
            print(f"Adding i'em: {s[k]}")
            revWord.append(s[k])
        
        ans.append("".join(revWord))

        i += 1
        j = i

    return " ".join(ans)

print(reverseWords("Let's take LeetCode contest"))