import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

class Usuario(BaseModel):
    nome: str
    idade: int
    email: str
    ativo: bool = True

@app.get("/saudar/{nome}")
async def saudar(nome:str):
    print(type(nome))
    return{"mensagem": f"Olá, {nome}"}


@app.post("/usuarios")
async def criar_usuario(usuario: Usuario):
    return{
        "mensagem":"Usuario criado com sucesso!",
        "dados": dict(usuario)
    }
@app.get("/usuarios")
async def listar_usuario(usuario: Usuario):
    return{
        
        "dados": dict(usuario)
    }

   
if __name__ == "__main__":
 uvicorn.run(
    "app:app",  
    host = "127.0.0.1",
    port =3001,
    reload=True
)    

