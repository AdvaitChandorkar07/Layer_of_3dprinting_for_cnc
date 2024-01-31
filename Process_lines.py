class liner:
    def __init__(self) -> None:
        pass

    def get_dictionary(self, line):
        result_dict = {}  # Dictionary to store alphabet characters and their corresponding numbers
        i = 0
        while i < len(line):
            char = line[i]

            if char.isalpha():
                # Found an alphabet character
                current_alphabet = char

                # Move to the next character
                i += 1

                # Collect digits and decimal point to form the floating-point number
                num_str = ''
                while i < len(line) and (line[i].isdigit() or line[i] == '.'):
                    num_str += line[i]
                    i += 1

                # Convert the collected string to a floating-point number and store in the dictionary
                if num_str:
                    result_dict[current_alphabet] = float(num_str)

            else:
                # Move to the next character
                i += 1
        return result_dict
        


    def process_file(self, input_file,height,default_z):
        with open(input_file, "r") as input_file:
            lines = input_file.readlines()
        gcode_string = ""  
        final_string= ""
        result_dict = {}
        for line in lines:
            result_dict = self.get_dictionary(line)
            if result_dict:
                if 'E' not in result_dict:
                    result_dict['Z'] = default_z
                else:
                    result_dict['Z'] = -height
                
                if 'G' in result_dict:
                    result_dict['G'] = int(result_dict['G']) 
                
                if 'E' in result_dict:
                    #remove 'E' from the dictionary
                    result_dict.pop('E')
                    
                # Convert the dictionary back to a string
                modified_line = ""
                #remove F from the dictionary
                if "F" in result_dict:
                    result_dict.pop("F")
                for key in result_dict:
                    modified_line += key + str(result_dict[key]) + " "
                gcode_string += modified_line 
                gcode_string += '\n' # Use modified_line instead of line

        # Close the opened file
        output_filename = "output1.gcode"
        with open(output_filename, "w") as output_file:  # Corrected this line
            output_file.write(gcode_string)
