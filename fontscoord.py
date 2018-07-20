import io,re

def id2char(id):
    char_bytes=(id).to_bytes(2,'little')
    return char_bytes.decode('utf-16')

def getInt(line,left,right):
    return int(line[left:right].strip())

def main():
    fname='custom' # имя .fnt файла
    fnt_file=io.open(fname+'.fnt')
    fnt_lines=fnt_file.readlines()
    fnt_file.close()
    output=[]
    for line in fnt_lines:
        if line[:5]=="char ":
            result = re.findall(r"char\s+id=(\d+)\s+x=(\d+)\s+y=(\d+)\s+width=(\d+)\s+height=(\d+)", line)
            char=id2char(int(result[0][0]))
            x=int(result[0][1])
            y = int(result[0][2])
            width=int(result[0][3])
            height=int(result[0][4])
            output.append(char+'\n')
            output.append('%d %d %d %d\n'%(x,y,width,height))

    new_fnt_file=io.open(fname+'.txt','w',encoding='utf-16')
    new_fnt_file.writelines(output)
    new_fnt_file.close()

if __name__ == "__main__":
    import sys
    sys.exit(main())