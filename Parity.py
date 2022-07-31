from bitarray import bitarray

class Parity:
    def __init__(self, firstMessage):
        self.firstMessage = firstMessage

    # Se crea la matrix de paridades con el mensaje sin noise
    def createFirstMatrix(self):
        firstMatrix = []
        for i in range(0, len(self.firstMessage), 8):
            row = self.firstMessage[i:i + 8]
            sumBits = sum(row) % 2
            row.append(sumBits)
            firstMatrix.append(row)

        col_totals = [ (sum(x) % 2) for x in zip(*firstMatrix) ]
        firstMatrix.append(col_totals)
        self.firstMatrix = firstMatrix

        # print(*firstMatrix, sep='\n')
        
    # Convierte de matriz a bitarray
    def matrixToBitarray(self):
        oneDimensionMatrix = []
        for row in self.firstMatrix:
            for element in row:
                oneDimensionMatrix.append(element)

        return bitarray(oneDimensionMatrix)

    # Se crea la matriz del mensaje con noise
    def createSecondMatrix(self, noiseMessage):
        secondMatrix = []
        for i in range(0, len(noiseMessage), 9):
            row = noiseMessage[i:i + 9]
            secondMatrix.append(row)

        print(*secondMatrix, sep='\n')
        self.secondMatrix = secondMatrix
        
    # Se verifica si hay error en las paridades recibidas
    def checkError(self):
        for row in self.secondMatrix:
            parityToTest = row.pop()
            possibleParity = sum(row) % 2
            if (possibleParity != parityToTest):
                print('Error de paridad en la fila', row)
        
        lastRow = self.secondMatrix.pop()
        possibleParity = [ (sum(x) % 2) for x in zip(*self.secondMatrix) ]

        for i in range(len(lastRow)):
            if (possibleParity[i] != lastRow[i]):
                print('Error de paridad en la columna', i)

