from enum import IntEnum
from typing import Tuple, List


Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str = 'ACGТGGCTCTCТAACGTACGТACGТACGGGGTПATATATACCCTAGGACТCCCПT'


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[1 + i]], Nucleotide[s[2 + i]])
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)