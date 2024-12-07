# ICPC to Quera format translator

you can change dataset format easily by this program from [domjudge](https://www.domjudge.org/) format to [quera class](https://quera.org/) format! We will explain how it works below.

## Quera Format
quera platform used [this test structure +](https://github.com/mjnaderi/Sharif-Judge/blob/docs/v1.4/tests_structure.md#tester-method). this platform uses 2 way of judgment. input/output method and tester method.

## running program
first clone this repo and change directory to repository directory. then using this command to run (maybe `python3` instead of `python`):
```bash
python -m iqs.main
```

## Format Table
| version | checker | uses |
|:---:|:---:|:---:|
| v0 | YES | quera |
| v1 | NO | [tcbank](https://github.com/EnAnsasri/cph) |
| v2 | NO | space (sajjad university icpc contest) |
| v3 | NO | internet icpc asia west (Tehran) 2024 |
| v4 | NO | icpc 2023 (asia west - onsite - Tehran) |
| v5 (not completed!) | YES | icpc 2022 (asia west - onsite - Tehran) |

## Version Structures
You can see the structures of the different versions in this section. Click on each section to expand it. You can see the uses of these versions in the Format Table.



<details><summary><strong>version 0</strong></summary>

```bash
./contest_name
    ./[problem_letter]
        problem.zip
            ./in
                input[test_case_number].txt
            ./out
                output[test_case_number].txt
            tester.cpp # tester file
```

<details><summary>test case example</summary>

```cpp
/*
 * tester.cpp
 */
 
#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(int argc, char const *argv[])
{
 
	ifstream test_in(argv[1]);    /* This stream reads from test's input file   */
	ifstream test_out(argv[2]);   /* This stream reads from test's output file  */
	ifstream user_out(argv[3]);   /* This stream reads from user's output file  */
 
	/* Your code here */
	/* If user's output is correct, return 0, otherwise return 1       */
 
	...
 
}
```
</details>
</details>

<details><summary><strong>version 1</strong></summary>

```bash
./contest_name
    ./[problem_letter]
        [test_case_number].in
        [test_case_number].ans
        tester.cpp # tester file
```
</details>

<details><summary><strong>version 2</strong></summary>

```bash
contest.zip
    [problem_letter].zip
        ./data
            ./secret
                [test_case_number].in
                [test_case_number].ans
```
hint: If the number of test cases is 2 digits, the first test case starts at `01`.
</details>

<details><summary><strong>version 3</strong></summary>

```bash
[contest_name].zip
    ./tests-[problem_letter]
        [test_case_number].in
        [test_case_number].ans
```
There is a bit of instability in this version. It can be either completely normal or in the form `x-y.in` or `.ans`. Where `x` is `0` or `1` (zero means the test case is `public` and other means `private`) and y starts at `01`.
</details>

<details><summary><strong>version 4</strong></summary>

```bash
[contest_name].zip
    ./testdata
        ./[problem_letter]-[problem_name]
            ./data
                ./samble
                    [test_case_number].in
                    [test_case_number].ans
                ./secret
                    [test_case_number].in
                    [test_case_number].ans
```
hint: files format `x-y.in` or `.ans`. Where `x` is `0` or `1` (zero means the test case is `public` and other means `private`) and y starts at `01`.
</details>

<details><summary><strong>version 5</strong></summary>

```bash
[contest_name].zip
    ./testdata
        ./[problem_letter]
            [test_case_number].in
            [test_case_number].ans
            ./checker
                checker.cpp # + Makefile and testlib.h
```
hint: files format `x-y.in` or `.ans`. Where `x` is `0` or `1` (zero means the test case is `public` and other means `private`) and y starts at `01`.
</details>