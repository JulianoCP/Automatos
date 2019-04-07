from turing_machine import turing_machine # representa a turing machine
from tape import Tape # representa uma unidade de fita
import sys


class Unido:
        def __init__(self):
                self.input_alphabet = list()
                self.tape_alphabet =  list()
                self.whitespace = list()
                self.states =  list()
                self.initial_state =  list()
                self.final_states =  list()
                self.number_of_tapes = list()
                self.transitions =  list()

        def abreArq(self,arquivo):
                fp = open(arquivo, "r") #abre em modo de leitura o arquivo com a definicao da maquina de turing
                lines_cmd = fp.readlines()
                lines = []
                for line in lines_cmd:
                        lines.append(line.rstrip())
                number_of_lines  = len(lines)
                '''valores de entrada que representam a turing machine de entrada'''
                self.input_alphabet   = lines[0].split()
                self.tape_alphabet    = lines[1].split()
                self.whitespace       = lines[2]
                self.states           = lines[3].split()
                self.initial_state    = lines[4]
                self.final_states     = lines[5].split()
                self.number_of_tapes  = lines[6]
                self.transitions      = []
                self.addTrans(number_of_lines,lines)
                

        def addTrans(self,qntlinhas,lines):
                for i in range(7, qntlinhas):
                        self.transitions.append(lines[i].split())


        def estadoDeCada(self,digito):
                lista = list()
                for i in self.states:
                        i = digito+i
                        lista.append(i)
                self.states = lista.copy()
                lista.clear()

        def novoInitial(self,digito):
                self.initial_state = digito + self.initial_state

        def novoFinal(self,digito):
                lista = list()
                for i in self.final_states:
                        i = digito+i
                        lista.append(i)
                self.final_states = lista.copy()
                lista.clear()
        
        def transicaoModificada(self,digito):
                for t in self.transitions:
                        t[0] = digito +t[0]
                        t[1] = digito +t[1]

        def estados(self,arq):
                for i in self.states:
                        arq.write(i)
                        if(self.states.index(i)< (len(self.states)-1)):
                                arq.write(' ')
                

        def aceitacao(self,arq):
                for i in self.final_states:
                        arq.write(i)
                        if(self.final_states.index(i)< (len(self.final_states)-1)):
                                arq.write(' ')
                

        def escreveTrans(self,arq):
                for i in self.transitions:
                        for j in i:
                                arq.write(j) 
                                if(i.index(j)< (len(i)-1)):
                                        arq.write(' ')
                        arq.write('\n')
        
        def uniInput(self,objeto2,arq):
                y=list(set().union(set(self.input_alphabet),set(objeto2.input_alphabet)))
                for i in y:
                        arq.write(i)
                        if(y.index(i)< (len(y)-1)):
                                arq.write(' ')
        
        def uniTape(self,objeto2,arq):
                w = list(set().union(set(self.tape_alphabet),set(objeto2.tape_alphabet)))
                for i in w:
                        arq.write(i)
                        if(w.index(i)< (len(w)-1)):
                                arq.write(' ')
        
        def newBranco(self,objeto2,arq):
                if self.whitespace != objeto2.whitespace:
                        for i in objeto2.transitions:
                                if i[2] == objeto2.whitespace:
                                        i[2] = self.whitespace
                                elif i[3] == objeto2.whitespace:
                                        i[3] = self.whitespace
                        objeto2.whitespace2 = self.whitespace

                arq.write(self.whitespace)

        def noDuplicateInitial(self):
                lista = list()
                for i in self.states:
                        if i != self.initial_state:
                                lista.append(i)

                self.states = lista.copy()
                lista.clear()

        def standardInitial(self,objeto1):
                for i in self.transitions:
                        if i[0] == self.initial_state:
                                i[0] = objeto1.initial_state
                        elif i[1] == self.initial_state:
                                i[1] = objeto1.initial_state

                self.initial_state = objeto1.initial_state
                
        def only1Initial(self,objeto1):
                for i in self.transitions:
                        if i[0] == self.initial_state:
                                i[0] = objeto1.initial_state
                        if i[1] == self.initial_state:
                                i[1] = objeto1.initial_state

#######################################################################################

def lerArquivo(objeto1, objeto2):
        '''ABRINDO, LENDO E RECEBENDO OS DADOS DO ARQUIVO .TXT DAS DUAS MAQUINAS DE TURING'''
        
        objeto1.abreArq(sys.argv[1])
        objeto2.abreArq(sys.argv[2])
      
        
        transformacao(objeto1,objeto2)


#################################################################################


def transformacao(objeto1,objeto2):
        '''MANIPULANDO AS VARIAVEIS QUE ARMAZENAM OS DADOS DAS MAQUINAS DE TURING'''
        
        ''' adicionado o digito referente na frente dos nomes dos estados da cada Maquina de Turing'''
        objeto1.estadoDeCada('1')
        objeto2.estadoDeCada('2')


        ''' adicionando o digito referente na frente do nome do estado inicial de cada Maquina de Turing'''
        objeto1.novoInitial('1')
        objeto2.novoInitial('2')


        ''' adicionando o digito referente na frente do nome de cada estado final de cada Maquina de Turing'''
        objeto1.novoFinal('1')
        objeto2.novoFinal('2')

        ''' adicionando o digito referente na frene dos estados usados em cada transição dentre a todas transições possiveis para cada Maquina de Turing'''
        objeto1.transicaoModificada('1')
        objeto2.transicaoModificada('2')
        

        ''' substituindo as aparições do estado inicial da inicial da segunda Maquina de Turing pelo estado inicial da primeira Maquina de Turing'''
        objeto2.only1Initial(objeto1)
        
        escrevendoUniao(objeto1,objeto2)


##################################################################################################


def escrevendoUniao(objeto1,objeto2):
        ''' ABRINDO E ESCREVENDO UM NOVO ARQUIVO CONTENDO A UNIÃO DAS DUAS MAQUINAS DE TURING '''

        ''' criando o arquivo Out.txt'''
        arq = open('Out.txt','w+')


        ''' escrevendo no arquivo o novo alfabeto de entrada, como resultado da união dos dois outros alfabetos de entrada'''
        objeto1.uniInput(objeto2,arq)
        arq.write('\n')


        ''' escrevendo no arquivo o novo alfabeto de fita, como resultado da união dos dois outros alfabetos de fita'''
        objeto1.uniTape(objeto2,arq)
        arq.write('\n')

        
        ''' escrevendo no arquivo o novo espaço branco, caso os antigos espaços brancos fossem diferentes, selecionando apenas um para se 
        tornar o principal, assim modificando o outro espeço branco e suas presenças'''
        objeto1.newBranco(objeto2,arq)
        arq.write('\n')



        ''' removendo a presença do estado inicial da segunda Maquina de Turing por motivos de redundancia'''
        objeto2.noDuplicateInitial()


        ''' substituindo a presença do estado inicial da segunda Maquina de Turing pelo 
        estado inicial da primeira Maquina de Turing, que ficou definido como padrão'''
        objeto2.standardInitial(objeto1)


        ''' escrevendo no arquivo os estados da união da primeira e segunda Maquina de Turing'''
        objeto1.estados(arq)
        arq.write(' ')
        objeto2.estados(arq)
        arq.write('\n')


        ''' escrevendo no arquivo o estado inicial da primeira Maquina de Turing, que ficou definido como unico e padrão'''
        arq.write(objeto1.initial_state)
        arq.write('\n')


        ''' escrevendo no arquivo os estados finais da união da primeira e segunda Maquina de Turing'''
        objeto1.aceitacao(arq)
        arq.write(' ')
        objeto2.aceitacao(arq)
        arq.write('\n')

        
        ''' escrevendo no arquivo a quantidade de fitas utilizadas'''
        arq.write(objeto1.number_of_tapes)
        arq.write('\n')


        ''' escrevendo no arquivo as transições da união da primeira e segunda Maquina de Turing'''
        objeto1.escreveTrans(arq)
        objeto2.escreveTrans(arq)
      
        arq.close()


if __name__ == "__main__":
        primeiro = Unido()
        segundo = Unido()
        lerArquivo(primeiro,segundo)
