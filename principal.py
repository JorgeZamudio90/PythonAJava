import antlr4
from PythonToJavaLexer import PythonToJavaLexer
from PythonToJavaParser import PythonToJavaParser
from PythonToJavaConverter import PythonToJavaConverter

#Autor: Jorge Alejandro Zamudio Cahuil
#Grupo: I7B
#Fecha: 13/11/2024
#Version: 1.0
#Descripcion: Este programa convierte un archivo de Python txt a Java.

def translate_python_to_java(file_path):
    with open(file_path, 'r') as file:
        python_code = file.read()

    input_stream = antlr4.InputStream(python_code)
    lexer = PythonToJavaLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = PythonToJavaParser(stream)
    tree = parser.program()

    converter = PythonToJavaConverter()
    walker = antlr4.ParseTreeWalker()
    walker.walk(converter, tree)

    java_code = converter.java_code
    return java_code


# Lee el archivo con la función en Python y tradúcelo a Java
file_path = 'prueba.txt'
java_code = translate_python_to_java(file_path)

# Guarda el código traducido a Java en un archivo de salida
with open('FuncionTraducida.java', 'w') as output_file:
    output_file.write(java_code)

print("La traducción a Java ha sido completada y guardada en 'FuncionTraducida.java'.")
