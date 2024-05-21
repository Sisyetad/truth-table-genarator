import re
class TruthTable:

    def extract_variables(self,expression):
        variables = []
        pattern = r'[a-zA-Z]+'
        sameLetters = re.findall(pattern, expression)
        for letter in sameLetters:
            if letter not in variables:
                variables.append(letter)
        return variables

    def generate_table_header(self,variables, expression):
        header = variables.copy()
        header.append(expression)
        return [header]

    def generate_truth_values(self,variables):
        values = []
        rows = 2 ** len(variables)
        for i in range(rows):
            row = []
            for j in range(len(variables)):
                value = (i >> j) & 1
                row.append(value)
            values.append(row)
        return values

    def evaluate_expression(self,expression, variables, values):
        evaluation = expression
        for i, variable in enumerate(variables):
            value = values[i]
            evaluation = evaluation.replace(variable, str(value))
        evaluation=evaluation.replace('~',"not ")
        evaluation=evaluation.replace('<=>',"==")
        evaluation=evaluation.replace('=>',"<=")
        return eval(evaluation)
    
    def generate_truth_table(self,expression):
        expression = expression.replace(" ", "")  # Remove whitespace from the expression
        variables = ob1.extract_variables(expression)  # Extract variables from the expression
        table = ob1.generate_table_header(variables, expression)  # Generate table header
        values = ob1.generate_truth_values(variables)  # Generate all possible truth values
        for row in values:
            result = ob1.evaluate_expression(expression, variables, row)  # Evaluate the expression for each truth value combination
            row.append(result)  # Append the expression result to the row
            table.append(row)  # Add the row to the table
        return table
    def generate_result(self,expression):
        expression = expression.replace(" ", "")  # Remove whitespace from the expression
        variables = ob1.extract_variables(expression)  # Extract variables from the expression
        values = ob1.generate_truth_values(variables)  # Generate all possible truth values
        list_result=[]
        for row in values:
            result = ob1.evaluate_expression(expression, variables, row)  # Evaluate the expression for each truth value combination
            list_result.append(result)
        return list_result
    
    def minTerms(self,term):#sum of products
        SOP=[]
        j=0
        for i in term:
            if i == 1:
                SOP.append(j)
            j+=1
        SOP=tuple(SOP)
        print(f"SOP = \u2211 m{SOP}")

    def maxTerms(self,term):#product of sums
        POS=[]
        j=0
        for i in term:
            if i == 0:
                POS.append(j)
            j+=1
        POS=tuple(POS)
        print(f"POS = \u2211 M{POS}")
    
    

# Example usage
for i in range(6):
    intialExpression = input("enter the expression: ")
    ob1=TruthTable()
    truth_table = ob1.generate_truth_table(intialExpression)
    print(f"Truth Table of {intialExpression}")
    for row in truth_table:
        print("\t".join(map(str, row)))
    x=ob1.generate_result(intialExpression)
    ob1.minTerms(x)
    ob1.maxTerms(x)
