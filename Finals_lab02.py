# Moore Machine Simulation (Converted from given Mealy Machine)

# Define the Moore Machine as a dictionary
moore_machine = {
    'A_A': {'output': 'A', '0': 'A_A', '1': 'B_B'},
    'B_B': {'output': 'B', '0': 'C_A', '1': 'D_B'},
    'C_A': {'output': 'A', '0': 'D_C', '1': 'B_B'},
    'C_C': {'output': 'C', '0': 'D_C', '1': 'B_B'},
    'D_B': {'output': 'B', '0': 'B_B', '1': 'C_C'},
    'D_C': {'output': 'C', '0': 'B_B', '1': 'C_C'},
    'E_C': {'output': 'C', '0': 'D_C', '1': 'E_C'},
}

# Define start state
start_state = 'A_A'


def process_input(input_str):
    state = start_state
    output = moore_machine[state]['output']  # initial output

    for symbol in input_str:
        if symbol not in ('0', '1'):
            raise ValueError("Input string must contain only 0s and 1s.")

        # Transition to the next state
        state = moore_machine[state][symbol]
        # Append the output of the *new* state
        output += moore_machine[state]['output']

    return output


# --- Test Inputs ---
inputs = ["00110", "11001", "1010110", "101111"]

for inp in inputs:
    print(f"Input: {inp} → Output: {process_input(inp)}")
