import asyncio
#corrotina assincrona
async def tarefa(nome, duracao):
    print(f"tarefa[{nome}] iniciando...")
    await asyncio.sleep(duracao)
    print(f"tarefa[{nome}] terminou...")
    
#processo assincrono
async def main():
    await asyncio.gather(
        tarefa (1, 3),
        tarefa (2 ,6)
    )
    await tarefa(3, 4)
    
# Processo sincrono

'''async def main():
    await tarefa (1,3)    #saida tarefa[1] iniciando...tarefa[1] terminou...
    await tarefa (2,3)''' #saida tarefa[1] iniciando...tarefa[1] terminou...

if __name__=="__main__":
    asyncio.run(main())