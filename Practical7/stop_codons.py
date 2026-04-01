# read the file
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output_file = 'stop_genes.fa'
stop_genes = open(output_file,'w')

gene_name = ""
codon = ""
current_seq = ""
stop = ['TAA','TAG','TGA']
stopcodon = []

for line in input:
    line = line.rstrip()

    if line[0] == '>':
        if current_seq != "":
            stopcodon = []

            for i in range(0, len(current_seq)-2, 3):
                codon = current_seq[i:i+3]
                if codon in stop:
                    if codon not in stopcodon:
                        stopcodon.append(codon)

            if len(stopcodon) > 0:
                line1 = gene_name + "," + " ".join(stopcodon) + "\n"
                stop_genes.write(line1)
                stop_genes.write(current_seq + "\n")
                print(line1.strip())

        if "gene:" in line:
            gene_name = line.split("gene:")[1].split()[0]

        current_seq = ""

    else:
        current_seq = current_seq + line

# last gene
if current_seq != "":
    stopcodon = []

    for i in range(0, len(current_seq)-2, 3):
        codon = current_seq[i:i+3]
        if codon in stop:
            if codon not in stopcodon:
                stopcodon.append(codon)

    if len(stopcodon) > 0:
        line1 = gene_name + "," + " ".join(stopcodon) + "\n"
        stop_genes.write(line1)
        stop_genes.write(current_seq + "\n")
        print(line1.strip())

input.close()
stop_genes.close()


