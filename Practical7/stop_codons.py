# read the file
input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
ouput_file = 'stop_genes.fa'
stop_genes = open(ouput_file,'w')

gene_name = ""
codon = ""
current_seq = ""
stop = ['TAA','TAG','TGA']
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
        current_seq = ""

    else:
        current_seq = current_seq + line
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

input.close()
stop_genes.close()



