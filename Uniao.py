from turing_machine import turing_machine # representa a turing machine
from tape import Tape # representa uma unidade de fita
import sys



fp = open(sys.argv[1], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
lines_cmd = fp.readlines()
lines = []
for line in lines_cmd:
        lines.append(line.rstrip())
number_of_lines  = len(lines)
'''valores de entrada que representam a turing machine de entrada'''
input_alphabet   = lines[0].split()
tape_alphabet    = lines[1]
whitespace       = lines[2]
states           = lines[3].split()
initial_state    = lines[4]
final_states     = lines[5].split()
number_of_tapes  = lines[6]
transitions      = []


fp2 = open(sys.argv[2], "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
lines2_cmd = fp2.readlines()
lines2 = []
for line in lines2_cmd:
        lines2.append(line.rstrip())
number_of_lines2  = len(lines2)
'''valores de entrada que representam a turing machine de entrada'''
input_alphabet2   = lines2[0].split()
tape_alphabet2    = lines2[1]
whitespace2       = lines2[2]
states2           = lines2[3].split()
initial_state2    = lines2[4]
final_states2     = lines2[5].split()
number_of_tapes2  = lines2[6]
transitions2      = []

lista = list()

for i in states:
        i = '1'+i
        lista.append(i)


states = lista


for i in range(7, number_of_lines):
        transitions.append(lines[i].split())

initial_state = '1'+initial_state 

lista = list()

for i in final_states:
        i = '1'+i
        lista.append(i)

final_states = lista

for t in transitions:
        t[0] = '1'+t[0]
        t[1] = '1'+t[1]

lista = list()

for i in states2:
    i = '2'+i
    lista.append(i)

states2 = lista

for i in range(7, number_of_lines2):
        transitions2.append(lines2[i].split())

initial_state2 = '2'+initial_state2 

lista = list()

for i in final_states2:
        i = '2'+i
        lista.append(i)

final_states2 = lista


for t in transitions2:
        t[0] = '2'+t[0]
        t[1] = '2'+t[1]


        
for i in transitions2:
        if i[0] == initial_state2:
                i[0] = initial_state
        if i[1] == initial_state2:
                i[1] = initial_state



arq = open('Out.txt','w+')

for i in input_alphabet:
        if i not in input_alphabet2:
                arq.write(i)
                arq.write(' ')
for i in input_alphabet2:
        arq.write(i)
        arq.write(' ')

arq.write('\n')

for i in tape_alphabet:
        if i not in tape_alphabet2:
                arq.write(i)
                arq.write(' ')
for i in tape_alphabet2:
        if i!=' ':
                arq.write(i)
                arq.write(' ')

arq.write('\n')

if whitespace != whitespace2:
        for i in transitions2:
                if i[2] == whitespace2:
                        i[2] = whitespace
                elif i[3] == whitespace2:
                        i[3] = whitespace
        whitespace2 = whitespace

arq.write(whitespace)

arq.write('\n')

lista = list()

for i in states2:
        if i != initial_state2:
                lista.append(i)

states2 = lista

for i in transitions2:
        if i[0] == initial_state2:
                i[0] = initial_state
        elif i[1] == initial_state2:
                i[1] = initial_state

initial_state2 = initial_state


for i in states:
        arq.write(i)
        arq.write(' ')

for i in states2:
        arq.write(i)
        arq.write(' ')

arq.write('\n')
arq.write(initial_state)

arq.write('\n')

for i in final_states:
        arq.write(i)
        arq.write(' ')

for i in final_states2:
        arq.write(i)
        arq.write(' ')

arq.write('\n')

arq.write(number_of_tapes)

arq.write('\n')

for i in transitions:
        for j in i:
                arq.write(j)
                arq.write(' ')
        arq.write('\n')

for i in transitions2:
        for j in i:
                arq.write(j)
                arq.write(' ')
        arq.write('\n')

arq.close()