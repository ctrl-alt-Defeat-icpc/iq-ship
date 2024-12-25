from iqs.utils import os, shutil
from .common import io2zip
from iqs.checker.handler import convert_domjudge_to_sharif

def run(src, des):
    des_path = os.path.join(des, 'contest')
    os.mkdir(des_path)
    src_path = os.path.join(src, os.listdir(src)[0])

    for letter in sorted(os.listdir(src_path)):
        if letter.startswith('_'):
            continue
        
        problem_des_path = os.path.join(des_path, letter)
        os.mkdir(problem_des_path) # makedir: contest/letter
        problem_src_path = os.path.join(src_path, letter)

        problem_des_path_input = os.path.join(problem_des_path, 'in')
        problem_des_path_output = os.path.join(problem_des_path, 'out')
        os.mkdir(problem_des_path_input) # makedir: contest/letter/in for inputs
        os.mkdir(problem_des_path_output) # makedir: contest/letter/out for outputs

        input_names = []
        output_names = []

        for item in os.listdir(problem_src_path):
            if item.endswith('in'):
                input_names.append(item)
            elif item.endswith('.out'):
                output_names.append(item)
        input_names.sort()
        output_names.sort()

        i = 1
        for fin, fout in zip(input_names, output_names):
            shutil.copy(os.path.join(problem_src_path, fin), os.path.join(problem_des_path_input, 'input' + str(i) + '.txt'))
            shutil.copy(os.path.join(problem_src_path, fout), os.path.join(problem_des_path_output, 'output' + str(i) + '.txt'))
            i += 1

        # checker convert
        checker_src_path = os.path.join(problem_src_path, 'checker', 'checker.cpp')
        checker_des_path = os.path.join(problem_des_path, 'tester.cpp')
        if os.path.exists(checker_src_path): # if checker exist
            with open(checker_src_path, 'r') as checker_in, open(checker_des_path, 'w') as checker_out:
                checker_out.write(convert_domjudge_to_sharif(checker_in.read()))

        io2zip(problem_des_path) # zipping files
        print(f'{letter} converted successfully!')