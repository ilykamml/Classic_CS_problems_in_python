class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # first tag
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            match nucleotide:
                case 'A': self.bit_string |= 0b00  # A == 00
                case 'C': self.bit_string |= 0b01  # C == 01
                case 'G': self.bit_string |= 0b10  # G == 10
                case 'T': self.bit_string |= 0b11  # T == 1
                case _: raise ValueError("Invalid nucleotide: {}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11
            match bits:
                case 0b00: gene += 'A'
                case 0b01: gene += 'C'
                case 0b10: gene += 'G'
                case 0b11: gene += 'T'
                case _: raise ValueError("Invalid bits: {}".format(bits))
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTATATATATATAAAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 1000

    print("Original is {} bytes".format(getsizeof(original)))

    compressed: CompressedGene = CompressedGene(original)  # zipping

    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))

    print(str(compressed)[:60] + "...")

    print("Original and decompressed are the same: {}".format(original == compressed.decompress()))

    print("Saved {:.2f}% of memory".format((1 - getsizeof(compressed.bit_string) / getsizeof(original)) * 100))
