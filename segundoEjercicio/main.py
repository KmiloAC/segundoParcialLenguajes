import sys
from antlr4 import *
from IterableFunctionsLexer import IterableFunctionsLexer
from IterableFunctionsParser import IterableFunctionsParser
from IterableFunctionsListener import IterableFunctionsListener

class CommandExecutor(IterableFunctionsListener):
    def __init__(self):
        self.output_results = []

    def enterMapDeclaration(self, ctx):  # Cambiado de enterMapCommand
        # Retrieve the lambda expression
        lambda_expression = ctx.lambdaFunction().getText()
        # Adjust lambda expression format if necessary
        corrected_expression = lambda_expression.replace("lambdax", "lambda x")
        iterable_content = ctx.iterableObject().getText()
        iterable_items = eval(iterable_content)

        try:
            function = eval(corrected_expression, {"__builtins__": None}, {})
            mapped_output = list(map(function, iterable_items))
            print(f"Mapped Results: {mapped_output}")
            self.output_results.append(mapped_output)
        except Exception as error:
            print(f"Error during mapping: {error}")

    def enterFilterDeclaration(self, ctx):  # Cambiado de enterFilterCommand
        lambda_expression = ctx.lambdaFunction().getText()
        corrected_expression = lambda_expression.replace("lambdax", "lambda x")
        iterable_content = ctx.iterableObject().getText()
        
        try:
            iterable_items = eval(iterable_content)
            function = eval(corrected_expression, {"__builtins__": None}, {})
            filtered_output = list(filter(function, iterable_items))
            print(f"Filtered Results: {filtered_output}")
            self.output_results.append(filtered_output)
        except Exception as error:
            print(f"Error during filtering: {error}")


def main(input_file):
    # Read the input file line by line
    with open(input_file, 'r') as file:
        for input_line in file:
            input_line = input_line.strip()  # Remove leading and trailing whitespace
            if not input_line:  # Skip empty lines
                continue
            
            print(f"Procesando linea: {input_line}")  # Añadido para depuración
            
            # Process each input line
            input_stream = InputStream(input_line)
            lexer = IterableFunctionsLexer(input_stream)
            tokens = CommonTokenStream(lexer)
            parser = IterableFunctionsParser(tokens)
            tree = parser.program()
            executor = CommandExecutor()
            walker = ParseTreeWalker()
            walker.walk(executor, tree)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Hace falta especificar el archivo con la entrada")
    else:
        main(sys.argv[1])  # Ensure a file name is provided as an argument
