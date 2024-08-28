from langchain_google_genai import GoogleGenerativeAI
gemini_api_key = "AIzaSyCqE-v8w4z4KVysRZ2fIv6s7NdOko-fbZg"

llm = GoogleGenerativeAI(
    model="gemini-pro",  # Replace with the desired Gemini model
    google_api_key=gemini_api_key
)

if __name__ == "__main__":
  gemini_api_key = gemini_api_key
  text = input("Enter the text you want to summarize: ")
  max_tokens = int(input("Enter the maximum number of tokens for the summary (optional, default is 128): ") or 128)

  prompt = [f"Summarize the following text:\n\n{text}"]
  response = llm.generate(prompt, max_tokens=max_tokens)
  print(f"Summary:\n{response}")
