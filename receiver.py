from Hamming import Hamming
from Parity import *
from Fletcher import Checksum
from bitarray import bitarray

class Transmission:
  def __init__(self, file_name='message.txt'):
    self.file_name = file_name

  def get_message(self):
    f = open(self.file_name, 'r')
    return f.read()

class Verification:
    def __init__(self, message):
        self.message = message

    def toString(self):
      return bitarray(self.message).tobytes().decode('utf-8')

# Checks the message from sender
print('----------------------\n\nParidad doble\n')
doubleParity = Parity('')
message_doubleParity = Transmission('doubleParity.txt').get_message()

secondMatrix = doubleParity.createSecondMatrix([int(char) for char in message_doubleParity])
correction = doubleParity.checkError()

if (correction == 0):
  print('No hubo ningun error')

try:
  original_message = doubleParity.get_message()
  original_message = ''.join(str(item) for innerlist in original_message for item in innerlist)
  print('Mensaje en bits:', original_message)
  received_message = Verification(original_message).toString()
  print('Mensaje recibido:', received_message)
except:
  ''

print('----------------------')

print('----------------------\n\nHamming\n')
# Checks the message from sender
message_hamming = Transmission('hamming.txt').get_message()
correction = Hamming().checkError(message_hamming)

if (correction == 0):
  print('No hubo ningun error')
else:
  print('El error se encuentra en la posicion: ', len(message_hamming)-correction+1)

try:
  original_message = Hamming().get_original(message_hamming)
  print('Mensaje en bits:', original_message)
  received_message = Verification(original_message).toString()
  print('Mensaje recibido:', received_message)
except:
  ''

print('----------------------')

print('----------------------\nFletcher\n')
# Checks the message from sender
message_checksum = Transmission('checksum.txt').get_message()
correction = Checksum().checkError(message_checksum)

if (correction == 0):
  print('No hubo ningun error')
else:
  print('Error detectado')

try:
  original_message = Checksum().get_original(message_checksum)
  print('Mensaje en bits:', original_message)
  received_message = Verification(original_message).toString()
  print('Mensaje recibido:', received_message)
except:
  ''

print('----------------------')