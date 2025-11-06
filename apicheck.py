import openai

# Set your OpenAI API key
api_key = "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"
#api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define the prompt for the model
prompt = f"write me small story"

# Make an API call to the 'davinci' model
response = openai.completions.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=2000  # You can adjust this as needed
)

# Extract the generated text from the API response
generated_text = response.choices[0].text
print(generated_text)