from pydantic import BaseModel

# Isso é um Modelo Pydantic
class Usuario(BaseModel):
    nome: str
    idade: int
    email: str
    ativo: bool = True

try:
   usuario = Usuario(nome="Rafa", idade="30", email="usuario@gmail.com") 
   print(usuario.idade)
   print(type(usuario.idade))
   print(usuario.email)
except Exception as e:
    print("erro de validacao")
    print(e)