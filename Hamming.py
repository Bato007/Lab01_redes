class Hamming:
  def __init__(self, bits=None):
    if (bits is not None):
      self.data = ''.join(str(n) for n in bits)

  def generate(self):
    bits = self.data[:]
    m = len(bits)
    redundat_bits = 0
    for i in range(m):
      if(2**i >= m + i + 1):
        redundat_bits = i
        break

    # We add the parity bits as 0 in the 2^n position
    j = 0
    k = 1
    res = ''
    for i in range(1, m + redundat_bits+1):
      if(i == 2**j):
        res = res + '0'
        j += 1
      else:
        res = res + bits[-1 * k]
        k += 1
    full_bits = res[::-1]
    
    # Determine the parity bits
    n = len(full_bits)
    for i in range(redundat_bits):
      val = 0
      for j in range(1, n + 1):
        if(j & (2**i) == (2**i)):
          val = val ^ int(full_bits[-1 * j])
      full_bits = full_bits[:n-(2**i)] + str(val) + full_bits[n-(2**i)+1:]
    return full_bits

  def checkError(self, arr):
    n = len(arr)
    num_parity = 0
    res = 0

    # Get parity bits amount
    for bit_pos in range(n):
      if (2**bit_pos >= n):
        break
      else:
        num_parity += 1
    
    # Calculate parity bits again
    for i in range(num_parity):
      val = 0
      for j in range(1, n + 1):
        if(j & (2**i) == (2**i)):
          val = val ^ int(arr[-1 * j])
      res = res + val*(10**i)
    # Convert binary to decimal
    return int(str(res), 2)

  def get_original(self, bits):
    j = 0
    result = ''
    reversed_bits = bits[::-1]

    for i in range(1, len(bits) + 1):
      if(2**j == i):
        j += 1
      else:
        result += reversed_bits[i-1]
    return result[::-1]