import streamlit as st

def main():
    st.set_page_config(
        page_title="DoctorAssist",
        page_icon="🔍",
        layout="centered"
    )
    
    # Header
    st.title("Text to SQL Generator")
    st.markdown("Convert your natural language queries into SQL statements")
    
    # Input area
    user_query = st.text_area(
        "Enter your question in plain English:",
        height=150,
        placeholder="e.g., Show me all customers who made purchases last month"
    )
    
    # Submit button with some styling
    if st.button("Generate SQL", type="primary"):
        if user_query:
            with st.spinner("Generating SQL query..."):
                # This is where you would call your text-to-SQL model
                # For now, we'll just display a placeholder
                
                # Placeholder for the SQL generation result
                st.success("SQL generated successfully!")
                
                # Display result in a code block
                sql_result = "SELECT * FROM customers WHERE purchase_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month') AND purchase_date < DATE_TRUNC('month', CURRENT_DATE);"
                
                st.code(sql_result, language="sql")
                
                # Add a copy button (Streamlit handles this automatically with code blocks)
                
                # Optional: Add an execution section
                st.subheader("Execute Query")
                st.warning("⚠️ Please review the SQL before executing")
                if st.button("Run Query"):
                    st.info("Query executed! (This is a placeholder)")
        else:
            st.warning("Please enter a question first.")
    
    # Footer
    st.markdown("---")
    st.markdown("*Powered by Text-to-SQL AI*")

if __name__ == "__main__":
    main()