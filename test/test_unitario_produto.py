
from ast import Assert
from classes.Produto import Produto


def test_deve_ser_criado_o_produto_ao_passar_o_codigo_e_nome():
    produto = Produto("0010342967", "Sabonete")

    assert isinstance(produto, Produto)

def test_metodo_busca_nome_deve_retornar_o_produto_cujo_nome_for_passado():
    produto1 = Produto("0010342967", "Sabonete")
    produto2 = Produto("0010342968", "Copo")
    produto3 = Produto("0010342969", "Talheres")

    produto = Produto.busca_nome('Co')[0]

    assert produto2 == produto

def test_busca_por_id_deve_retornar_o_produto_cujo_id_corresponde_ao_que_foi_passado():
    produto1 = Produto("0010342967", "Sabonete")
    produto2 = Produto("0010342968", "Copo")
    produto3 = Produto("0010342969", "Talheres")

    produto = Produto.busca_por_id("0010342968")

    assert produto2 == produto