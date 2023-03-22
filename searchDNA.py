from enum import IntEnum
from typing import Tuple, List


Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str = 'ATTACACACATTGGGA'


def stringToGene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[1 + i]], Nucleotide[s[2 + i]])
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)

print(my_gene)


#linear search O(n)
def linearSearch(gene: Gene, k_codon: Codon) -> bool:
    for i in Gene:
        if i == k_codon:
            return True
    return False


#bi search O(lg(n)), but O(n*lg(n)) if first we sorting list
def binSearch(gene: Gene, k_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high:
        mid: int = (low + high) // 2
        if gene[mid] < k_codon:
            low = mid + 1
        elif gene[mid] > k_codon:
            high = mid - 1
        else:
            return True
    return False