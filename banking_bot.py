import streamlit as st
import pandas as pd
from mistralai import Mistral

# Page configuration
st.set_page_config(
    page_title="HBDB Banking Bot", 
    page_icon="🏦", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for banking theme
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #001a4d 0%, #003d99 50%, #0052cc 100%);
        background-attachment: fixed;
    }
    
    /* Global text color */
    * {
        color: #E8E8E8 !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002244 0%, #003d80 100%);
        border-right: 3px solid #FFD700;
    }
    
    /* Main content area */
    [data-testid="stMainBlockContainer"] {
        padding: 2rem;
        background: rgba(0, 26, 77, 0.95);
    }
    
    /* Headers and titles */
    h1, h2, h3 {
        color: #FFD700 !important;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    /* Text styling */
    p, span, label {
        color: #E8E8E8 !important;
        font-weight: 500;
    }
    
    /* Chat messages - User */
    .stChatMessage[data-testid="message"] {
        background: linear-gradient(90deg, #003d99 0%, #0052cc 100%);
        border-left: 4px solid #FFD700;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    
    /* Chat input area */
    [data-testid="stChatInputContainer"] {
        background: linear-gradient(90deg, #002244 0%, #003d80 100%);
        border: 2px solid #FFD700;
        border-radius: 12px;
        padding: 1rem;
    }
    
    /* Chat input textbox */
    [data-testid="stTextInput"] input {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #FFD700 !important;
        border-radius: 6px !important;
        font-size: 16px !important;
    }
    
    [data-testid="stTextInput"] input::placeholder {
        color: rgba(255, 215, 0, 0.7) !important;
    }
    
    /* Buttons */
    button {
        background: linear-gradient(90deg, #FFD700 0%, #FFA500 100%) !important;
        color: #001a4d !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 6px !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.3s ease !important;
    }
    
    button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.4) !important;
    }
    
    /* Info boxes */
    .stInfo {
        background: rgba(0, 82, 204, 0.2) !important;
        border-left: 4px solid #FFD700 !important;
        border-radius: 8px !important;
    }
    
    /* Metric styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.3) 0%, rgba(0, 61, 153, 0.3) 100%);
        border: 1px solid #FFD700;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Expander styling */
    [data-testid="stExpander"] {
        background: rgba(0, 82, 204, 0.1) !important;
        border: 1px solid #FFD700 !important;
        border-radius: 8px !important;
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 26, 77, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: #FFD700;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #FFA500;
    }
    
    /* Spinner styling */
    .stSpinner {
        color: #FFD700 !important;
    }
    
    /* Divider */
    hr {
        border: 1px solid #FFD700 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Mistral client
api_key = "3Gvc8k5dxnRxSNa2l9PsyWYpYkyCiRhI"
client = Mistral(api_key=api_key)

# Load FAQ data
@st.cache_data
def load_faq_data():
    df = pd.read_csv("hbdb_banking_faqs (2) (1).csv")
    return df

# Create context from FAQ
def create_context(df):
    context = "You are a helpful HBDB Banking Assistant. Here are frequently asked questions and answers:\n\n"
    for idx, row in df.iterrows():
        context += f"Q: {row['Question']}\nA: {row['Answer']}\n\n"
    return context

# Get response from Mistral
def get_mistral_response(user_message, context):
    messages = [
        {"role": "system", "content": context},
        {"role": "user", "content": user_message}
    ]
    
    response = client.chat.complete(
        model="mistral-large-latest",
        messages=messages,
        temperature=0.7,
        max_tokens=1024
    )
    
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="HBDB Banking Bot", page_icon="🏦", layout="wide")

st.title("🏦 HBDB Banking Assistant Bot")
st.markdown("---")

# Add decorative header
st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 215, 0, 0.05) 100%); border-radius: 12px; margin-bottom: 2rem; border: 2px solid #FFD700;">
    <h3 style="color: #FFD700; margin: 0; font-size: 24px;">💼 Welcome to Your Digital Banking Assistant</h3>
    <p style="color: #E8E8E8; margin: 0.5rem 0 0 0;">Powered by Mistral AI - Your 24/7 Banking Support</p>
</div>
""", unsafe_allow_html=True)

# Load FAQ data
df = load_faq_data()
context = create_context(df)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, rgba(255, 215, 0, 0.1) 0%, rgba(255, 215, 0, 0.05) 100%); border-radius: 12px; border: 2px solid #FFD700; margin-bottom: 1.5rem;">
        <h2 style="color: #FFD700; margin: 0;">🏛️ HBDB Bank</h2>
        <p style="color: #E8E8E8; margin: 0.5rem 0 0 0; font-size: 14px;">Your Trusted Financial Partner</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.header("ℹ️ About This Bot")
    st.info(
        "🤖 **AI-Powered Assistant**: Instant answers to all your banking questions\n\n"
        "💡 **24/7 Support**: Available anytime, anywhere\n\n"
        "🔒 **Secure & Private**: Your information is protected\n\n"
        "📚 **Knowledge Base**: Powered by comprehensive FAQ database"
    )
    
    st.markdown("---")
    
    st.subheader("📊 Service Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📚 FAQ Articles", len(df), "Available")
    with col2:
        st.metric("⚡ Response Speed", "Instant", "Real-time")
    
    st.markdown("---")
    
    st.subheader("🔍 Search FAQs")
    if st.checkbox("📖 Browse FAQ Database", value=False):
        search_query = st.text_input("🔎 Search banking questions...", placeholder="e.g., credit card, account")
        
        filtered_df = df
        if search_query:
            filtered_df = df[
                df['Question'].str.contains(search_query, case=False, na=False) |
                df['Answer'].str.contains(search_query, case=False, na=False)
            ]
        
        if len(filtered_df) > 0:
            st.markdown(f"**Found {len(filtered_df)} matching FAQs**")
            for idx, row in filtered_df.iterrows():
                with st.expander(f"❓ {row['Question'][:70]}...", expanded=False):
                    st.markdown(f"**Answer:**")
                    st.write(row['Answer'])
                    st.divider()
        else:
            st.warning("No matching FAQs found. Try a different search term.")
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: rgba(0, 82, 204, 0.1); border-radius: 8px; border: 1px solid #FFD700;">
        <p style="color: #FFD700; margin: 0; font-size: 12px;">🔐 Secure Banking • 24/7 Support • AI Powered</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Ask me anything about HBDB Banking services...")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response from Mistral
    with st.spinner("🤔 Thinking..."):
        try:
            response = get_mistral_response(user_input, context)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
            with st.chat_message("assistant"):
                st.write(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.session_state.chat_history.pop()  # Remove the user message if API fails

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1.5rem; background: linear-gradient(90deg, rgba(0, 82, 204, 0.1) 0%, rgba(0, 61, 153, 0.1) 100%); border-radius: 12px; border: 1px solid #FFD700; margin-top: 2rem;">
    <p style="color: #FFD700; margin: 0; font-weight: bold;">🏦 HBDB Banking Assistant</p>
    <p style="color: #E8E8E8; margin: 0.5rem 0 0 0; font-size: 14px;">Powered by Mistral Large AI | Secure Banking Solutions</p>
    <p style="color: #A0A0A0; margin: 0.5rem 0 0 0; font-size: 12px;">© 2026 HBDB Bank. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
