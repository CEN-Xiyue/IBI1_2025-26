# read the file
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
<<<<<<< HEAD
output_file = 'stop_genes.fa'
stop_genes = open(output_file,'w')
=======
ouput_file = 'stop_genes.fa'
stop_genes = open(ouput_file,'w')
>>>>>>> 7b6f9555e7d02142aed914d410a86473c0dabac8

gene_name = ""
codon = ""
current_seq = ""
stop = ['TAA','TAG','TGA']
<<<<<<< HEAD
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

=======
stopcodon = ""

# identify sequence with stop codons, sequences without should not be returned
for line in input:
    if line[0]=='>':
        if current_seq != "":
            stopcodon = ""
            for i in range(0, len(current_seq)-2, 3):
                codon = current_seq[i:i+3]
                if codon in stop:
                    stopcodon = codon
                    break

            if stopcodon != "":
                line1 = gene_name + "," + stopcodon + "\n"
                stop_genes.write(line1)     
                print(line1.strip()) 
# fetch the gene names
        if "gene:" in line:
            gene_name = line.split("gene:")[1].split()[0]
>>>>>>> 7b6f9555e7d02142aed914d410a86473c0dabac8
        current_seq = ""

    else:
        current_seq = current_seq + line
<<<<<<< HEAD

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
=======
 # the last genetic sequence
if current_seq != "":
    stopcodon = ""
    for i in range(0, len(current_seq)-2, 3):
        codon = current_seq[i:i+3]
        if codon in stop:
            stopcodon = codon
            break
    if stopcodon != "":
        line1 =  gene_name + "," + stopcodon + "\n"
        stop_genes.write(line1) 
        print(line1.strip()) 
>>>>>>> 7b6f9555e7d02142aed914d410a86473c0dabac8

input.close()
stop_genes.close()


<<<<<<< HEAD
=======

>>>>>>> 7b6f9555e7d02142aed914d410a86473c0dabac8
