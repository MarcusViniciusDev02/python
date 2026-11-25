# Listas
# São mutáveis.
# Aceita qualquer tipo de dados.

# empty_list = []  # ou list();
# my_list = ['Categories', 'Wall', 'Floor', 'Roof', 'Ceiling', 'Wall', 'Floor', 'Roof', 'Ceiling']

# print(my_list)
# print(my_list[2]) # Imprime apenas um elemento.
# print(my_list[-3]) # Imprime ao inverso.

# print(my_list[:2]) # Imprime até o indice 2
# print(my_list[2:]) # Imprime depois do indice 2
# print(my_list[1:3])# Imprime do 1 ao 2.
# print(my_list[::2])# Cada segundo item será impresso.
# print(my_list[2:6:2]) # Imprime de 2 em 2 até o sexto item.
# print(my_list[::-1]) # imprime de 1 em 1 ao inverso. (Inverte a lista)

# print(my_list[0]) - header
# print(my_list[1:]) - itens
#
# print('Wall' in my_list) - verifica se o item está na lista.
# print('Door' not in my_list) - verifica se o item não está na lista.

# print()
# type() # imprime o tipo do item


# print(len(my_list)) # Imprime o tamanho da lista.
# print(sorted(my_list)) # Imprime em ordem.

# numbers = [10, 20, 30, 40, 50]
#
# print(sum(numbers)) # Soma todos os itens da lista.
# print(min(numbers)) # Captura o menor valor da lista.
# print(max(numbers)) # Captura o maior valor da lista.

# Metodos da lista.
#-------------------------------------------------------
# listAbc = [40, 35, 12]
# list = [1, 2, 3, 3, 4, 5]
# list[2] = 11111 #Item do índice 2 passa a ser o valor inserido.
# list.append(11) # adiciona um item a lista.
# list.append(24)
# list.extend(listAbc) #Junta duas listas.
# list.sort() # Imprime em ordem.
# quantasVezes = list.count(3) #Imprime quantas vezes o elemento aparece na lista.
# list.index(2) # busca em qual índice está o elemento.
# list.insert(2, 33)# insere o elemento em um índice indicado.
# list.remove(2) # remove o item da lista a partir do valor.
# list.pop() #Remove e retorna o índice da lista.
# list.reverse()# Inverte a lista.
# list.clear() #Remove todos os elementos da lista.
# list = [] # Também remove todos os elementos da lista. (Melhor forma)
# copia = list.copy() # Cria uma cópia independente de uma lista.
# list.append(2222)

# x = list #Faz uma referencia a lista.
# y= copia #Está pegando a cópia.

# print(x)
# print(y)

#Tupla - Não podem ser modificadas
# data = (0,1,2,3,4,5,0,1,2,3,4,5)
#
# #Principais funções
# print(len(data))
# print(min(data))# valor minimoe
# print(max(data))# valor máximo
# print(sum(data))# soma numeros
# print(sorted(data))#cria lista em ordem.
# print(tuple(sorted(data)))#converte a lista para tupla
