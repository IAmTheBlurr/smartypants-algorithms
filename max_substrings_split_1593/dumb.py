
def max_unique_split(s):
    """ Returns the maximum number of unique substrings that can be split from s, the dumb way """
    def backtrack(start, seen):
        """ Backtracking function to find the maximum number of unique substrings... so dumb... """
        nonlocal max_unique
        if start == len(s):
            max_unique = max(max_unique, len(seen))
            return
        for i in range(start, len(s)):
            sub = s[start:i + 1]
            if sub not in seen:
                seen.add(sub)
                backtrack(i + 1, seen)
                seen.remove(sub)

    max_unique = 0
    backtrack(0, set())
    return max_unique
