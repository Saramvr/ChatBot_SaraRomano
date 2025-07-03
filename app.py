import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    #if comando in ('olá', 'boa tarde', 'bom dia'):
    #    return 'Olá tudo bem!'
    #if comando == 'como estás':
     #   return 'Estou bem, obrigado!'
    #if comando == 'como te chamas?':
     #   return 'O meu nome é: Bot :)'
    #if comando == 'tempo':
     #   return 'Está um dia de sol!'
    #if comando in ('bye', 'adeus', 'tchau'):
     #   return 'Gostei de falar contigo! Até breve...'
    #if 'horas' in comando:
     #   return f'São: {datetime.now():%H:%M} horas'
    #if 'data' in comando:
     #   return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    #return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas?': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        'qual é a tua cor favorita?': 'Gosto muito de azul!',
        'qual é a tua comida preferida?': 'A minha comida favorita é pizza!',
        'quantos anos tens?': 'Sou novo... fui criado há pouco!',
        'estás aí': 'Sempre presente!',
        'gostas de mim': 'Claro que sim! Adoro conversar contigo.',
        'o que sabes fazer?': 'Posso responder a perguntas simples e fazer-te companhia!',
        'o que mais gostas de fazer?': 'Responder às tuas perguntas!',
        ''
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
    }

    


    
    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! "{texto}"'

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}!\nComo te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')

def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()

if __name__ == '__main__':
    main()