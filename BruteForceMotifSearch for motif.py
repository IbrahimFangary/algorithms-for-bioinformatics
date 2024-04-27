def AllStrings(k):
    """Generate all possible k-mers of length k."""
    nucleotides = ['A', 'C', 'G', 'T']
    patterns = ['']
    for _ in range(k):
        patterns = [pattern + nucleotide for pattern in patterns for nucleotide in nucleotides]
    return patterns
def HammingDistance(s1, s2):
    """Calculate the Hamming distance between two strings."""
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def DistanceBetweenPatternAndStrings(Pattern, Dna):
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

def MedianString(Dna, k):
    distance = float('inf')  # Initialize distance to positive infinity
    patterns = AllStrings(k) #gives all posiible kmers that can be used to search with
    for Pattern in patterns:
        dist = DistanceBetweenPatternAndStrings(Pattern, Dna)
        if dist < distance:
            distance = dist
            Median = Pattern
    return Median
# Extract pattern and DNA strings from the text variable
text = """CTCGTAAATAGAACGCTTGTACCAAGGGCTAGAATGAAGCCA
AGAAGGACTTGACTTGGTGAGTATTGTGTGAGTCCGGGGACA
TCGTATAGAACGGTATTGCCAATCCGAGCCATGTGCTATTCA
CTTTATAGGTCGCGCCATACCCAAGCGCCGGGATTAAGAAGG
CATTTTACTTTACCGGGCCGGATTAGAAAGGCTAATGGTACG
GGCGTCAGAATGCTCCCTAAGGGTACCGAAAGAATGGATTAT
CTGGAGGCCATTTTATTGTGAAAGGCATGCAGAACGGTGGTC
TAAGACTTTCTCTCATACAAGTGTCTATCCGGACATAGAAGG
GGTTCAGCGCGTTTCAGATAAAATAGAAAGTTATTTTGAAGT
CCTCCATTAGACAGAATCTACCTTAGAACGACTCGATTCGGA"""

Dna = text.split()
k=6


print(MedianString(Dna, k))