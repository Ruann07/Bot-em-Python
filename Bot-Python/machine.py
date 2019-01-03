# programador: Ruann

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

# arquivo = open('Legenda.src', 'r')
conversas = ['Oi', 'Olá', 'Tudo bem?', 'Eu estou bem', 'Qual o seu nome?', 'meu nome é Zeno, e o seu ?',
             'Ruann', 'legal', 'Fazendo o que ?', 'eu nada, e você? ', 'nada também', 'tedio né', 'um pouco']
conversa2 = ['Qual sua cor favorita ?', 'preto', 'a minha também', 'Quantos anos você tem ?', '15, 16, 17, 18, 19 20',
             'interesante', 'e você? ', 'sou bem novo']


bot.set_trainer(ListTrainer)

bot.train(conversas)
bot.train(conversa2)

while True:
    quest = input('\033[33mVocê:\033[m ')
    resposta = bot.get_response(quest)
    if float(resposta.confidence) > 0.5:
       print('\033[34mbot:\033[m', resposta)
    else:
       print('\033[034mbot:\033[m Eu não sei')
