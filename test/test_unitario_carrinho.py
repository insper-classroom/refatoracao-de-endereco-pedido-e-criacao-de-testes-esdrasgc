from classes.Carrinho import Carrinho
from classes.Produto import Produto

def test_deve_ser_possivel_criar_um_carrinho_sem_passar_argumentos_no_construtor():
    carro = Carrinho()
    assert isinstance(carro, Carrinho)

def test_deve_ser_possivel_adicionar_itens_ao_carrinho_por_meio_do_metodo_adicionar_item():
    carro = Carrinho()
    sabonete = Produto("0010342967", "Sabonete")
    carro.adicionar_item(sabonete)
    assert 'Sabonete : 1' in str(carro)

