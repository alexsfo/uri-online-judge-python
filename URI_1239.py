import re
texto = 'You *should* see the baby elephant at the zoo!'


result = re.search('_', texto)
if result != None:
    result = result.group(0)

if result == "_":
    texto = texto.replace('_', '<i>',1)
    texto = texto.replace('_', '</i>',1)

elif result == "*":
    texto = texto.replace('*', '<b>',1)
    texto = texto.replace('*', '</b>',1)

print(texto)
