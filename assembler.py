f = open("compiler_output.txt", 'r')

dic = f.readline()
lst = dic.split()

mem = {}
for i in range((len(lst)-4)/4):
    mem[lst[3+4*i]] = int(lst[5+4*i])

x=f.readline()
op=["lw","sw","beq","j","add","addi","mul","muli"]
reg=['$s0', '$s1','$s2', '$s3', '$s4','$s5', '$s6', '$zero']
binary=["000","001","010","011","100","101","110","111"]
skip=["Loop","Exit"]
index = 0
loop_index = {}

for line in f.readlines():
    code = line.split()
    if (code[0] in skip):
        loop_index[code[0]+code[1]+';'] = index
    else:
        index = index + 1

f.close()
f = open("compiler_output.txt", 'r')
x=f.readline()
x=f.readline()
for line in f.readlines():
    print line
    code=line.split()
    if (code[0] in skip):
        continue
    else:
        index = index + 1
        for i in range(len(op)):
            if (op[i] ==  code[0]):
                op_code = str(binary[i]) +" "
        if(code[0]!="j"):
            for i in range(len(reg)):
                if (reg[i] ==  code[1]):
                    op_code = op_code + str(binary[i]) + " "
            if (code[0] == "sw" or code[0] == "lw"):
                op_code = op_code + format(mem[code[3][:len(code[3])-1]], '010b')
                print op_code
            elif (code[0] == "add" or code[0] == "addi" or code[0] == "mul" or code[0] == "muli"):
                for i in range(len(reg)):
                    if (reg[i] ==  code[3]):
                        op_code = op_code + str(binary[i]) + " "
                if (code[0] == "addi" or code[0] == "muli"):
                    op_code = op_code + format(int(code[5][:len(code[5])-1]), '07b')
                else:
                    for i in range(len(reg)):
                        if (reg[i] ==  code[5][:len(code[5])-1]):
                            op_code = op_code + str(binary[i])
                print op_code
            if (code[0] == "beq"):
                op_code = op_code + format(int(code[3]), '04b')
                op_code = op_code + format(int(loop_index[code[5]+code[6]]), '06b')
                print op_code
        else:
            op_code = op_code + format(int(loop_index[code[1]+code[2]]), '013b')
            print op_code
