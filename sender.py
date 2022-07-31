from bitarray import bitarray
import random
from Fletcher import Checksum
from Parity import *

class Application:
    def __init__(self):
        self.message = ''
    
    def get_message(self):
        self.message = input('Ingrese mensaje: ')
        return self.message

class Verification:
    def __init__(self, message):
        self.message = message

    def toBitArray(self):
        bitArray = bitarray()
        bitArray.frombytes(self.message.encode('utf-8'))
        return bitArray

class Noise:
    def __init__(self, bitarray):
        self.bitarray = bitarray
        self.probability = input('Ingrese la probabilidad de error: ')
    
    def addNoise(self):
        for i in self.bitarray:
            rand = random.uniform(0, 1)

            try:
                float(self.probability)
                if rand < float(self.probability):
                    self.bitarray[i] = (self.bitarray[i] + 1) % 2
            except:
                a, b = self.probability.split('/')
                if rand < int(a) / int(b):
                    self.bitarray[i] = (self.bitarray[i] + 1) % 2
    
    def returnNoise(self):
        return self.bitarray

class Transmission:
    def __init__(self, message):
        self.message = message

    def send_message(self):
        # socket.send
        return


application = Application()
message = application.get_message()

verification = Verification(message)
bitarray = verification.toBitArray()

doubleParity = Parity(list(bitarray))
doubleParity.createFirstMatrix()

noiseDoubleParity = Noise(doubleParity.matrixToBitarray())
noiseDoubleParity.addNoise()
finalMessageParity = noiseDoubleParity.returnNoise()

print('\nCorreccion de errores: Paridad doble')
secondMatrix = doubleParity.createSecondMatrix(list(finalMessageParity))
doubleParity.checkError()
print('\n')

print('\nDeteccion de errores: Fletcher checksum')
cheksum = Checksum(finalMessageParity)
blocks = cheksum.encode()
print('\n')