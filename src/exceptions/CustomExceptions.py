class Error(Exception):
    """Classe base para outras exceptions"""
    pass


class ErroNaoMapeado(Error):
    """ Ocorre quando um erro no projeto não está definido """
    pass


class JanelaComProblema(Error):
    """ Ocorre quando tenta interagir com alguma janela e ela não responde devidamente """
    pass


class EstadoPosteriorNaoAlcancado(Error):
    """ Ocorre quando a verificação do estado da aplicação após executada não está comforme o mapeado """
    pass
