def process_gcode(input_filename, output_filename):
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    modified_lines = []

    for line in lines:
        modified_line = ''
        i = 0
        while i < len(line):
            char = line[i]

            if char == 'G' or char == 'X' or char == 'Y':
                # Keep the letter itself
                modified_line += char
                i += 1

                # Keep the numbers following 'G', 'X', 'Y'
                while i < len(line) and (line[i].isdigit() or line[i] == '.' or line[i] == '-'):
                    modified_line += line[i]
                    i += 1
            elif char.isspace():
                # Keep spaces
                modified_line += char
                i += 1
            else:
                i += 1

        modified_lines.append(modified_line)

    with open(output_filename, 'w') as output_file:
        output_file.writelines(modified_lines)

# Hard code the input and output filenames
input_filename = 'C:/Users/advai/OneDrive/Desktop/MP_Volkswagen.gcode'
output_filename = 'output.gcode'

# Process the G-code file
process_gcode(input_filename, output_filename)
