from iqs.utils import os, shutil
from .common import io2zip

def run(src, des):
    des_path = os.path.join(des, 'contest')
    os.mkdir(des_path)
    src_path = os.path.join(src, os.listdir(src)[0]) # Entering first layer
    src_path = os.path.join(src_path, os.listdir(src_path)[0]) # Entering second layer
    question_names = []

    for letter in os.listdir(src_path):
        question_names.append(f'{letter[0].upper()}: {letter[2:]}')
        problem_src_path = os.path.join(src_path, letter)
        problem_des_path = os.path.join(des_path, letter[0].upper())
        os.mkdir(problem_des_path)
        
        problem_des_path_input = os.path.join(problem_des_path, 'in')
        problem_des_path_output = os.path.join(problem_des_path, 'out')
        os.mkdir(problem_des_path_input)
        os.mkdir(problem_des_path_output)

        

        i = 1
        # print(problem_src_path)
        for item in sorted(os.listdir(problem_src_path)):
            if not item.startswith('.') and item.endswith('.in'):
                testcase_des_input = 'input' + str(i) + '.txt'
                testcase_des_output = 'output' + str(i) + '.txt'
                shutil.copy(os.path.join(problem_src_path, item), os.path.join(problem_des_path_input, testcase_des_input))
                shutil.copy(os.path.join(problem_src_path, os.path.splitext(item)[0] + '.ans'), os.path.join(problem_des_path_output, testcase_des_output))
                i += 1

        io2zip(problem_des_path)
        print(f'{question_names[-1]} converted successfully!')
    question_names.sort()
    with open(os.path.join(des_path, 'question-names.txt'), 'w') as name_file:
        name_file.write('\n'.join(question_names))