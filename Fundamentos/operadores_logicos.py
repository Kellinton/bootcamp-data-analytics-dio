# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True) # true
print(True and False and True) # false
print(False and False and False) # false
print(True or True or True)  # true
print(True or False or False) # true
print(False or False or False) # false


print((saldo >= saque) and (saque <= limite)) # False
print((saldo >= saque) or (saque <= limite)) # True
print(not(1000 > 1500)) # True

# and       Operador E    && em javascript
# or        Operador OU  || em javascript
# not       Operador NOT ! em javascript

saldo = 1000
saque = 200
limite = 100
conta_especial = True

conta_normal_com_saldo_suficiente = (saldo >= saque) and (saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial) and (saldo >= saque)

resultado = (conta_normal_com_saldo_suficiente) or (conta_especial_com_saldo_suficiente)
print(resultado)