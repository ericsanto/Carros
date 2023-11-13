import openai


def get_car_ai_description(model, brand, year):
  prompt = ''''
      Gere uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas do modelo
    '''
  openai.api_key = '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'
  prompt = prompt.format(brand, model, year)
  response = openai.completions.create(
      model='text-davinci-003',
      prompt=prompt,
      max_tokens=1000,
  )
  # Retorna o texto da primeira escolha no objeto de resposta
  return response['choices'][0]['text']