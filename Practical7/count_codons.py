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

# draw a pie chart
plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%')
plt.title(f"{stop} distrubution of all in-frame codons")
plt.savefig(f"pie_{stop}.png")
plt.close()
