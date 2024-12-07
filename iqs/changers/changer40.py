from iqs.utils import os, shutil
from .common import io2zip

def getTestCases(src):
    input_names = []
    output_names = []
    
    for testcase_src in os.listdir(src):
        if testcase_src.endswith('.in'):
            input_names.append(testcase_src)
        else: # ends with .ans
            output_names.append(testcase_src)
    input_names.sort()
    output_names.sort()

    return input_names, output_names


def run(src, des):
    des_path = os.path.join(des, 'contest')
    os.mkdir(des_path)
    src_path = os.path.join(src, os.listdir(src)[0], 'testdata')
    question_names = []

    for letter in os.listdir(src_path):
        question_names.append(f'{letter[0].upper()}: {letter[2:]}')
        problem_des_path = os.path.join(des_path, letter[0].upper())
        os.mkdir(problem_des_path)
        
        problem_des_path_input = os.path.join(problem_des_path, 'in')
        problem_des_path_output = os.path.join(problem_des_path, 'out')
        os.mkdir(problem_des_path_input)
        os.mkdir(problem_des_path_output)

        testcases_sample = os.path.join(src_path, letter, 'data', 'sample')
        testcases_secret = os.path.join(src_path, letter, 'data', 'secret')
        sample_inputs, sample_outputs = getTestCases(testcases_sample)
        secret_inputs, secret_outputs = getTestCases(testcases_secret)
        inputs_path = [*[os.path.join(testcases_sample, item) for item in sample_inputs], *[os.path.join(testcases_secret, item) for item in secret_inputs]]
        outputs_path = [*[os.path.join(testcases_sample, item) for item in sample_outputs], *[os.path.join(testcases_secret, item) for item in secret_outputs]]
        i = 1
        for fin, fout in zip(inputs_path, outputs_path):
            testcase_des_input = 'input' + str(i) + '.txt'
            testcase_des_output = 'output' + str(i) + '.txt'
            i += 1
            shutil.copy(fin, os.path.join(problem_des_path_input, testcase_des_input))
            shutil.copy(fout, os.path.join(problem_des_path_output, testcase_des_output))

        io2zip(problem_des_path, problem_des_path_input, problem_des_path_output)
        print(f'{question_names[-1]} converted successfully!')
    question_names.sort()
    with open(os.path.join(des_path, 'question-names.txt'), 'w') as name_file:
        name_file.write('\n'.join(question_names))