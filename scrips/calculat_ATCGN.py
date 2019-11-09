genome = ""

with open("YBR092C.fasta", "r") as input_file:
    for line in input_file:
        if line[0] != ">":
            #print(line)
            line = line.strip().upper()
            
            genome = genome + line
		


A=genome.count("A")
T=genome.count("T")
G=genome.count("G")
C=genome.count("C")
lens=len(genome)


print('A%:'+str(int(A)/int(lens)))
print('T%:'+str(int(T)/int(lens)))
print('C%:'+str(int(C)/int(lens)))
print('G%:'+str(int(G)/int(lens)))
