from iqs.utils import os, shutil
from .common import io2zip

def run(src, des):
    des_path = os.path.join(des, 'contest')
    os.mkdir(des_path)
    src_path = os.path.join(src, os.listdir(src)[0])

    for testcase_letter in os.listdir(src_path):
        problem_src_path = os.path.join(src_path, testcase_letter)
        problem_des_path = os.path.join(des_path, testcase_letter[-1].upper())
        os.mkdir(problem_des_path)
        
        problem_des_path_input = os.path.join(problem_des_path, 'in')
        problem_des_path_output = os.path.join(problem_des_path, 'out')
        os.mkdir(problem_des_path_input)
        os.mkdir(problem_des_path_output)

        input_names = []
        output_names = []

        for testcase_src in os.listdir(problem_src_path):
            if testcase_src.endswith('.in'):
                input_names.append(testcase_src)
            else: # ends with .ans
                output_names.append(testcase_src)
        
        input_names.sort()
        output_names.sort()
        i = 1
        for fin, fout in zip(input_names, output_names):
            testcase_des_input = 'input' + str(i) + '.txt'
            testcase_des_output = 'output' + str(i) + '.txt'
            i += 1
            
            shutil.copy(os.path.join(problem_src_path, fin), os.path.join(problem_des_path_input, testcase_des_input))
            shutil.copy(os.path.join(problem_src_path, fout), os.path.join(problem_des_path_output, testcase_des_output))

        io2zip(problem_des_path, problem_des_path_input, problem_des_path_output)