import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def diagnostic_test():
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found in .env file.")
        return

    print(f"✅ API Key found: {api_key[:5]}...{api_key[-5:]}")
    
    try:
        client = genai.Client(api_key=api_key)
        
        print("\n--- Testing Model Access ---")
        available_models = []
        for model in client.models.list():
            available_models.append(model.name)
            # Shorten names for display: 'models/gemini-3-flash' -> 'gemini-3-flash'
            print(f"  - {model.name}")

        # Check for Gemini 3 or 2
        test_model = "gemini-3-flash" if "models/gemini-3-flash" in available_models else "gemini-2.0-flash"
        
        print(f"\n--- Making Test Call with {test_model} ---")
        response = client.models.generate_content(
            model=test_model, 
            contents="Say 'API is working!'"
        )
        print(f"🤖 Response: {response.text}")
        print("\n✅ Everything looks good!")

    except Exception as e:
        print(f"\n❌ API Error: {e}")
        if "403" in str(e):
            print("💡 Tip: 403 usually means your API key is correct, but it doesn't have permission for this specific API or model.")
        elif "404" in str(e):
            print("💡 Tip: 404 usually means the model name you typed doesn't exist.")

if __name__ == "__main__":
    diagnostic_test()