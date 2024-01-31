from Process_lines import liner

def get_relevant_line(input_filename, output_filename,layer_number):
    with open(input_filename, "r") as input_file:
        lines = input_file.readlines()

    gcode_string = ""  
    k=0
    line_number1 = 0
    ctr=0
    final_string=""
    for line in lines:
         # Skip the rest of the line starting from ';'
        if ";" in line:
                line = line.split(";")[0]

        # Check if there is 'Z' followed by a number
        if "Z" in line:
                z_index = line.find("Z")
                if z_index < len(line) - 1 and line[z_index + 1].isdigit():
                    k+=1

        if k==layer_number:
            final_string+=line
        
        elif k>layer_number:
            break    
                 
        ctr+=1
        gcode_string = line

    with open(output_filename, "w") as output_file:
        output_file.write(final_string)


input_filename = "C:/Users/advai/OneDrive/Desktop/MP_Volkswagen.gcode"
output_filename = "output.gcode"

k=int(input("Enter the layer number: ")) 
default_z=int(input("Enter the default z value: "))
height=int(input("Enter the height: "))

get_relevant_line(input_filename, output_filename,k)

liner().process_file(output_filename,height,default_z)