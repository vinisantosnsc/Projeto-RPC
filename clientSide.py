import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
# Imprime lista de métodos disponíveis
print(str(s.system.listMethods()) + "\n")

print(s.cToF(24) + "\n")

x=20
y=10
print(s.soma(x,y) + "\n")
print(s.subt(x,y) + "\n")
print(s.mult(x,y) + "\n")
print(s.divi(x,y) + "\n")
