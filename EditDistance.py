import pprint

class EditDist:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2
        # Initialize 2D matrix to all 0's
        self.matrix = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)] 
        
    def calculateEditDistance(self):
        # Set initial values for the first row and column
        for i in range(0, len(self.word1)+1):
            self.matrix[0][i] = i
        for j in range(1, len(self.word2)+1):
            self.matrix[j][0] = j

		# Fill out the rest of the table
        for i in range(1, len(self.word2)+1):
            for j in range(1, len(self.word1)+1):
                up = self.matrix[i-1][j] + 1
                left = self.matrix[i][j-1] + 1

                diag = self.matrix[i-1][j-1] + 1
                if self.word1[j-1] == self.word2[i-1]:
                    diag -= 1
                
                self.matrix[i][j] = min(up, left, diag)


        return self.matrix[len(self.word2)][len(self.word1)]

    def printMatrix(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.matrix)
        return

    def printAlignment(self):
        return