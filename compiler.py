import cPickle as pickle

f= open('input.txt','r')
count=1;
sp = 1023
mem = {}
lst = ['$s6', '$s5','$s4', '$s3', '$s2','$s1', '$s0']
assembly = ""
reg_dic = {}

for line in f.readlines():
    code = line.split()
    if (len(code) > 0):
        if (code[0] == "int"):
            mem[code[1]] = sp
            sp = sp - 1
            if (reg_dic.get(code[1], -1) == -1):
                reg = lst.pop()
                reg_dic[code[1]] = reg
        elif (code[1] == '='):
            if (len(code) == 5 and code[3] == '+'):
                reg1= reg_dic[code[2]]
                print "    lw    " +  reg1 + " , " + code[2] + ";"
                assembly = assembly + "    lw    " +  reg1 + " , " + code[2] + ";\n"
                reg2= reg_dic.get(code[4],-1)
                print "    lw    " +  reg2 + " , " + code[4] + ";"
                assembly = assembly + "    lw    " +  reg2 + " , " + code[4] + ";\n"
                reg= reg_dic[code[0]]
                print "    add  " +  reg + " , " + reg1 + " , " + reg2 + ";"
                assembly = assembly + "    add  " +  reg + " , " + reg1 + " , " + reg2 + ";\n"
                print "    sw    " + reg + " , " + code[0] +";"
                assembly = assembly + "    sw    " + reg + " , " + code[0] +";\n"
            elif (len(code) == 5 and code[3] == '*'):
                reg1= reg_dic[code[2]]
                print "    lw    " +  reg1 + " , " + code[2] + ";"
                assembly = assembly + "    lw    " +  reg1 + " , " + code[2] + ";\n"
                reg2= reg_dic.get(code[4],-1)
                print "    lw    " +  reg2 + " , " + code[4] + ";"
                assembly = assembly + "    lw    " +  reg2 + " , " + code[4] + ";\n"
                reg= reg_dic[code[0]]
                print "    mul  " +  reg + " , " + reg1 + " , " + reg2 + ";"
                assembly = assembly + "    mul  " +  reg + " , " + reg1 + " , " + reg2 + ";\n"
                print "    sw    " + reg + " , " + code[0] +";"
                assembly = assembly + "    sw    " + reg + " , " + code[0] +";\n"
            else:
                reg1= reg_dic[code[0]]
                print "    addi " +  reg1 + " , " + "$zero" + " , " + code[2] + ";"
                assembly = assembly + "    addi " +  reg1 + " , " + "$zero" + " , " + code[2] + ";\n"
                print "    sw    " + reg1 + " , " + code[0] +";"
                assembly = assembly + "    sw    " + reg1 + " , " + code[0] +";\n"
        elif (code[0] == "for"):
            mem[code[1]] = sp
            sp = sp - 1
            loop = code[1]
            if (reg_dic.get(code[1], -1) == -1):
                reg = lst.pop()
                reg_dic[code[1]] = reg
            reg1= reg_dic[code[1]]
            print "    addi " +  reg1 + " , " + "$zero" + " , " + '0' + ";"
            assembly = assembly + "    addi " +  reg1 + " , " + "$zero" + " , " + '0' + ";\n"
            print "    sw    " + reg1 + " , " + code[1] +";"
            assembly = assembly + "    sw    " + reg1 + " , " + code[1] +";\n"
            print "Loop " + str(count) +" :"
            assembly = assembly + "Loop " + str(count) +" :\n"
            print "    beq " + reg1 + " , " + code[3] + " , " + "Exit "+ str(count) + ";"
            assembly = assembly + "    beq " + reg1 + " , " + code[3] + " , " + "Exit "+ str(count) + ";\n"
        elif (code[0] == "end"):
            reg1= reg_dic[loop]
            print "    addi " +  reg1 + " , " + reg1 + " , " + '1' + ";"
            assembly = assembly + "    addi " +  reg1 + " , " + reg1 + " , " + '1' + ";\n"
            print "    sw    " + reg1 + " , " + loop +";"
            assembly = assembly + "    sw    " + reg1 + " , " + loop +";\n"
            print "    j     Loop "+ str(count) + ";"
            assembly = assembly + "    j     Loop "+ str(count) + ";\n"
            print "Exit "+ str(count) + " :"
            assembly = assembly + "Exit "+ str(count) + " :\n"
            count  = count + 1


f.close()
f = open("D:\compiler_output.txt",'w')
f.write("mem = { ")
for i in mem:
    f.write(str(i) + " : " + str(mem[i]) + " , ")
f.write("} \n\n")
f.write(assembly)
f.close()
