#!/usr/bin/python
# -*- coding: utf-8 -*-

from instance  import instance
import copy
''' @mod turing_machine: módulo que representa uma turing machine '''
class turing_machine:
    '''
        @const: construtor do módulo (classe) turing machine
        @param states: lista de estados
        @param final_states: lista de estados de aceitacao
        @param initial_state: estado inicial
        @param transitions: lista de transicoes
        @param whitespace: simbolo que representa o branco
        @param tape_list: lista de fitas da turing machine
    '''
    def __init__(self,states, final_states, initial_state, transitions, whitespace, tape_list):
        '''
            @var self.instances: é uma lista de instâncias de turing machine, que é iniciada com apenas 
            uma instância que usa os estados de aceitação e a lista de fitas da entrada
        '''
        self.instances = [instance(initial_state, tape_list)]
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.whitespace = whitespace
    
    
    '''
        @func run: Executa toda a computação necessária para máquina de turing ser processada
    '''
    def run(self):      
        # Laço de repeticao que executa enquanto existir instancias de maquina de turing
        while self.instances:
            instance = self.instances.pop(0)

            # Verifica aceitacao por estado final
            for final_state in self.final_states:
                # Se o estado atual é igual ao estado final
                if instance.current_state == final_state:
                    return [1, instance]

            # stepResult recebe a lista de transições válidas
            validtransitions = instance.step(self.transitions)
            for transition in validtransitions:
                newinstance = instance.doTransition(transition)
                self.instances.append(newinstance)

        return [0, None]
