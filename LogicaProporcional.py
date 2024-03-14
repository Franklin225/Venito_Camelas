import ttg

proposiciones = ['p', 'q', 'r']


expresionLogica = ['p implies q', 'not q', 'not q and r', '(p implies q) or (not q and r)', 'r implies q', 'p implies q', '((p implies q) or (not q and r)) implies (r implies q)']

tablita = ttg.Truths(proposiciones, expresionLogica)

print(tablita)

"""
De alguna forma no me funciona el pip freeze asi que adjunto el link para descargar la libreria
https://pypi.org/project/truth-table-generator/

El codigo depende mas que todo de que coloquen bien las expresiones logicas, ya que si no lo hacen, el codigo no funcionara como deberia

El anterior codigo es la respuesta del ejercicio anteriormente planteado en clase
https://photos.app.goo.gl/pBzffudiEvhAQLE57

Muito cuidado pq el codigo esta al reves
"""

"""
Este otro codigo es la version volteada del anterior como lo planteo el profesor
import ttg

proposiciones = ['p', 'q', 'r']

expresionLogica = ['p implies q', 'not q', 'not q and r', '(p implies q) or (not q and r)', 'r implies q', 'p implies q', '((p implies q) or (not q and r)) implies (r implies q)']

tablita = ttg.Truths(proposiciones, expresionLogica)

# Convertir el objeto tablita a una lista de strings
tablita_list = str(tablita).split('\n')

# Invertir el orden de la lista
tablita_list = tablita_list[::-1]

# Unir los elementos de la lista en un solo string
tablita_invertida = '\n'.join(tablita_list)

print(tablita_invertida)
"""