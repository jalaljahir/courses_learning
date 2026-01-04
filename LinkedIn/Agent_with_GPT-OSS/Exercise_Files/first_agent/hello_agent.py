def create_greeting (name: str) -> str:
    return f"Hello, {name}! Welcome to the world of AI Agents!"

def run_agent():
    # Understand Intent
    user_name = input ("What is your name?")
    # Plan
    print("Optimus: I should use the create_greeting tool.")
    # Use Tools
    greeting = create_greeting (user_name)
    # Reflect
    if greeting:
        print(f"Optimus: {greeting}")
    else:
        print("Optimus: I failed to create a greeting")

if __name__ == "__main__":
    run_agent ()