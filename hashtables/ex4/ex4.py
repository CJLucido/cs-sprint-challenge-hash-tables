def has_negatives(b):
    """
    YOUR CODE HERE
    """
    # Your code here

    analysis_cache = {}
    result = []
    for a in b:
        if a > 0:
            if analysis_cache.get(a) == "+ Value Only":
                pass
            elif analysis_cache.get(a) == "- Value Only":
                analysis_cache[a] = "Both"
                result.append(a)
            else:
                analysis_cache[a] = "+ Value Only"
        if a < 0:
            new_a = a*(-1)
            print(new_a)
            if analysis_cache.get(new_a) == "+ Value Only":
                analysis_cache[new_a] = "Both"
                result.append(new_a)
                
            elif analysis_cache.get(new_a) == "- Value Only":
                pass
            else:
                analysis_cache[new_a] = "- Value Only"

    print(len(analysis_cache))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
