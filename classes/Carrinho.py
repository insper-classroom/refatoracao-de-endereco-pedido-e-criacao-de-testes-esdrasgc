#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.__itens = {}

    def adicionar_item(self, item:Produto, qtd=1):
        
        id = item.id
        # Implemente a adição do item no dicionário
        if id in self.itens:
            self.itens[id] += qtd
        else:
            self.itens[id] = qtd 

    def remover_item(self, item:Produto, qtd=1):
        # Implemente este método
        id = item.id

        if id in self.itens:
            self.itens[id] -= qtd
        else:
            raise KeyError('Item não está presente no carrinho.')


    def __str__(self) -> str:
        repr = '\n'
        for id, qtd in self.itens.items():
            repr += f'{Produto.busca_por_id(id)} : {qtd}\n'
        return repr

    @property
    def itens(self):
        return self.__itens

    @itens.getter
    def itens(self):
        return self.__itens

    @itens.setter
    def itens(self, new_itens:str):
        self.__itens = new_itens