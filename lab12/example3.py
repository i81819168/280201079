class DNA:
  dna_string = ""
  def __init__(self, dna_string):
    self.set_dna_string(dna_string)
  def get_dna_string(self):
    return self.dna_string
  def set_dna_string(self, dna_string):
    self.dna_string = dna_string
  def count_nucleotides(self):
    dict_dna = {"A":0, "G":0, "T":0, "C":0}
    for nuc in self.dna_string:
      dict_dna[nuc] += 1
    return dict_dna
  def calculate_complement(self):
    complement_dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    reversed_dna = self.dna_string[::-1]
    complement_dna = ""
    for nuc in reversed_dna:
      complement_dna = complement_dna + complement_dict[nuc]
    return DNA(complement_dna)

dna = DNA("AATGGGCTA")
complement_dna = dna.calculate_complement()
print(complement_dna.get_dna_string())