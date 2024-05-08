def process_file(input_file_path, output_file_path):
    """
    Reads the input file, finds the unique integers, and writes the result to the output file.
    """
    # Open the input file
    with open(input_file_path, 'r') as input_file:
        # Read the integers from the input file
        integers = [int(line.strip()) for line in input_file if line.strip().isdigit()]

    # Find the unique integers
    unique_integers = sorted(set(integers))

    # Write the unique integers to the output file
    with open(output_file_path, 'w') as output_file:
        for num in unique_integers:
            output_file.write(str(num) + '\n')

def read_next_item_from_file(input_file):
    """
    Reads the next integer from the input file, handling the variations mentioned in the instructions.
    """
    line = input_file.readline().strip()
    if line.isdigit():
        return int(line)
    else:
        return None