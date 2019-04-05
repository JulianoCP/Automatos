from turing_machine import turing_machine # representa a turing machine
from tape import Tape # representa uma unidade de fita
import sys


def lerArquivo():
        '''ABRINDO, LENDO E RECEBENDO OS DADOS DO ARQUIVO .TXT DAS DUAS MAQUINAS DE TURING'''

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


        ''' adicionando cada transição da primeira maquina de turing ao vetor de transições'''
        for i in range(7, number_of_lines):
                transitions.append(lines[i].split())


        ''' adicionando cada transição da segunda maquina de turing ao vetor de transições'''
        for i in range(7, number_of_lines2):
                transitions2.append(lines2[i].split())
        
        transformacao(initial_state,initial_state2,input_alphabet,input_alphabet2,tape_alphabet,tape_alphabet2,whitespace,whitespace2,states,states2,final_states,final_states2,number_of_tapes,number_of_tapes2,transitions,transitions2)


#################################################################################


def transformacao(initial_state,initial_state2,input_alphabet,input_alphabet2,tape_alphabet,tape_alphabet2,whitespace,whitespace2,states,states2,final_states,final_states2,number_of_tapes,number_of_tapes2,transitions,transitions2):
        '''MANIPULANDO AS VARIAVEIS QUE ARMAZENAM OS DADOS DAS MAQUINAS DE TURING'''

        ''' adicionado o digito 1 na frente dos nomes dos estados da primeira maquina de turing'''
        lista = list()

        for i in states:
                i = '1'+i
                lista.append(i)

        states = lista.copy()


        ''' adicionando o digito 1 na frente do nome do estado inicial da primeira maquina de turing'''
        initial_state = '1'+initial_state 



        ''' adicionando o digito 1 na frente do nome de cada estado final'''
        lista.clear()

        for i in final_states:
                i = '1'+i
                lista.append(i)

        final_states = lista.copy()


        ''' adicionando o digito 1 na frene dos estados usados em cada transição dentre a todas transições possiveis '''
        for t in transitions:
                t[0] = '1'+t[0]
                t[1] = '1'+t[1]


        ''' adicionando o digito 2 na frente do nome de cada estado da segunda maquina de turing'''
        lista.clear()

        for i in states2:
            i = '2'+i
            lista.append(i)

        states2 = lista.copy()


        ''' adicionando o digito 2 na frente do estado inicial da segunda maquina de turing'''
        initial_state2 = '2'+initial_state2 


        ''' adicionando o digito 2 na frente dos estados finais da segunda maquina de turing'''
        lista.clear()

        for i in final_states2:
                i = '2'+i
                lista.append(i)

        final_states2 = lista.copy()


        '''adicionando o digito 2 na frene dos estados usados em cada transição dentre a todas transições possiveis '''
        for t in transitions2:
                t[0] = '2'+t[0]
                t[1] = '2'+t[1]


        ''' substituindo as aparições do estado inicial da inicial da segunda maquina de turing pelo estado inicial da primeira maquina de turing'''
        for i in transitions2:
                if i[0] == initial_state2:
                        i[0] = initial_state
                if i[1] == initial_state2:
                        i[1] = initial_state
        
        escrevendoUniao(initial_state,initial_state2,input_alphabet,input_alphabet2,tape_alphabet,tape_alphabet2,whitespace,whitespace2,states,states2,final_states,final_states2,number_of_tapes,number_of_tapes2,transitions,transitions2)


##################################################################################################


def escrevendoUniao(initial_state,initial_state2,input_alphabet,input_alphabet2,tape_alphabet,tape_alphabet2,whitespace,whitespace2, states,states2,final_states,final_states2,number_of_tapes,number_of_tapes2,transitions,transitions2):
        ''' ABRINDO E ESCREVENDO UM NOVO ARQUIVO CONTENDO A UNIÃO DAS DUAS MAQUINAS DE TURING '''

        ''' criando o arquivo Out.txt'''
        arq = open('Out.txt','w+')

        ''' escrevendo no arquivo o novo alfabeto de entrada, como resultado da união dos dois outros alfabetos de entrada'''
        ''' removendo as repetições de caracteres usados nos alfabetos de entrada'''
        for i in input_alphabet:
                if i not in input_alphabet2:
                        arq.write(i)
                        arq.write(' ')
        for i in input_alphabet2:
                arq.write(i)
                arq.write(' ')

        arq.write('\n')


        ''' escrevendo no arquivo o novo alfabeto de fita, como resultado da união dos dois outros alfabetos de fita'''
        ''' removendo as repetições de caracteres usados nos alfabetos da fita'''
        for i in tape_alphabet:
                if i not in tape_alphabet2:
                        arq.write(i)
                        arq.write(' ')
        for i in tape_alphabet2:
                if i!=' ':
                        arq.write(i)
                        arq.write(' ')

        arq.write('\n')


        ''' escrevendo no arquivo o novo espaço branco, caso os antigos espaços brancos fossem diferentes, selecionando apenas um para se 
        tornar o principal, assim modificando o outro espeço branco e suas presenças'''
        if whitespace != whitespace2:
                for i in transitions2:
                        if i[2] == whitespace2:
                                i[2] = whitespace
                        elif i[3] == whitespace2:
                                i[3] = whitespace
                whitespace2 = whitespace

        arq.write(whitespace)

        arq.write('\n')



        ''' removendo a presença do estado inicial da segunda maquina de turing por motivos de redundancia'''
        lista = list()

        for i in states2:
                if i != initial_state2:
                        lista.append(i)

        states2 = lista.copy()


        ''' substituindo a presença do estado inicial da segunda maquina de turing pelo 
        estado inicial da primeira maquina de turing, que ficou definido como padrão'''
        for i in transitions2:
                if i[0] == initial_state2:
                        i[0] = initial_state
                elif i[1] == initial_state2:
                        i[1] = initial_state

        initial_state2 = initial_state


        ''' escrevendo no arquivo os estados presentes na primeira e segunda maquina de turing'''
        for i in states:
                arq.write(i)
                arq.write(' ')

        for i in states2:
                arq.write(i)
                arq.write(' ')

        arq.write('\n')


        ''' escrevendo no arquivo o estado inicial da primeira maquina de turing, que ficou definido como unico e padrão'''
        arq.write(initial_state)

        arq.write('\n')


        ''' escrevendo no arquivo os estados finais da primeira e segunda maquina de turing'''
        for i in final_states:
                arq.write(i)
                arq.write(' ')

        for i in final_states2:
                arq.write(i)
                arq.write(' ')

        arq.write('\n')


        ''' escrevendo no arquivo a quantidade de fitas utilizadas'''
        arq.write(number_of_tapes)

        arq.write('\n')

        ''' escrevendo no arquivo as transições da primeira e segunda maquina de turing'''
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


if __name__ == "__main__":
        lerArquivo()
