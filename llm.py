import ollama

with open("prompt.txt") as f:
    SYSTEM_PROMPT = f.read()

def review_pr(diff):
   
    context = diff

    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": f"You are reviewing PR. System prompt: {SYSTEM_PROMPT}"},
            {"role": "user", "content": context}
        ]        
    )
    output = response['message']['content']

    return output