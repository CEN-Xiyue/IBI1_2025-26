# read the file
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output_file = 'stop_genes.fa'
stop_genes = open(output_file,'w')

gene_name = ""
codon = ""
current_seq = ""
stop = ['TAA','TAG','TGA']
stopcodon = ""

# identify sequence with stop codons
for line in input:
    line = line.rstrip()   

    if line[0] == '>':  
        # the first gene
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
                stop_genes.write(current_seq + "\n")   
                

        # fetch the name
        if "gene:" in line:
            gene_name = line.split("gene:")[1].split()[0]

        current_seq = ""

    else:
        current_seq = current_seq + line  

# The last gene
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
        stop_genes.write(current_seq + "\n")   
        

# close files
input.close()
stop_genes.close()