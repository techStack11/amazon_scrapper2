import streamlit as st
import pandas as pd
import os
from Controllers.scraper_controller import search_products
#from Pipelines.data_pipeline import DataPipeline
#from Agents.Agent_feedback import recommend_best_deal_with_ai

# 🧱 Page setup
st.set_page_config(page_title="Amazon Scraper", page_icon="🛍️", layout="centered")

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# 🧾 Title
st.markdown('<div class="title">🛍️ Amazon Product Scraper</div>', unsafe_allow_html=True)

# 📥 Input Section
st.markdown('<div class="section-title">🔎 Search for a product</div>', unsafe_allow_html=True)
product_name = st.text_input("Enter the product name:", placeholder="e.g. MacBook, Headphones...")

# 🔘 Scrape button
if st.button("🚀 Scrape Product Data"):
    if not product_name.strip():
        st.warning("⚠️ Please enter a valid product name.")
    else:
        try:
            with st.spinner('🔍 Searching for products...'):
                # Get results directly without saving to file
                results = search_products(product_name, data_pipeline=None)
                
                if results:
                    df = pd.DataFrame([vars(product) for product in results])
                    
                    # Add serial numbers
                    df.insert(0, 'S.No.', range(1, len(df) + 1))
                    columns_to_keep = ['S.No.', 'name', 'product_title', 'product_url', 
                                     'current_price', 'currency', 'rating']
                    df = df[columns_to_keep]
                    
                    st.success(f"✅ Found {len(df)} products!")
                    st.markdown('<div class="section-title">🗂️ Scraped Product List</div>', unsafe_allow_html=True)
                    
                    # Display with clickable links
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
                    
                    # Add download button that creates CSV on demand
                    st.download_button(
                        "📥 Download CSV",
                        df.to_csv(index=False),
                        file_name=f"{product_name}_products.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("⚠️ No results found.")
        
        except Exception as e:
            st.error(f"⚠️ Error occurred: {str(e)}")

# 🔁 Divider
st.markdown("---")

# 🤖 AI Recommendation Section
#if product_name and os.path.exists(f"{product_name}.csv"):
 #   st.markdown('<div class="section-title">🤖 Ask the AI agent for the best deal</div>', unsafe_allow_html=True)

  #  if st.button("🧠 Recommend the best product"):
   #     with st.spinner("The AI agent is thinking..."):
    #        product, reason = recommend_best_deal_with_ai(f"{product_name}.csv")
     #       st.success(f"🌟 **Recommended product:** {product}")
      #      st.info(f"💬 **Why:** {reason}")
