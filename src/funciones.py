def quitamierda(string):
    '''
    Funcion que limpia de % mis columnas para evitar problemas
    ignora los NaN para poder ejecutarse
    '''
    if type(string)==float:
        return string
    else:
        return string.replace('‰',' ').strip()

def marico(arr, size):
    ''' Funcion que agrupa los elementos de 
    un array segun un size dado'''
    arrs = []
    while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
    arrs.append(arr)
    return arrs