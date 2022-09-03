#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    listagem = []
    def adicionar_pessoa_na_lista(nova_pessoa):
        PessoaFisica.listagem.append(nova_pessoa)

    def __init__(self, cpf, email, nome='Visitante'):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__enderecos = {}
        PessoaFisica.adicionar_pessoa_na_lista(self)

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.enderecos[apelido_endereco] = end

    def remover_endereco(self, apelido_endereco):
        del self.enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        return self.enderecos[apelido_endereco]

    def listar_enderecos(self):
        enderecos = []
        for key, value in self.__enderecos.items():
            enderecos.append(str(key + ': ' + str(value)))
        return enderecos

    def busca_nome(nome:str):
        resultado_busca = []
        for pessoa in PessoaFisica.listagem:
            if nome == pessoa.nome:
                resultado_busca.append(pessoa)
        return resultado_busca

    

    def __eq__(self, other):
        ## https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes
        if not isinstance(other, PessoaFisica):
            # don't attempt to compare against unrelated types
            return False

        return (self.nome == other.nome and self.email == other.email and self.cpf == other.cpf and self.enderecos == other.enderecos)

        
    def __str__(self) -> str:
        return f'Nome: {self.nome}, email: {self.email}, cpf: {self.cpf}, enderecos: {self.enderecos}'

    
    @property
    def nome(self):
        return self.__nome

    @nome.getter
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_name:str):
        self.__nome = new_name

    @property
    def email(self):
        return self.__email

    @email.getter
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email:str):
        self.__email = new_email

    @property
    def cpf(self):
        return self.__cpf

    @cpf.getter
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, new_cpf:str):
        self.__cpf = new_cpf

    @property
    def enderecos(self):
        return self.__enderecos

    @enderecos.getter
    def enderecos(self):
        return self.__enderecos

    @enderecos.setter
    def enderecos(self, new_end:str):
        self.__enderecos = new_end

# pessoa1 = PessoaFisica('74454358400', 'test@gmail.com', 'Gerôncio')
# pessoa2 = PessoaFisica('12345678974', 'tested@gmail.com', 'Carlos')
# pessoa3 = PessoaFisica('08053944434', 'tested@gmail.com', 'Estrôncio')

# print(pessoa2 == PessoaFisica.busca_nome('Carlos')[0])