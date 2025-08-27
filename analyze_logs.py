import openai
import os

# Set up the OpenAI API client using the new syntax
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

def get_ai_explanation(error_log):
    """
    Sends an error log to the OpenAI API and gets a plain-English explanation.
    """
    prompt_text = f"""
    Explain the following error log in simple, plain English.
    Provide potential causes and a general solution, without providing code.
    
    Error log:
    {error_log}
    """

    try:
        # Use the new Chat Completions API endpoint
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that explains technical error logs."},
                {"role": "user", "content": prompt_text}
            ],
            max_tokens=150,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error communicating with OpenAI API: {e}"

def analyze_log_file(file_path):
    """
    Reads a log file, finds error lines, and explains them.
    """
    print("Analyzing log file...")
    with open(file_path, 'r') as log_file:
        for line in log_file:
            if "ERROR" in line:
                print("\n" + "="*50)
                print("Detected ERROR log:")
                print(line.strip())
                print("--- AI Explanation ---")
                explanation = get_ai_explanation(line.strip())
                print(explanation)
                print("="*50 + "\n")

if __name__ == "__main__":
    analyze_log_file('sample.log')