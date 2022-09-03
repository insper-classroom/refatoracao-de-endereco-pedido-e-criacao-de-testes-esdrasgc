#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------


class Produto:
    listagem = []

    def adicionar_produto_na_lista(novo_produto):
        Produto.listagem.append(novo_produto)

    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        Produto.adicionar_produto_na_lista(self)

    def busca_nome(nome:str):
        resultado_busca = []
        for produto in Produto.listagem:
            if nome in produto.nome:
                resultado_busca.append(produto)

        return resultado_busca

    def busca_por_id(id:str):
        for produto in Produto.listagem:
            if id == produto.id:
                return produto
        return None

    def to_dict(self):
        return {'id' : self.id, 'nome' : self.nome} 

    def __str__(self) -> str:
        return f'{self.nome}'

    def __eq__(self, other):
        if not isinstance(other, Produto):
            return False

        else:
            return (self.id == other.id and self.nome == other.nome)

    
    @property
    def nome(self):
        return self.__nome

    @nome.getter
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_name):
        self.__nome = new_name

    @property
    def id(self):
        return self.__id

    @id.getter
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id:str):
        self.__id = new_id

