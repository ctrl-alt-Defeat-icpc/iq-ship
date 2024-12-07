from iqs.utils import os, shutil
from .common import io2zip

def run(src, des):
    des_path = os.path.join(des, 'contest')
    os.mkdir(des_path)
    src_path = os.path.join(src, os.listdir(src)[0])

    for letter in os.listdir(src_path):
        problem_src_path = os.path.join(src_path, letter, 'data', 'secret')
        problem_des_path = os.path.join(des_path, letter)
        os.mkdir(problem_des_path)
        
        problem_des_path_input = os.path.join(problem_des_path, 'in')
        problem_des_path_output = os.path.join(problem_des_path, 'out')
        os.mkdir(problem_des_path_input)
        os.mkdir(problem_des_path_output)

        for testcase_src in os.listdir(problem_src_path):
            if testcase_src.endswith('.in'):
                testcase_des = 'input' + str(int(os.path.splitext(testcase_src)[0])) + '.txt'
                shutil.copy(
                    os.path.join(problem_src_path, testcase_src),
                    os.path.join(problem_des_path_input, testcase_des)
                )
            else: # ends with .ans
                testcase_des = 'output' + str(int(os.path.splitext(testcase_src)[0])) + '.txt'
                shutil.copy(
                    os.path.join(problem_src_path, testcase_src),
                    os.path.join(problem_des_path_output, testcase_des)
                )
        io2zip(problem_des_path)