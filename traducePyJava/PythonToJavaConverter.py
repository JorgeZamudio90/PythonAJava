from PythonToJavaListener import PythonToJavaListener
from PythonToJavaParser import PythonToJavaParser

class PythonToJavaConverter(PythonToJavaListener):
    def __init__(self):
        self.java_code = ""
        self.functions_code = ""

    def enterProgram(self, ctx: PythonToJavaParser.ProgramContext):
        # Clase principal y el main
        self.java_code += "public class Main {\n"
        self.java_code += "    public static void main(String[] args) {\n"

    def exitProgram(self, ctx: PythonToJavaParser.ProgramContext):
        # Funciones fuera del main
        self.java_code += "    }\n"
        self.java_code += self.functions_code
        self.java_code += "}\n"

        # Imprimir el código completo de Java generado
        print("Código Java generado:")
        print(self.java_code)

    def enterFunc_def(self, ctx: PythonToJavaParser.Func_defContext):
        # Defiinr las funciones fuera del método main
        func_name = ctx.NAME().getText()
        params = ', '.join([f"int {param.getText()}" for param in ctx.params().NAME()])
        self.functions_code += f"    public static int {func_name}({params}) " + "{\n"
        print(f"Función '{func_name}' detectada con parámetros: {params}")

    def exitFunc_def(self, ctx: PythonToJavaParser.Func_defContext):
        # Cerrar la definición de la función
        self.functions_code += "    }\n"
        print(f"Función '{ctx.NAME().getText()}' cerrada.")

    def enterVar_assign(self, ctx: PythonToJavaParser.Var_assignContext):
        var_name = ctx.NAME().getText()
        expr = ctx.expr().getText()
        self.functions_code += f"        int {var_name} = {expr};\n"
        print(f"Asignación detectada: {var_name} = {expr}")

    def enterReturn_stmt(self, ctx: PythonToJavaParser.Return_stmtContext):
        expr = ctx.expr().getText()
        self.functions_code += f"        return {expr};\n"
        print(f"Sentencia de retorno detectada: return {expr}")

    def enterPrint_stmt(self, ctx: PythonToJavaParser.Print_stmtContext):
        # Captura el texto completo de la expresión dentro del print
        expr_text = ctx.getText().replace("print(", "").rstrip(")")

        # Construye la instrucción println en Java con el texto capturado
        self.java_code += f"        System.out.println({expr_text}));\n"
        print(f"Sentencia de impresión detectada: print({expr_text})")