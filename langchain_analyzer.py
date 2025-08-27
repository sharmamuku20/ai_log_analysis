import os
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain, SequentialChain

# Make sure Ollama is running in the background and 'phi3' is pulled
# We use the Ollama LLM wrapper from langchain_community
# Note: You can also use ChatOllama if you prefer the ChatMessage format
ollama_model = Ollama(model="phi3")

# --- Step 1: The Explanation Chain ---
# This prompt template defines the first step in our chain
explanation_prompt = ChatPromptTemplate.from_template(
    """
    Explain the following error log in simple, plain English. 
    Be thorough and provide potential causes and a general solution.
    
    Error log:
    {error_log}
    """
)
explanation_chain = LLMChain(
    llm=ollama_model, 
    prompt=explanation_prompt, 
    output_key="explanation"
)

# --- Step 2: The Summary Chain ---
# This prompt template takes the output from the previous step as its input
summary_prompt = ChatPromptTemplate.from_template(
    """
    Summarize the following explanation into a single, concise sentence.
    
    Explanation:
    {explanation}
    """
)
summary_chain = LLMChain(
    llm=ollama_model,
    prompt=summary_prompt,
    output_key="summary"
)

# --- The Final Sequential Chain ---
# This combines the two chains into a single, cohesive workflow
overall_chain = SequentialChain(
    chains=[explanation_chain, summary_chain],
    input_variables=["error_log"],
    output_variables=["explanation", "summary"],
    verbose=True # This shows you what is happening at each step
)

if __name__ == "__main__":
    sample_error = "DatabaseConnectionError: Failed to connect to PostgreSQL database on host 127.0.0.1."
    
    print("Executing the LangChain Sequential Chain...")
    
    # Run the entire chain from a single starting point
    result = overall_chain.invoke({"error_log": sample_error})
    
    print("\n" + "="*50)
    print("Original Log:")
    print(sample_error)
    print("\nFull Explanation (from Step 1):")
    print(result["explanation"])
    print("\nConcise Summary (from Step 2):")
    print(result["summary"])
    print("="*50 + "\n")