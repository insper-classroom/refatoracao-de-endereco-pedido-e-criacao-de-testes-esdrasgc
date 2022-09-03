from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
import pytest

def test_pessoa_fisica_deve_ser_criada_ao_receber_nome_email_e_cpf():
    pessoa = PessoaFisica('74454358400', 'test@gmail.com', 'Gerôncio')
    assert isinstance(pessoa, PessoaFisica)

def test_metodo_busca_nome_deve_retornar_a_pessoa_cujo_nome_for_passado_como_argumento():
    pessoa1 = PessoaFisica('74454358400', 'test@gmail.com', 'Gerôncio')
    pessoa2 = PessoaFisica('12345678974', 'tested@gmail.com', 'Carlos')
    pessoa3 = PessoaFisica('08053944434', 'tested@gmail.com', 'Estrôncio')

    busca = PessoaFisica.busca_nome('Carlos')[0]

    assert pessoa2 == busca

def test_metodo_adicionar_endereco_deve_salvar_o_endereco_e_o_apelido_caso_sejam_passados_uma_str_e_um_endereco():
    pessoa = PessoaFisica('74454358400', 'test@gmail.com', 'Gerôncio')
    end =  Endereco(cep = '04552040', numero = 265)
    pessoa.adicionar_endereco('casa', end)
    assert end == pessoa.get_endereco('casa')

def test_metodo_remover_endereco_deve_remover_o_endereco_correspondente_a_str_apelido_do_endereco_que_foi_passada():
    pessoa = PessoaFisica('74454358400', 'test@gmail.com', 'Gerôncio')
    end =  Endereco(cep = '04552040', numero = 265)
    pessoa.adicionar_endereco('casa', end)
    pessoa.remover_endereco('casa')
    assert 0 == len(pessoa.listar_enderecos())


def test_metodo_listar_endereco_deve_apresentar_a_lista_com_os_enderecos_adicionados():
    pessoa = PessoaFisica('74454358400', 'test@gmail.com', 'Gerôncio')
    end1 =  Endereco(cep = '04552040', numero = 265)
    end2 = Endereco('04546042', 300)
    end3 = Endereco('08320330', 430)

    pessoa.adicionar_endereco('casa', end1)
    pessoa.adicionar_endereco('facul', end2)
    pessoa.adicionar_endereco('job', end3)

    mensagem = 'casa: Rua Elvira Ferraz, 265'

    assert mensagem in str(pessoa.listar_enderecos())



