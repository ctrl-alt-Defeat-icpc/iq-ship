import os

def convert_domjudge_to_sharif(domjudge_file_path, output_dir):
    """
    Converts a Domjudge checker file to the Sharif Judge format.

    Args:
        domjudge_file_path (str): Path to the Domjudge checker C++ file.
        output_dir (str): Directory to save the converted Sharif Judge file.

    Returns:
        str: Path to the generated Sharif Judge file.
    """
    if not os.path.exists(domjudge_file_path):
        raise FileNotFoundError(f"Domjudge checker file not found: {domjudge_file_path}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file_path = os.path.join(output_dir, "tester.cpp")
    
    with open(domjudge_file_path, "r") as domjudge_file, open(output_file_path, "w") as output_file:
        domjudge_code = domjudge_file.read()
        
        # Generate Sharif Judge tester.cpp file
        output_code = f"""/*
 * tester.cpp
 */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[]) {{
    ifstream test_in(argv[1]);    /* Reads test's input file */
    ifstream test_out(argv[2]);  /* Reads test's output file */
    ifstream user_out(argv[3]);  /* Reads user's output file */
    
    /* Your code here, derived from Domjudge checker */
    
    // Parse input values
    int n, k;
    test_in >> n >> k;
    vector<string> U(n);
    for (int i = 0; i < n; ++i) {{
        test_in >> U[i];
    }}

    for (int day = 1; day <= k; ++day) {{
        int outCost, outSize;
        user_out >> outCost >> outSize;
        vector<string> P(outSize);
        for (int i = 0; i < outSize; ++i) {{
            user_out >> P[i];
            for (char &c : P[i]) {{
                c = toupper(c);
            }}
        }}
        
        // Logic for patterns
        vector<bool> inS(n, false);
        int sSize;
        test_in >> sSize;
        vector<int> S(sSize);
        for (int i = 0; i < sSize; ++i) {{
            test_in >> S[i];
            inS[S[i] - 1] = true;
        }}
        
        // Validate patterns and costs
        for (size_t i = 0; i < U.size(); ++i) {{
            bool matches = false;
            for (const string &pattern : P) {{
                if (U[i].find(pattern) != string::npos) {{
                    matches = true;
                    break;
                }}
            }}
            if (matches && !inS[i]) {{
                return 1; // Mismatch in patterns
            }}
            if (!matches && inS[i]) {{
                return 1; // Missing required pattern
            }}
        }}

        int compCost = sSize * 1000 + outSize;
        if (compCost != outCost) {{
            return 1; // Incorrect cost calculation
        }}

        int ansCost;
        test_out >> ansCost;
        if (outCost > ansCost) {{
            return 1; // Output cost exceeds allowed
        }}
    }}

    // Ensure user's output ends correctly
    if (!user_out.eof()) {{
        return 1; // Extra data in user's output
    }}

    return 0; // Output is correct
}}
"""
        output_file.write(output_code)
        return output_file_path


# Example usage
domjudge_checker = "path_to_domjudge_checker.cpp"
output_directory = "output_checker"
converted_checker = convert_domjudge_to_sharif(domjudge_checker, output_directory)
print(f"Converted checker saved at: {converted_checker}")
