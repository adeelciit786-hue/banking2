# 🏦 HBDB Banking Bot - AI-Powered Banking Assistant

A professional banking chatbot powered by **Mistral Large AI** and built with **Streamlit**. This bot provides instant answers to banking-related questions using a comprehensive FAQ database.

## ✨ Features

- 🤖 **AI-Powered Responses** - Uses Mistral Large LLM for intelligent banking assistance
- 💬 **Real-time Chat** - Interactive conversation interface
- 📚 **FAQ Database** - 50+ banking questions and answers
- 🔍 **Smart Search** - Search through FAQs instantly
- 🎨 **Professional UI** - Banking-themed dark interface with gold accents
- 🔒 **Secure** - Built with security best practices
- ⚡ **Fast** - Real-time responses from Mistral AI
- 📱 **Responsive** - Works on desktop and mobile

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/adeelciit786-hue/banking2.git
cd banking2
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run banking_bot.py
```

5. **Access the bot**
Open your browser and go to: http://localhost:8501

## 📦 Dependencies

- `streamlit` - Web app framework
- `mistralai` - Mistral AI SDK
- `pandas` - Data processing
- `python-dotenv` - Environment variables

See `requirements.txt` for all dependencies.

## 🌐 Deployment on Streamlit Cloud

### Step 1: Prepare Your Repository
✅ Already done! Your code is pushed to GitHub at:
- Repository: https://github.com/adeelciit786-hue/banking2

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit https://share.streamlit.io

2. **Sign in with GitHub**
   - Click "Sign in with GitHub" or create a new account
   - Authorize Streamlit to access your repositories

3. **Deploy Your App**
   - Click "New app"
   - Select Repository: `adeelciit786-hue/banking2`
   - Select Branch: `master`
   - Set Main file path: `banking_bot.py`
   - Click "Deploy"

4. **Wait for Deployment**
   - Streamlit will automatically build and deploy your app
   - You'll get a shareable URL (e.g., `https://banking2-xxxxx.streamlit.app`)

### Step 3: Configure Environment (if needed)

If you need to use environment variables:

1. In Streamlit Cloud dashboard, go to your app settings
2. Add secrets in the "Secrets" section
3. Add your Mistral API key:
```
MISTRAL_API_KEY = "your-api-key-here"
```

## 📋 Project Structure

```
banking2/
├── banking_bot.py                    # Main Streamlit application
├── requirements.txt                  # Python dependencies
├── hbdb_banking_faqs (2) (1).csv    # Banking FAQ dataset
├── .gitignore                        # Git ignore file
└── README.md                         # This file
```

## 🎨 UI Features

**Color Scheme:**
- Deep Navy Blue (#001a4d to #0052cc)
- Gold Accents (#FFD700)
- Professional banking aesthetic

**Sections:**
- Decorative header with welcome message
- Chat interface with message history
- Sidebar with FAQ search and statistics
- Professional footer with branding

## 💡 How It Works

1. User asks a banking question
2. Question is sent to Mistral Large LLM
3. LLM uses FAQ context to generate relevant answers
4. Response is displayed in chat interface
5. Chat history is maintained during session

## 🔑 API Key

The bot uses the Mistral Large model API. The API key is configured in the application.

**Note:** For production, store API keys securely as environment variables.

## 📝 FAQ Database

The bot is trained on a comprehensive FAQ database including:
- Account opening and management
- Banking services (credit cards, loans, mortgages)
- Online and mobile banking
- Transfers and payments
- Customer support information

## 🛠️ Customization

You can customize the bot by:

1. **Adding more FAQs** - Edit `hbdb_banking_faqs (2) (1).csv`
2. **Changing colors** - Modify CSS in `banking_bot.py` under the `<style>` section
3. **Adjusting responses** - Change temperature and max_tokens in `get_mistral_response()`

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Mistral AI Documentation](https://docs.mistral.ai)
- [GitHub Actions for CI/CD](https://github.com/features/actions)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements.

## 📄 License

This project is open source and available under the MIT License.

## 📞 Support

For issues or questions:
1. Check the FAQ database in the sidebar
2. Review the [GitHub Issues](https://github.com/adeelciit786-hue/banking2/issues)
3. Contact HBDB customer service

## 🎯 Next Steps

1. ✅ Code is pushed to GitHub
2. ⏭️ Deploy to Streamlit Cloud (follow steps above)
3. 📢 Share your deployment link
4. 🚀 Monitor and improve based on feedback

---

**Created with ❤️ for HBDB Bank**
Powered by Mistral AI & Streamlit
