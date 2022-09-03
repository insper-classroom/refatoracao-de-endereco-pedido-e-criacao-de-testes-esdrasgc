from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
import copy

def test_deve_ser_possivel_criar_um_pedido_ao_passar_uma_pessoaFisica_e_um_carrinho():
    pessoa = PessoaFisica('524.222.452-6','tiago@email.com','Carlos')
    carro = Carrinho()
    pedido = Pedido(pessoa, carro)

    assert isinstance(pedido, Pedido)

def test_metodo_endereco_entrega_deve_salvar_o_endereco():
    pessoa = PessoaFisica('524.222.452-6','tiago@email.com','Carlos')
    carro = Carrinho()
    pedido = Pedido(pessoa, carro)
    end = Endereco('08320330', 430)

    pedido.endereco_entrega = copy.deepcopy(end)
    assert end == pedido.endereco_entrega

def test_metodo_endereco_faturamento_deve_salvar_o_endereco():
    pessoa = PessoaFisica('524.222.452-6','tiago@email.com','Carlos')
    carro = Carrinho()
    pedido = Pedido(pessoa, carro)
    end = Endereco('08320330', 430)

    pedido.endereco_entrega = copy.deepcopy(end)
    assert end == pedido.endereco_entrega

