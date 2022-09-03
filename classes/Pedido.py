#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re


class Pedido:
    EM_ABERTO = 1
    PAGO = 2
    
    
    def __init__(self, user:PessoaFisica = None, carrinho:Carrinho = None):
        self.__user = user
        self.__carrinho = carrinho
        self.__endereco_entrega = None
        self.__endereco_faturamento = None
        self.__status = Pedido.EM_ABERTO


    def __eq__(self, other):
        if not isinstance(other, Pedido):
            return False
        else:
            return (self.user == other.user and self.carrinho == other.carrinho and self.endereco_entrega == other.endereco_entrega and self.endereco_faturamento == other.endereco_faturamento and self.status == other.status)

    def __str__(self) -> str:
        repr = f'Detalhes do Pedido\nNome do usuário: {self.__user.nome}\nEndereço de entrega: {self.endereco_entrega}\nEndereço de faturamento: {self.endereco_faturamento}\nLista de produtos: {self.__carrinho}'
        return repr

    @property
    def endereco_entrega(self):
        return self.__endereco_entrega

    @endereco_entrega.getter
    def endereco_entrega(self):
        return self.__endereco_entrega

    @endereco_entrega.setter
    def endereco_entrega(self, end:Endereco):
        self.__endereco_entrega = end

    @property
    def endereco_faturamento(self):
        return self.__endereco_faturamento

    @endereco_faturamento.getter
    def endereco_faturamento(self):
        return self.__endereco_faturamento

    @endereco_faturamento.setter
    def endereco_faturamento(self, end:Endereco):
        self.__endereco_faturamento = end

    @property
    def user(self):
        return self.__user

    @user.getter
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_user:str):
        self.__user = new_user

    @property
    def carrinho(self):
        return self.__carrinho

    @carrinho.getter
    def carrinho(self):
        return self.__carrinho

    @carrinho.setter
    def carrinho(self, new_carrinho:str):
        self.__carrinho = new_carrinho

    @property
    def status(self):
        return self.__status

    @status.getter
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status:str):
        self.__status = new_status