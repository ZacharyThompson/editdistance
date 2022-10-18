import pprint

class EditDist:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2
        # Initialize 2D matricies to all 0's
        # Distance Matrix is used to calculate the edit distance
        # Similarity and Alignment Matrices are used for printing the alignment
        self._distanceMatrix = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)] 
        self._similarityMatrix = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)] 
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

		# Fill out the rest of the matricies
        for i in range(1, len(self.word1)+1):
            for j in range(1, len(self.word2)+1):
                # Edit Distance Matrix
                Values = [self._distanceMatrix[j-1][i]+1, self._distanceMatrix[j][i-1]+1, self._distanceMatrix[j-1][i-1]+1]
                if self.word1[i-1] == self.word2[j-1]:
                    Values[2] -= 1
                self._distanceMatrix[j][i] = min(Values)

                # Similarity Matrix
                Values = [self._similarityMatrix[j-1][i], self._similarityMatrix[j][i-1], self._similarityMatrix[j-1][i-1]]
                if self.word1[i-1] == self.word2[j-1]:
                    Values[2] += 1
                self._similarityMatrix[j][i] = max(Values)

                # Alignment Matrix
                # 1 = UP, 2 = LEFT, 3 = DIAG
                if self._similarityMatrix[j][i] == self._similarityMatrix[j-1][i]:
                    self._alignmentMatrix[j][i] = 1
                elif self._similarityMatrix[j][i] == self._similarityMatrix[j][i-1]:
                    self._alignmentMatrix[j][i] = 2
                elif self._similarityMatrix[j][i] == self._similarityMatrix[j-1][i-1]+1:
                    self._alignmentMatrix[j][i] = 3
        return

    def getEditDistance(self):
        return self._distanceMatrix[len(self.word2)][len(self.word1)]

    def printDistanceMatrix(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self._distanceMatrix)
        print('\n')
        pp.pprint(self._similarityMatrix)
        print('\n')
        pp.pprint(self._alignmentMatrix)
        return

    def _printAlignmentRec(self, i, j):
        # Algorithm is a modified version of the PrintLCS algorithm on page 176
        self.string1 = ""
        self.string2 = ""
        if i==0 and j==0:
            self.string1 += self.word1[0]
            self.string2 += self.word2[0]
            return
        if i == 0:
            self.string1 += '_'
            self.string2 += self.word2[j-1]
            return
        if j == 0:
            self.string1 += self.word1[i-1]
            self.string2 += '_'
            return

        # i = horizontal, j = vertical
        # 1 = UP, 2 = LEFT, 3 = DIAG
        if self._alignmentMatrix[j][i] == 3:
            self._printAlignmentRec(i-1,j-1)
            self.string1 += self.word1[i-1]
            self.string2 += self.word2[j-1]
        else:
            if self._alignmentMatrix[j][i] == 2:
                self._printAlignmentRec(i,j-1)
                self.string1 += '_'
                self.string2 += self.word2[j-1]
            else:
                self._printAlignmentRec(i-1,j)
                self.string1 += self.word1[i-1]
                self.string2 += '_'

        return self.string1[::-1] + '\n' + self.string2[::-1]

    def printAlignment(self):
        print(self._printAlignmentRec(len(self.word1), len(self.word2)))
        return