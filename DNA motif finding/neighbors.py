def Neighbors(Pattern, d):
    # find the neighbors of a DNA pattern with up to d mismatches
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"} # Return all possible single nucleotides if Pattern is of length 1
    Neighborhood = set()
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for nucleotide in ["A", "C", "G", "T"]:
                Neighborhood.add(nucleotide + Text)
        else:
            Neighborhood.add(Pattern[0] + Text)
    return Neighborhood

def HammingDistance(s1, s2):
    #calculate the Hamming distance between two strings
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))




