import os

from dsa.hw01.code.src.UniqueInt import process_file

def test_unique_integers():
    input_dir = '/dsa/hw01/sample_inputs/'
    output_dir = '/dsa/hw01/sample_results/'

    for filename in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, f"{filename}_results.txt")
        process_file(input_file_path, output_file_path)

        # Verify the output
        with open(output_file_path, 'r') as output_file:
            unique_integers = [int(line.strip()) for line in output_file]
            assert len(unique_integers) == len(set(unique_integers))
            assert unique_integers == sorted(unique_integers)

if __name__ == '__main__':
    test_unique_integers()