# Lista de comandos aceptados por el robot
commands = {
    'MOVE' : True,
    'RIGHT' : True,
    'LEFT' : True,
    'ROTATE' : True,
    'LOOK' : True,
    'DROP' : True,
    'FREE' : True,
    'PICK' : True,
    'POP' : True,
    'CHECK' : True,
    'BLOCKEDP' : True,
    '!BLOCKEDP' : True,
    'NOP' : True,
    'REPEAT' : True,
    'IF' : True,
    'DEFINE' : True,
    'TO' : True,
    'OUTPUT' : True,
    'END' : True
}

numericParametersCommands = {
    'MOVE' : True,
    'RIGHT' : True,
    'LEFT' : True,
    'ROTATE' : True,
    'DROP' : True,
    'FREE' : True,
    'PICK' : True,
    'POP' : True,
}

#Lista de comandos para la instrucción Look
lookCommands = {
    'N' : True,
    'E' : True,
    'W' : True,
    'S' : True
}

#Lista de comandos para la instrucción Check
checkCommands = {
    'C' : True,
    'B' : True
}

#Funciones de verificacion

def alphabeticVariable(variable):
    if variable.isalpha():
        return True
    else:
        return False

def integerValue(value):
    if value.isnumeric():
        return True
    else:
        return False

#Variables definidas durante la ejecución del programa
definedVariables= {}

#Caracteres especiales
specialChars = {
    "(" : 0,
    ")" : 0,
    "[" : 0,
    "]" : 0,
    ":" : 0
}

def wordInCommands(word):
    """Verifica si una instrucción se encuentra dentro de la lista de comandos."""
    if word in commands.keys():
        return True
    else:
        return False

def verifyInstructions():
    """Verifica que las instrucciones ingresadas sean correctas"""
    instructionsList = "" #String que contiene todas las instrucciones leídas en el archivo de texto
    filename = input("Ingrese el nombre del archivo a leer (incluya la extensión): \n")
    with open(filename,"r") as file: #Lectura el archivo de texto
        for line in file:
            instructionsList += line #Se añade cada línea leída al String que contiene todo
    print("INICIO DE LA VERIFICACIÓN")
    actualPosition = 0
    value = 0
    lookInstruction = False # Centinela que espera la instrucción del LOOK
    validInstruction = True # Centinela que comprueba si el conjunto de instrucciones es correcto
    word = "" # Formación de comandos
    for char in instructionsList: #Recorremos cada una de las instrucciones
        if word in numericParametersCommands.keys():
            if instructionsList[actualPosition + 1].isdigit() == False:
                validInstruction = False
        if word == "LOOK": #Verifica si el comando es LOOK
            lookInstruction = True
        if word in lookCommands.keys():
            lookInstruction = False
        if word == "DEFINE": #Revisa la instruccion de definición
            variable = instructionsList[actualPosition + 1]
            value = instructionsList[actualPosition + 2]
            if (alphabeticVariable(variable) == False or variable.lower() != variable) or integerValue(value) == False: #Revisa si no son correctos los parametros
                validInstruction = False
            else: #Si lo son, se agrega la variable al diccionario
                definedVariables[variable] = value
        if word == "TO":
            if type(instructionsList[actualPosition + 1]) == str: #Si la funcion tiene un nombre en string asignado, comienza la verificación
                followup = True
                advanceNumber = 2
                parametersNumber = 0
                while followup == True: #Mientras hayan parametros a agregar, se ejecuta la instruccion
                    posibleParameter = instructionsList[actualPosition + advanceNumber]
                    if posibleParameter.count(':') == 1 and posibleParameter[0] == ':': #Si es un parametro, se añade al numero de parametros y se aavnza
                        parametersNumber += 1
                        advanceNumber += 1
                    elif posibleParameter == "OUTPUT": #Si se llega a la instruccion OUTPUT se detiene la revision de parametros
                        followup = False
                    else: #Si hay una instruccion extra o una variable mal declarada se detiene el ciclo y se invalida la instruccion 
                        followup = False
                        validInstruction = False
            else: #Si el nombre no es valido, se invalida la instruccion
                validInstruction = False
        if char in specialChars.keys():
            specialChars[char] += 1
        if char == " " or char == "\n" or char in specialChars.keys():  #Si el caracter es un espacio o salto de línea, se ignora
            pass
        else:        # De lo contrario se le añade a la cadena de caracteres
            word += char
        if char == " " or char == "\n": #Indica el separador
            result = wordInCommands(word)
            if result:
                word = ""
            else:
                word = ""
        actualPosition+= 1
    #Verificación de que haya la misma cantidad de caracteres de apertura como de cierre            
    if specialChars['('] == specialChars[')']:
        pass
    else:
        validInstruction = False
    if specialChars['['] == specialChars[']']:
        pass
    else:
        validInstruction = False
    if not lookInstruction:
        pass
    else:
        validInstruction = False

    # Veridicamos si la instrucción fue correcta o no
    if validInstruction:
        print("La instrucción ingresada es correcta.")
    else:
        print("La instrucción ingresada no es válida.")

verifyInstructions()