##Etapa de extração:
import pandas as pd
extracao = pd.read_csv('pokemon.csv')
usuario = extracao['nome'].tolist()
favorito = extracao['pokemonfavorito'].tolist()
print (usuario,favorito)
for e, i in enumerate(usuario):
  print (f"Crie uma mensagem para {usuario[e]} sobre seu pokémon favorito {favorito[e]}.")
mensagem = []
##Transformação: 
import openai
api_key = 'API_KEY'
openai.api_key = api_key
def generate_ai_news(usuario):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
          "role": "system",
          "content": "Você é um professor pokémon."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {usuario[e]} sobre seu pokémon favorito {favorito[e]}. Máximo de 200 caracteres."
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"')
for e, i in enumerate(usuario):
  mensagens = generate_ai_news(usuario)
  print (mensagens)
  mensagem.append(mensagens)
##Load no arquivo CSV criado previamente.
for e, i in enumerate(usuario):
  extracao.loc [[e], 'mensagem'] = mensagem[e]
  extracao.to_csv("pokemon.csv", index=False)
  print(f"Mensagem do usuário {usuario[e]} alterada! {mensagem[e]}")
print (extracao)