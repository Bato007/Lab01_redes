from bitarray import bitarray
import random
from Fletcher import Checksum
from Parity import *
from Hamming import Hamming

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
    
    def addNoise(self, stop=None):
        entered = 0
        if stop:
            for i in range(len(self.bitarray) - 16):
                rand = random.uniform(0, 1)

                try:
                    float(self.probability)
                    if rand < float(self.probability):
                        entered += 1
                        self.bitarray[i] = (self.bitarray[i] + 1) % 2
                except:
                    a, b = self.probability.split('/')
                    if rand < int(a) / int(b):
                        entered += 1
                        self.bitarray[i] = (self.bitarray[i] + 1) % 2
        else:
            for i in self.bitarray:
                rand = random.uniform(0, 1)

                try:
                    float(self.probability)
                    if rand < float(self.probability):
                        entered += 1
                        self.bitarray[i] = (self.bitarray[i] + 1) % 2
                except:
                    a, b = self.probability.split('/')
                    if rand < int(a) / int(b):
                        entered += 1
                        self.bitarray[i] = (self.bitarray[i] + 1) % 2
        return entered

    def returnNoise(self):
        return self.bitarray

class Transmission:
    def __init__(self, message):
        self.message = message

    def send_message(self, file_name='message.txt'):
        f = open(file_name, 'w')
        f.write(self.message)
        f.close()

application = Application()
message = application.get_message()

verification = Verification(message)
ver_bitarray = verification.toBitArray()

print('\nCorreccion de errores: Paridad doble')
doubleParity = Parity(list(ver_bitarray))
doubleParity.createFirstMatrix()

noiseDoubleParity = Noise(doubleParity.matrixToBitarray())
noiseDoubleParity.addNoise()
finalMessageParity = list(noiseDoubleParity.returnNoise())

finalMessageParity = list(noiseDoubleParity.returnNoise())
message_doubleParity = ''.join(str(item) for item in list(finalMessageParity))
transmition_doubleParity = Transmission(message_doubleParity)
transmition_doubleParity.send_message('doubleParity.txt')
print('\n')

print('\nCorreccion de errores: Algoritmo de Hamming')
    # Creating message
hamming = Hamming(list(ver_bitarray))
bits_hamming = hamming.generate()

    # Generating error
noise_hamming = Noise(bitarray(bits_hamming))
noise_hamming.addNoise()
temp_message_hamming = noise_hamming.returnNoise()

    # Makes string to send
message_hamming = ''.join(str(n) for n in list(temp_message_hamming))
transmition_hamming = Transmission(message_hamming)
transmition_hamming.send_message('hamming.txt')

print('Mensaje original:', ''.join(str(n) for n in bitarray(ver_bitarray)))
print('Hamming genero los siguientes bits:', bits_hamming)
print('El mensaje enviado fue el siguiente:', message_hamming)
print('\n')

print('\nDeteccion de errores: Fletcher checksum')
# Creating Fletcher Checksum message
cheksum = Checksum(ver_bitarray)
blocks = cheksum.encode()

    # Generating error
noise_checksum = Noise(bitarray(blocks))
noise_checksum.addNoise(stop=True)
temp_message_checksum = noise_checksum.returnNoise()

    # Makes string to send
message_checksum = ''.join(str(n) for n in list(temp_message_checksum))
transmition_checksum = Transmission(message_checksum)
transmition_checksum.send_message('checksum.txt')

print('Mensaje original:', ''.join(str(n) for n in bitarray(ver_bitarray)))
print('Fletcher Checksum genero los siguientes bits:', blocks)
print('El mensaje enviado fue el siguiente:', message_checksum)
print('\n')