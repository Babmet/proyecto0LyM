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
    "(" : True,
    ")" : True,
    "[" : True,
    "]" : True,
    ":" : True
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
    word = "" # Formación de comandos
    for letter in instruction: #Recorremos cada una de las instrucciones
        if letter == " " or letter == "\n":  #Si el caracter es un espacio o salto de línea, se ignora
            pass
        else:        # De lo contrario se le añade a la cadena de caracteres
            word += letter
        if letter == " " or letter == "\n": #Indica el separador
            result = wordInCommands(word)
            if result:
                print(word)
                print(result)
                word = ""
            else:
                word = ""
                print("NUEVO COMANDO")
    pass

verifyInstructions(instruction)