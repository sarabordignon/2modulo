from fastapi import FastAPI 

#cria a aplicação
app = FastAPI()

#rota inicial e quando acessar / recebe a mensagem
@app.get("/")
def leitura_rota():
    return {"mensagem: " "Primeira rota rodando!"}

#rota que exibe informações fixas
@app.get("/sobre")
def sobre():
    return {"nome: " "Sara" " | " "curso: " "Jovem Programador"} 

#rota com parametro informado na url
@app.get("/sobre/{nome}")
def sobrePersonalizado(nome: str):
    return {"mensagem: " f"Olá, {nome}! Bem vindo(a) ao Jovem Programador!"}