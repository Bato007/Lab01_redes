from numpy import block


class Checksum:
    # Realiza Fletcher 16, por utilizar utf-8
    def __init__(self, message=None):
        self.message = message
        self.blockCount = int(len(message) / 8) if message else None
        self.blocks = []

    def defineBlocks(self):
        messageBlocks = []
        # Separate in blocks, and convert them to numbers from binary
        for i in range(0, self.blockCount):
            singleBlock = ''
            for j in range(0, 8):
                singleBlock += str(self.message[i*8 + j])
            messageBlocks.append(int(singleBlock, 2))
        return(messageBlocks)

    def encode(self):
        self.blocks = self.defineBlocks()
        c1, c2 = 0, 0
        for block in self.blocks:
            c1 += block
            c2 += c1
        c1 = c1 % 256
        c2 = c2 % 256
        self.blocks.append(c1)
        self.blocks.append(c2)
        return self.writeOutput()
    
    def writeOutput(self):
        encoded = ''
        for block in self.blocks:
            encoded += str(format(block,'08b'))
        return encoded

    def checkError(self, arr):
        self.message = arr
        self.blockCount = int(len(arr) / 8) - 2
        self.blocks = self.defineBlocks()
        self.blocks = self.defineBlocks()
        check1 = arr[-16:-8]
        check1 = int(check1, 2)
        check2 = arr[-8:]
        check2 = int(check2, 2)
        c1, c2 = 0, 0
        for block in self.blocks:
            c1 += block
            c2 += c1
        c1 = c1 % 256
        c2 = c2 % 256
        if check1 == c1 or check2 == c2:
            return 0
        else:
            return 1

    def get_original(self, bits):
        blocks = []
        for i in range(0, int(len(bits) / 8) - 2):
            singleBlock = ''
            for j in range(0, 8):
                singleBlock += str(bits[i*8 + j])
            blocks.append(singleBlock)
        message = ''
        for i in blocks:
            message += i
        return message