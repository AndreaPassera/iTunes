from model.model import Model

mymodel=Model()
mymodel.buildGraph(120)
n,e=mymodel.getGraphDetails()
print(f"Numero nodi: {n}, numero archi: {e}")

