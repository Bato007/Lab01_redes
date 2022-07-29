from bitarray import bitarray
import random

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

            if rand < float(self.probability):
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

noise = Noise(bitarray)
noise.addNoise()

finalMessage = noise.returnNoise()
