import sys,os


script,gtffile,outputfile=sys.argv
# gtffile: a gtf file of gene annotations
# outputfile: file name of extracted genes and their length

def genelength(gtffile,outputfile):
    f=open(gtffile)
    fnew=open(outputfile,'w')
    for line in f:
        if line[0] != '#':
            t=line.split('\t')
            if t[2] == 'gene':
                length    = int(t[4]) - int(t[3])+1
                gene_id   = line.split('gene_id')[1].split('"')[1]
                gene_name = line.split('gene_name')[1].split('"')[1]
                out ='\t'.join([gene_id,gene_name,str(length)])+'\n'
                fnew.write(out)
    f.close()
    fnew.close()

# main
genelength(gtffile,outputfile)





                

