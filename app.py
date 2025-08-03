import streamlit as st
import pandas as pd
import os
from Controllers.scraper_controller import search_products



# Page setup
st.set_page_config(page_title="Amazon Scraper", page_icon="🛍️", layout="centered")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


#Title
st.markdown("<div class=\"title\">🛍️ Amazon Product Scraper</div>", unsafe_allow_html=True)

# Input Section
st.markdown("<div class=\"section-title\">🔎 Search for a product</div>", unsafe_allow_html=True)
product_name = st.text_input("Enter the product name:", placeholder="e.g. MacBook, Headphones...")


from Agents.Agent_feedback import recommend_best_deal_with_ai

# Scrape Button
if st.button("🚀 Scrape Product Data"):
    try:
        with st.spinner("🔍 Searching for products..."):
            # Run product scraper
            results = search_products(product_name, data_pipeline=None)

            if results:
                # Convert to DataFrame
                df = pd.DataFrame([vars(product) for product in results])
                
                # Store in session
                st.session_state.df = df

            else:
                st.warning("⚠️ No results found.")
    except Exception as e:
        st.error(f"⚠️ Error occurred: {str(e)}")

# Display DataFrame if it exists in session state
if "df" in st.session_state and not st.session_state.df.empty:
    df = st.session_state.df
    # Add serial number column only if it doesn't exist
    if "S.No." not in df.columns:
        df.insert(0, "S.No.", range(1, len(df) + 1))

    # Keep only selected columns
    columns_to_keep = ["S.No.", "name", "product_title", "product_url", 
                               "current_price", "currency", "rating"]
    df = df[columns_to_keep]

    st.success(f"✅ Found {len(df)} products!")
    st.markdown("<div class=\"section-title\">🗂️ Scraped Product List</div>", unsafe_allow_html=True)

    # Show DataFrame with clickable links
    st.dataframe(
        df,
        column_config={
            "product_url": st.column_config.LinkColumn(
                "Product URL",
                display_text="View Product",
                help="Click to view product on Amazon"
            )
        },
        hide_index=True
    )

    # CSV download
    st.download_button(
        "📥 Download CSV",
        df.to_csv(index=False),
        file_name=f"{product_name}_products.csv",
        mime="text/csv"
    )


st.markdown("---")

# AI Recommendation Section
if "df" in st.session_state and not st.session_state.df.empty:
    st.markdown("<div class=\"section-title\">🤖 Ask the AI agent for the best deal</div>", unsafe_allow_html=True)

    if st.button("🧠 Recommend the best Affordable product"):
        
        with st.spinner("🧠 The AI agent is thinking..."):
            product, reason = recommend_best_deal_with_ai(st.session_state.df)
            st.success(f"🌟 **Recommended product:** {product}")
            st.info(f"💬 **Why:** {reason}")
           # Extract product URL from the DataFrame based on the recommended product title
            product_url = "#"
            if product != "Unknown Product" and product != "No product found":
    
             filtered_df = st.session_state.df[st.session_state.df["product_title"] == product]

             if len(filtered_df) >= 2:
        # If at least 2 matches, use the second one
              recommended_product_row = filtered_df.iloc[1]
              product_url = recommended_product_row["product_url"]
             elif len(filtered_df) == 1:
        # If only one match, use it
              recommended_product_row = filtered_df.iloc[0]
              product_url = recommended_product_row["product_url"]
             else:
              st.warning("No matching product found in the dataset.")

# Display the button if a valid URL is available
            if product_url and product_url != "#":
              st.markdown(f"""
        <a href="{product_url}" target="_blank">
            <button style="background-color:#4CAF50;color:white;
            padding:10px 20px;border:none;cursor:pointer;border-radius:5px;">
            View Recommended Product</button>
        </a>
    """, unsafe_allow_html=True)


