from gemini_client import *

def main():
    client = GeminiClient()
    print("Hello, this is your personal AI assistant. How can I help? \nEnter exit to quit.")
    user_input = input()
    while(user_input.lower() != "exit"):
      print(client.generate_response(user_input))
      user_input = input()
    print("Goodbye!")

if __name__ == "__main__":
  main()