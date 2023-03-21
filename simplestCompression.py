
#trivial compression
class CompressedGene:

    def __init__(self, gene: str) -> None:
        self.__compress(gene)

    def __compress(self, gene: str) -> None:
        self.bit_string: int = 1 #initial label
        for nucleotide in gene.upper():
            self.bit_string <<= 2 #left shift by 2 bits
            if nucleotide =='A': #change the last 2 bits to
                self.bit_string |= 0b00
            elif nucleotide =='C':#change the last 2 bits to
                self.bit_string |= 0b01
            elif nucleotide =='G':#change the last 2 bits to
                self.bit_string |= 0b10
            elif nucleotide =='T':#change the last 2 bits to
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))


    def decompress(self) -> str:
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2): #-1 for exclude a label
            bits: int = self.bit_string >> i & 0b11 #get 2 significant bits
            self.bit_string <<= 2 #left shift by 2 bits
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:#change the last 2 bits to
                gene += 'C'
            elif bits == 0b10:#change the last 2 bits to
                gene += 'G'
            elif bits == 0b11:#change the last 2 bits to
                gene += 'T'
            else:
                raise ValueError("Invalid bits: {}".format(bits))
        return gene[::-1] #inverting a string using a reverse slice

    def __str__(self) -> str:
        return self.decompress()


if __name__ == '__main__':
    from sys import getsizeof
    original: str = "TAGC"
    print('original is {} bytes'.format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print('compressed is {} bytes'.format(getsizeof(compressed.bit_string)))
    print(compressed)
    print('original and decompressed are the same: {}'.format(original == compressed.decompress()))