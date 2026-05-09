import matplotlib.pyplot as plt

# read the original fasta file
data = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
gene = ""
seq = ""
genes = {}

for line in data:
    if line[0] == ">":
        if gene and seq:
            genes[gene] = seq
        if "gene:" in line:
            gene = line.split("gene:")[1].split()[0]
        else:
            gene = line[1:].split()[0]
        seq = ""
    else:
        seq = seq + line.strip()
if gene and seq:
    genes[gene] = seq
data.close()

# let user input stop codon
stop = input("Enter the stop codon(TAA/TAG/TGA): ")
while stop not in ["TAA","TAG","TGA"]:
    stop = input("Error, codon must be either TAA, TAG or TGA, try again: ")

# cound the codons
counts = {}
for g, s in genes.items():
    stops = [i for i in range(0, len(s)-2, 3) if s[i:i+3] == stop]
    if stops:
        end = max(stops)
        for i in range(0, end, 3):
            c = s[i:i+3]
            counts[c] = counts.get(c, 0) + 1
# report the count for each codon
print("Counts of in-frame codons upstream of", stop)
for codon in counts:
    print(codon, counts[codon])


# draw a big pie chart
# Combine the codons whose porpotions are <2% into the group "others" to make the pie chart clearer
total = sum(counts.values())
main_counts = {}
other_codons = []

for codon, cnt in counts.items():
    if (cnt / total) * 100 < 2:
        other_codons.append(codon)
    else:
        main_counts[codon] = cnt

if other_codons:
    #split the lines other codons every 10 codons
    codon_lines = []
    for i in range(0, len(other_codons), 10):
        codon_lines.append(", ".join(other_codons[i:i+10]))
    codon_str = ",\n".join(codon_lines)
    # label other codons
    label = f"Others\n(contributions <2%):\n{codon_str}"
    main_counts[label] = sum(counts[c] for c in other_codons)

plt.figure(figsize=(16, 16), dpi=150)

wedges, texts, autotexts = plt.pie(
    main_counts.values(),
    labels=main_counts.keys(),
    autopct='%1.1f%%',
    pctdistance=0.7,
    labeldistance=1.05,
    startangle=90,
    textprops={'fontsize': 9},
    rotatelabels=False  
)
plt.setp(autotexts, size=9, weight="bold", color="white")

plt.title(f"{stop} distribution of all in-frame codons", fontsize=16, pad=30)
plt.tight_layout()
plt.savefig(f"pie_{stop}.png", bbox_inches='tight')
plt.close()
