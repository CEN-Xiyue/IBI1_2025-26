# 1. create a dictionary
genedict = {}
genes = {'TP53':12.4, 'EGFR':15.1, 'BRCA1':8.2, 'PTEN':5.3,'ESR1':10.7}
print(genes)
genes ['MYC']=11.6
print(genes)
# 2. create a bar chart
import numpy as np
import matplotlib.pyplot as plt
N = len(genes)
gene_expression = np.array(list(genes.values()))
gene_names = list(genes.keys())
ind = np.arange(N)
width = 0.4
pl = plt.bar(ind,gene_expression, width)
plt.ylabel('gene expression level')
plt.title('	expression values of several genes measured in a biological	sample')
plt.xticks(ind, gene_names)
plt.show()

#3. create a variable EGFR to represent the target gene, EGFR can be modified into other genes as well
geneinterest = 'EGFR'
if geneinterest in genes:
    print("The expression value of",geneinterest,"is",genes[geneinterest])
else:
    print("Error:",geneinterest,"not found in the current sample")

#4. calculate the average gene expression values
average = sum(genes.values())/len(genes)
print("The average gene expression value is:",average)