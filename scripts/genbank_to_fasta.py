from Bio import SeqIO

records = SeqIO.parse("1A01_2.region001.gbk", "genbank")
count = SeqIO.write(records, "1A01_2.region001.fasta", "fasta")
print("Converted %i records" % count)