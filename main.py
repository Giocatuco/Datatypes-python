'''
Text Type (String)
'''
# s="isto e um string de linha simples"
# z=s+"catalogada"
# print(s)
# print(z)

# ====================================

# s1='''Isto e um string de multipla
# linha'''

# print(s1)
# ===================================
# Encontrar um caracter pelo index
# s="eu sou alto"
# print (s[4])

# Encontrar segmentos, de... ate "slicing"
# s="eu sou alto"
# print (s[4:])

# Mutar posicoes/ strings sao imutaveis
# s="eu sou alto"
# s[2] = 'o'
# print (s)





# ====================================
'''
 Numeric Type (int,float,complex)
'''
#Integer para numeros inteiros, float numeros decimais, complex 

# i=4+2j
# x=20-4
# y=x-0.10
# print(x)
# print(y)
# print(type(x))
# print (type(y))
# print (type(i))

# ===============
'''
sequence Type (List,Tuple,Range)
'''
# Lista

# x=[8,9,6,'ola']
# print(x[3])
# mutar uma listar/alterar um elemento da lista
# x[2] = 'python'
# print (x)

# Tuple


# tuple = ("cat", [4,3,2], (1,2,3))
# print(tuple[2])

# both of examples below are type tuples, without comma makes it a string.
# tuple = ("hello")
# tuple = "hello",
# print(type(tuple))

# Tuple nao e mutavel


# Range serve para gerar numeros

# x=range(10)
# for n in x:
#  print (n)

'''
Mapping Type (Dictionary)
'''
# dict = {}
# print(type(dict))

# ========================
# O dicionario pode ser mutavel
# dict = {"Nome":"Geovany", "Idade":29}
# print (dict["Nome"])
# print (dict.get("Idade"))

# dict["Idade"] = 25
# print (dict)

# dict["Age"] = 22
# print (dict)

'''
Set Types
'''
# Set so usa um valor em cada posicao 
# Set vazio assim set={} fica dicionario vazio
# set = set()

# print (type(set))

# =========================================
# Set tem tipos de dados misturados, todos imutaveis
# set nao suporta index, busca por posicao
# tipo de erro: TypeError: 'set' object is not subscriptable
# set nao pode conter elementos duplicados
# Bom para usar em projetos que necessitam de usar dados unicos, que nao se repetem

# set = {3.2,"oi",(1,2,3)}
# print(type(set))
# print (set[0])

# set = {3.2,"oi",(1,2,3),[1,2,3,4,]}
# print(set)

# set nao pode conter uma lista
# tipo de erro: unhashable type: 'list'

# =======================================


'''
Boolean Type (True or false)
'''
# Tipo de dados usado para sim ou nao

# print(type(True))

# boolean as numbers
# print(True == 1)
# print(False == 0)
# print (False == 2)

# interesting logic
# print (True + True + True)

# not boolean operators
# print(not True)
# print(not False)

# and boolean operator
# true and false sempre sera falso, true and true sempre sera true
# false and false sera falso

# print (True and False)
# print (True and True)
# print (False and False)

# or boolean operator
# true or false sera true, true or true sera true, false or false sempre sera false
# print(True or False)
# print(True or True)
# print(False or False)