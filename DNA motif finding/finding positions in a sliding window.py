import os
Text = ""# the text of the DNA
k = 9 #lenth of the kmer
L=500 #sliding window of length L
t=3 # the min number of occurrences required 
def FrequencyTable(Text,k):
    #generate frequency table of k-mers in a given text
    dic={}
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        if pattern in dic:
            dic[pattern]=dic[pattern]+1 
        else:
            dic[pattern]=1
    return dic  
def BetterFrequentWords(Text, k):
    #find the most frequent k-mers in a given text
    FrequentPatterns = []  # Initialize an array to store frequent patterns
    freqMap = FrequencyTable(Text, k)  # Get frequency table for patterns of length k
    maxCount = max(freqMap.values())  # Find the maximum count among the patterns
    
    for Pattern, count in freqMap.items():
        if count == maxCount:
            FrequentPatterns.append(Pattern)
    
    return FrequentPatterns
def FindClumps(Text, k, L, t):
    #find (k, L)-clumps in a given text
    patterns = []
    n = len(Text)
    for i in range(n - L + 1):
        window = Text[i:i+L]
        freq_map = FrequencyTable(window, k)
        for pattern, count in freq_map.items():
            if count >= t and pattern not in patterns:
                patterns.append(pattern)
    return patterns
# writing the output in a file named result iinto desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, 'result.txt')

with open(file_path, 'w') as file:
    for pos in FindClumps(Text, k, L, t):
        file.write(str(pos) + '\n')
print(FindClumps(Text, k, L, t))