from iqs.utils import os, shutil

def run(src, des):
    des_path = os.path.join(des, 'contest')
    os.mkdir(des_path)
    src_path = os.path.join(src, os.listdir(src)[0])

    for letter in os.listdir(src_path):
        problem_des_path = os.path.join(des_path, letter)
        os.mkdir(problem_des_path)
        problem_src_path = os.path.join(src_path, letter, 'problem')
        problem_src_path_input = os.path.join(problem_src_path, 'in')
        problem_src_path_output = os.path.join(problem_src_path, 'out')

        i = 1
        while True:
            fin_src = os.path.join(problem_src_path_input, 'input' + str(i) + '.txt')
            fout_src = os.path.join(problem_src_path_output, 'output' + str(i) + '.txt')
            if not os.path.exists(fin_src) or not os.path.exists(fout_src):
                break
            shutil.copy(fin_src, os.path.join(problem_des_path, str(i) + '.in'))
            shutil.copy(fout_src, os.path.join(problem_des_path, str(i) + '.ans'))
            i += 1
        tester_path_src = os.path.join(problem_src_path, 'tester.cpp')
        if os.path.exists(tester_path_src):
            shutil.copy(tester_path_src, os.path.join(problem_des_path, 'tester.cpp'))

        print(f'{letter} converted successfully!')