class Checksum:
    # Realiza Fletcher 16, por utilizar utf-8
    def __init__(self, message):
        self.message = message
        self.blockCount = int(len(message) / 8)
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