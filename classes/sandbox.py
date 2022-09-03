
@property
def itens(self):
    return self.__itens

@itens.getter
def itens(self):
    return self.__itens

@itens.setter
def itens(self, new_itens:str):
    self.__itens = new_itens