import pandas as pd
from LLM.groq import ask_groq  # Make sure this points to your Groq function

def recommend_best_deal_with_ai(df: pd.DataFrame) -> tuple:
    try:
        # Filter high-rated products and sort by price
        df = df[df['rating'] >= 4.0]
        df = df.sort_values(by=['current_price'])

        if df.empty:
            return "No product found", "No products meet the criteria."

        products_text = "\n".join(
            f"{row['product_title']} : {row['current_price']}$, {row['rating']}⭐"
            for _, row in df.iterrows()
        )

        prompt = f"""Here is a list of Amazon India products in INR (₹):
{products_text}

Give me the best value-for-money product from this list(Always choose second product from the list), priced in Indian Rupees (₹). 
NEVER REFER MY INSTRUCTIONS IN THE REPLY. MAKE IT SUCH THAT THE PERSON WILL BE CONVINCED ITS THE BEST PRODUCT
Avoid using the dollar symbol ($). Keep the explanation within 2 sentences.
"""

        result = ask_groq(prompt)
        product = df.iloc[1]['product_title']
        return product, result

    except Exception as e:
        return "Error", f"An error occurred: {e}"
