#!/usr/bin/python
# -*- coding: utf-8 -*-

'''@mod tape: móduloe que representa uma unidade de fita da turing machine'''
class Tape:
    '''
        @const: construtor do módulo que representa a classe tape (fita)
        @param whitespace: espaco em branco
        @param tape_alphabet: alfabeto da fita, do tipo lista
        @param content: conteudo da fita, do tipo lista
    '''
    def __init__(self, whitespace, tape_alphabet, content=[]):
        self.position = 0 # posicao atual da fita
        self.whitespace_symbol = whitespace
        self.alphabet = tape_alphabet
        self.content = content

    '''
        @func move_head: tem por finalidade prover as movimentações para a fita
        @param movement: movimento da fita → pode ser para esquerda (L) ou para direita (R)
    '''
    def move_head(self, movement):
        if movement == 'L': 
            self.move_left()
        elif movement == 'R':
            self.move_right()
        elif movement == 'S':
            pass

    '''
        @func move_left: tem por finalidade mover a posição da fita para a esquerda
    '''
    def move_left(self):
        if self.position > 0: # se existir espaco pra esquerda, vai para a esquerda
            self.position -= 1
        else: # se nao, coloca um branco no comeco da fita (e mantém a posição 0)
            self.content.insert(0,self.whitespace_symbol)


    '''
        @func move_right: movimenta a posição da fita para a direita
    '''
    def move_right(self): 
        if self.position < len(self.content)-1: # se tiver posicao para a direita, vai para a direita
            self.position += 1
        else: # se nao, coloca um espaco em branco na fita e vai para a direita
            whitespace = self.whitespace_symbol
            self.content.append(whitespace)
            self.position += 1

    '''
        @func get_content: retorna o conteúdo da posição atual da fita
    '''
    def get_content(self):
        if len(self.content) == 0:
             return self.whitespace_symbol
        else:
             return self.content[self.position]

    '''
        @func set_content: modifica o conteúdo da posição atual da fita
    '''    
    def set_content(self, symbol):
        if len(self.content) == 0:
            self.content.append(symbol)
        else:
            self.content[self.position] = symbol 

    def __str__(self):
        result = "(";
        result += str(self.content)
        result += ")@"
        result += str(self.position)
        return result
