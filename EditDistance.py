import pprint

class EditDist:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2
        # Initialize 2D matricies to all 0's
        # Distance Matrix is used to calculate the edit distance
        # Alignment Matrix is used for printing the alignment
        self._distanceMatrix = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)] 
        self._alignmentMatrix = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)] 
        
    def calculate(self):
        # Algorithm is a modified version of the LCS algorithm on page 176
        # Set initial values for the first row and column
        # of the Edit Distance Matrix
        # i = horizontal, j = vertical
        for i in range(0, len(self.word1)+1):
            self._distanceMatrix[0][i] = i
        for j in range(1, len(self.word2)+1):
            self._distanceMatrix[j][0] = j

		# Fill out the the matricies
        for i in range(1, len(self.word1)+1):
            for j in range(1, len(self.word2)+1):
                # Edit Distance Matrix
                Values = [self._distanceMatrix[j-1][i]+1, self._distanceMatrix[j][i-1]+1, self._distanceMatrix[j-1][i-1]+1]
                if self.word1[i-1] == self.word2[j-1]:
                    Values[2] -= 1
                self._distanceMatrix[j][i] = min(Values)

                # Alignment Matrix
                # 1 = UP, 2 = LEFT, 3 = DIAG
                self._alignmentMatrix[j][i] = Values.index(min(Values)) + 1
        return

    def getEditDistance(self):
        return self._distanceMatrix[len(self.word2)][len(self.word1)]

    def printDistanceMatrix(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self._distanceMatrix)
        return

    def printAlignment(self):
        # i = horizontal, j = vertical
        # 1 = UP, 2 = LEFT, 3 = DIAG
        i = len(self.word1)
        j = len(self.word2)
        string1 = ""
        string2 = ""

        # Walk through the alignment matrix starting from the bottom right
        # and construct the strings to be printed
        while i > 0 and j > 0:
            if self._alignmentMatrix[j][i] == 3:
                string1 = self.word1[i-1] + string1
                string2 = self.word2[j-1] + string2
                i-=1
                j-=1
            elif self._alignmentMatrix[j][i] == 2:
                string1 = self.word1[i-1] + string1
                string2 = '_' + string2
                i-=1
            elif self._alignmentMatrix[j][i] == 1:
                string1 = '_' + string1
                string2 = self.word2[j-1] + string2
                j-=1

        if i == 0 and j !=0:
            string1 = '_' + string1
            string2 = self.word2[j-1] + string2
        elif j == 0 and i != 0:
            string1 = self.word1[i-1] + string1
            string2 = '_' + string2

        print(string1 + '\n' + string2)
        return