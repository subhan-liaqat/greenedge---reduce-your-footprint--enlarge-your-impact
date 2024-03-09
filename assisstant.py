import os
import time
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "asst_qTL3e7ItDIhtNUmDtWum1cA0"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

assistant_id = "asst_qTL3e7ItDIhtNUmDtWum1cA0"

def get_prompt(question):
    try:
        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=question
        )
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant_id)

        # Wait for the run to complete
        while True:
            time.sleep(10)
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )
            if run_status.status == "completed":
                break

        messages = client.beta.threads.messages.list(thread_id=thread.id)
        assistant_response = messages.data[1].content[0].text.value  # Assuming assistant's response is the second message
        return assistant_response

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
question = "What is the best way to reduce my carbon footprint?"
response = get_prompt(question)
print(response)