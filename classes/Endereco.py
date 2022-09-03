#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

import requests
import json


class Endereco: 
    '''
    Endereço de uma pessoa ou conta.
    Esta classe possui overload de Contrutor, caso envie apenas três parametros será encaminhado
    para o contrutor que consulta o cep para encontrar o endereço.
    '''

    def __init__(self, cep, numero ,rua='', estado='', cidade='', complemento=''):

        if (rua == '') or (estado == '') or (cidade == ''):
            end_json = Endereco.consultar_cep(cep)

            self.__rua = end_json['logradouro']
            self.__estado = end_json['uf']
            self.__cidade = end_json['localidade']
            self.__numero = numero
            self.__complemento = complemento
            self.__cep = str(cep)

        else:

            self.__rua = rua
            self.__estado = estado
            self.__cidade = cidade
            self.__numero = int(numero)
            self.__complemento = complemento
            self.__cep = str(cep)

    def __eq__(self, other):
        if not isinstance(other, Endereco):
            return False
        else:
            return (self.rua == other.rua and self.cidade == other.cidade and self.cep == other.cep and self.estado == other.estado and self.numero == other.numero)

    def __str__(self) -> str:

        mensagem = f'{self.rua}, {self.numero}. {self.complemento}. {self.cidade}-{self.estado}. {self.cep}.'
        return mensagem

    def consultar_cep(cep):
        '''
        Metodo realiza a consulta do cep em uma api publica para obter informações
        como estado, cidade e rua
        '''
        # continuam existindo variaveis locais, nem tudo é propriedade de objeto
        if ( not((isinstance(cep, int)) or (isinstance(cep, str))) ) or ( len(str(cep)) != 8):
            return False
        # end point da API de consulta ao cep
        url_api = f'https://viacep.com.br/ws/{str(cep)}/json/'

        # Sem corpo na requisição
        # Não é necessario nenhum cabeçalho HTTP especial
        payload = {}
        headers = {}

        # requisição GET na url de pesquisa do cep. Doc.: https://viacep.com.br/
        try:
            response = requests.request("GET", url_api, headers=headers, data=payload)
        except requests.exceptions.ConnectionError:
            raise ConnectionError('Não foi possível conectar com a aplicação. Por favor verifique a conexão com a internet.')
        # converte a resposta json em dict
        json_resp = response.json()
        print(json_resp)
        if 'erro' in json_resp:
            return False
        return json_resp


    @property
    def rua(self):
        return self.__rua

    @rua.getter
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, new_rua:str):
        self.__rua = new_rua


    @property
    def cep(self):
        return self.__cep

    @cep.getter
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, new_cep:str):
        self.__cep = new_cep


    @property
    def numero(self):
        return self.__numero

    @numero.getter
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, new_numero:str):
        self.__numero = new_numero


    @property
    def complemento(self):
        return self.__complemento

    @complemento.getter
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, new_complemento:str):
        self.__complemento = new_complemento


    @property
    def estado(self):
        return self.__estado

    @estado.getter
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, new_estado:str):
        self.__estado = new_estado


    @property
    def cidade(self):
        return self.__cidade

    @cidade.getter
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, new_cidade:str):
        self.__cidade = new_cidade