def HammingDistance(s1, s2):
    """Calculate the Hamming distance between two strings."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    """Calculate the total Hamming distance between a pattern and a collection of DNA strings."""
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        HammingDistance_min = float('inf')  # Initialize to positive infinity
        for i in range(len(Text) - k + 1):
            Pattern_prime = Text[i:i+k]  # Extract k-mer from Text
            HammingDist = HammingDistance(Pattern, Pattern_prime)
            if HammingDist < HammingDistance_min:
                HammingDistance_min = HammingDist
        distance += HammingDistance_min
    return distance


