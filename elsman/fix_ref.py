file = open('references.bib',"r")
lines = file.readlines()
file.close()
for i,line in enumerate(lines):
    if '@' in line:
        if '_' in line:
            line = line.replace('_','-')
            print(line)
        lines[i]=line

file = open('ref.bib',"w")
file.writelines(lines)
file.close()
