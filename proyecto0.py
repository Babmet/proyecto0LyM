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
    'NOP' : True,
    'REPEAT' : True,
    'IF' : True,
    'DEFINE' : True,
    'TO' : True,
    'OUTPUT' : True,
    'END' : True
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

#Variables definidas durante la ejecución del programa
definedVariables = {

}

#Caracteres especiales
specialChars = {
    "(" : 0,
    ")" : 0,
    "[" : 0,
    "]" : 0,
    ":" : 0
}

instruction = input("Ingrese la serie de instrucciones a verificar: \n")

def wordInCommands(word):
    """Verifica si una instrucción se encuentra dentro de la lista de comandos."""
    if word in commands.keys():
        return True
    else:
        return False

def verifyInstructions(instruction):
    """Verifica que las instrucciones ingresadas sean correctas"""
    print("INICIO DE LA VERIFICACIÓN")
    lookInstruction = False
    validInstruction = True
    word = "" # Formación de comandos
    for char in instruction: #Recorremos cada una de las instrucciones
        if word == "LOOK":
            lookInstruction = True
        if word in lookCommands.keys():
            lookInstruction = False
        if char in specialChars.keys():
            specialChars[char] += 1
        if char == " " or char == "\n" or char in specialChars.keys():  #Si el caracter es un espacio o salto de línea, se ignora
            pass
        else:        # De lo contrario se le añade a la cadena de caracteres
            word += char
        if char == " " or char == "\n": #Indica el separador
            result = wordInCommands(word)
            if result:
                #print(word)
                #print(result)
                word = ""
            else:
                word = ""
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

verifyInstructions(instruction)