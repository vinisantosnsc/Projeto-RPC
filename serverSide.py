from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restringir a um determinado caminho.

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Cria servidor
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Registra uma função com um nome diferente
    def celciusParaFahrenheit(c):
        f = ((9/5)*c)+32
        return "{0}°C equivale a {1}°F".format(c, f)

    server.register_function(celciusParaFahrenheit, 'cToF')

    # Registra uma instância; todos os métodos da instância são
    # publicado como métodos XML-RPC (neste caso:'soma', 'subt', 'mult' e 'divi').
    class Calculadora:
        def soma(self, a, b):
            resultado = a + b
            return "A soma entre {0} e {1} é igual a {2}".format(a, b, resultado)

        def subt(self, a, b):
            resultado = a - b
            return "A subtração entre {0} e {1} é igual a {2}".format(a, b, resultado)

        def mult(self, a, b):
            resultado = a * b
            return "A multiplicação entre {0} e {1} é igual a {2}".format(a, b, resultado)

        def divi(self, a, b):
            resultado = a / b
            return "A divisão entre {0} e {1} é igual a {2}".format(a, b, resultado)

    server.register_instance(Calculadora())

    # Executa o loop principal do servidor
    server.serve_forever()
