import re

def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first = []
    second = []
    lines = []
    results = []

    for problem in problems:
        # Check for invalid characters and operators
        if re.search("[^\s0-9+-]", problem) or re.search("[/*]", problem):
            if re.search("[/*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        # Split the problem into parts
        parts = problem.split()
        first_number, operator, second_number = parts[0], parts[1], parts[2]

        # Check for number length
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate result
        if operator == "+":
            result = str(int(first_number) + int(second_number))
        elif operator == "-":
            result = str(int(first_number) - int(second_number))

        # Determine the width of the problems
        width = max(len(first_number), len(second_number)) + 2

        # Format each part
        first.append(first_number.rjust(width))
        second.append(operator + second_number.rjust(width - 1))
        lines.append("-" * width)
        results.append(result.rjust(width))

    # Combine the parts into the final formatted string
    arranged_problems = (
        '    '.join(first) + '\n' +
        '    '.join(second) + '\n' +
        '    '.join(lines) + '\n' +
        '    '.join(results) if solve else
        '    '.join(first) + '\n' +
        '    '.join(second) + '\n' +
        '    '.join(lines)
    )

    return arranged_problems

# Example usage
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], solve=True)}')
