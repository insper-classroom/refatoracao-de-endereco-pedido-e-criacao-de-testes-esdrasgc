from classes.Endereco import Endereco
import pytest
import pytest_network

@pytest.mark.exercicio_2
@pytest.mark.endereco
def test_endereco_deve_ser_criado_ao_receber_CEP_e_numero():
    
    end = Endereco('04552040', 265)
    assert isinstance(end, Endereco)

### https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions

@pytest.mark.exercicio_2
@pytest.mark.endereco
def test_endereco_nao_deve_ser_criado_ao_receber_somente_CEP():
    with pytest.raises(TypeError) as excmessage:
        end = Endereco('04552040')
    assert "missing 1 required positional argument: 'numero'" in str(excmessage.value)


def test_endereco_nao_deve_ser_criado_ao_receber_somente_numero():
    with pytest.raises(TypeError) as excmessage:
        end = Endereco(numero = 265)
    assert "missing 1 required positional argument: 'cep'" in str(excmessage.value)


def test_metodo_consultar_cep_deve_retornar_os_dados_ao_receber_cep_como_string():
    end_dict = Endereco.consultar_cep(cep ='04552040')
    # return end_dict
    ## https://appdividend.com/2022/05/30/python-list-contains/#:~:text=To%20check%20if%20the%20list%20contains%20an%20element%20in%20Python,or%20not%20using%20the%20list.
    List1 = list(end_dict.keys())
    List2 = ['logradouro', 'localidade', 'uf']
    check = all(item in List1 for item in List2)
    assert check

def test_metodo_consultar_cep_deve_retornar_os_dados_ao_receber_cep_como_int():
    end_dict = Endereco.consultar_cep(cep = 55296630)
    List1 = list(end_dict.keys())
    List2 = ['logradouro', 'localidade', 'uf']
    check = all(item in List1 for item in List2)
    assert check

def test_metodo_consultar_cep_deve_falhar_ao_receber_cep_como_float():
    # with pytest.raises(TypeError):
    end_dict = Endereco.consultar_cep(cep = 55296630.0)
    assert False == end_dict

@pytest.mark.exercicio_2
@pytest.mark.endereco
def test_endereco_deve_ser_criado_ao_receber_todas_as_info():
    
    end = Endereco(cep = '04552040', numero= 265, rua = 'Rua Elvira Ferraz', cidade='São Paulo', complemento= 'Toca da Raposa, qaurto 3')
    assert isinstance(end, Endereco)


def test_metodo_consultar_cep_deve_falhar_ao_receber_cep_com_quantidade_de_digitos_diferente_maior_que_8():
    # with pytest.raises(TypeError):
        end_dict = Endereco.consultar_cep(cep = 552966300)
        assert False == end_dict

def test_metodo_consultar_cep_deve_falhar_ao_receber_cep_com_quantidade_de_digitos_diferente_menor_que_8():
    # with pytest.raises(TypeError):
        end_dict = Endereco.consultar_cep(cep = 5529663)
        assert False == end_dict


def test_metodo_consultar_cep_deve_falhar_ao_receber_cep_inexistente():
    # with pytest.raises(TypeError):
        end_dict = Endereco.consultar_cep(cep = '04552041')
        assert False == end_dict

@pytest.mark.falha_internet
def test_metodo_consultar_cep_deve_apresentar_erro_caso_haja_falha_de_internet():
    with pytest.raises(ConnectionError) as excemessage:
        end_dict = Endereco.consultar_cep(cep = '04552040')

    assert 'Não foi possível conectar com a aplicação. Por favor verifique a conexão com a internet.' in str(excemessage.value)