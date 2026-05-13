# Download the AA sequnce of DLX5 in human and rat
# Generate a random AA sequence with the same length of DLX5: 289 
from Bio import SeqIO
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices


# input BLOSUM matrix
bl62 = substitution_matrices.load("BLOSUM62")
aligner = PairwiseAligner()
aligner.substitution_matrix = bl62
aligner.open_gap_score = -10
aligner.extend_gap_score = -2


def get_seq(file):
    rec = SeqIO.read(file, "fasta")
    return str(rec.seq)


human = get_seq("DLX5_human.fasta")
mouse = get_seq("DLX5_mouse.fasta")
rand  = get_seq("random.fasta")

# 1. Human ns mouse
print("\n===== Human DLX5 vs Mouse DLX5 =====")
a1 = aligner.align(human, mouse)[0]
print(a1)
print("Score:", a1.score)
match = sum(1 for a,b in zip(a1[0],a1[1]) if a==b and a!='-')
total = sum(1 for a,b in zip(a1[0],a1[1]) if a!='-' and b!='-')
print(f"Similarity:{match/total*100:.1f}%\n")

# 2：human vs random
print("===== Human DLX5 vs random sequence =====")
a2 = aligner.align(human, rand)[0]
print(a2)
print("Score:", a2.score)
match2 = sum(1 for a,b in zip(a2[0],a2[1]) if a==b and a!='-')
total2 = sum(1 for a,b in zip(a2[0],a2[1]) if a!='-' and b!='-')
print(f"Similarity:{match2/total*100:.1f}%\n")

# 2：mouse vs random
print("===== Mouse DLX5 vs random sequence =====")
a3 = aligner.align(mouse, rand)[0]
print(a3)
print("Score:", a3.score)
match3 = sum(1 for a,b in zip(a3[0],a3[1]) if a==b and a!='-')
total3 = sum(1 for a,b in zip(a3[0],a3[1]) if a!='-' and b!='-')
print(f"Similarity:{match3/total*100:.1f}%\n")
