# import chatcore
# from dotenv import load_dotenv
# import os
# load_dotenv()

# chatcore.api_key = os.getenv("OPENAI_API_KEY")


# def chat_with_gpt(prompt):
#     response = chatcore.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or "gpt-4" if available
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return response.choices[0].message.content.strip()

# print("GPTBot: Hello! Type 'exit' to quit.")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("GPTBot: Goodbye!")
#         break
#     reply = chat_with_gpt(user_input)
#     print("GPTBot:", reply)
