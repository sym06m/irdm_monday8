STATIC_INSTRUCTION = "You are a helpful business advisor."

def run_turn(user_input):
    turn_instruction = f"User input: {user_input}"
    prompt = STATIC_INSTRUCTION + "\n" + turn_instruction
    return prompt


print(run_turn("Open a cafe in Almaty"))
