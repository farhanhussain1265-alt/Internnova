def rule_bot(message: str) -> str:
    text = message.strip().lower()

    if text in {"hello", "hi", "hey"}:
        return "Hello! Welcome."
    elif "how are you" in text:
        return "I'm fine."
    elif text in {"bye", "goodbye"}:
        return "Goodbye!"
    elif "see you later" in text:
        return "See you later!"
    else:
        return "Sorry, I didn't understand that."

user_input=input("Enter the text:")
response=rule_bot(user_input)
print(response)