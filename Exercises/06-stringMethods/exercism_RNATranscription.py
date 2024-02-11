def to_rna(dna_strand):
    rna = ''
    for char in dna_strand:
        if char == 'G':
            rna = rna + 'C'
        if char == 'C':
            rna = rna + 'G'
        if char == 'T':
            rna = rna + 'A'
        if char == 'A':
            rna = rna + 'U'
    
    return rna