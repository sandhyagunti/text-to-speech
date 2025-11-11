import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator
from io import BytesIO

# --- Page Setup ---
st.set_page_config(page_title="Text to Speech Translator", page_icon="🗣️", layout="centered")

# --- Title ---
st.title("🗣️ Text to Speech Translator")

st.divider()

# --- Sidebar: Language Selection ---
with st.sidebar:
    st.header("🌐 Choose Language")
    languages = {
        'English': 'en', 'Hindi': 'hi', 'Bengali': 'bn', 'Tamil': 'ta',
        'Telugu': 'te', 'French': 'fr', 'German': 'de', 'Punjabi': 'pa',
        'Gujarati': 'gu', 'Marathi': 'mr', 'Kannada': 'kn', 'Malayalam': 'ml',
        'Urdu': 'ur', 'Spanish': 'es','Korea':'ko','Japanese':'ja'
    }
    lang_name = st.selectbox("Select Target Language", list(languages.keys()))
    lang_code = languages[lang_name]

# --- Main Section ---
st.subheader("📝 Enter English Text Below")
text = st.text_area("Your Text", placeholder="Type something to translate and hear...")

# --- Translate and Speak ---
if st.button("🎧 Translate & Speak"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        with st.spinner("Translating and generating speech... ⏳"):
            try:
                translated_text = GoogleTranslator(source='en', target=lang_code).translate(text)

                st.success(f"Translated Text ({lang_name}):")
                st.write(translated_text)

                # Generate and play audio
                tts = gTTS(text=translated_text, lang=lang_code)
                audio_stream = BytesIO()
                tts.write_to_fp(audio_stream)
                audio_stream.seek(0)

                st.audio(audio_stream, format="audio/mp3")
                st.download_button(
                    "💾 Download Audio",
                    audio_stream,
                    file_name="translated.mp3",
                    mime="audio/mp3"
                )
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")

st.divider()

# --- Tips Section ---
st.header("💡 Pro Tips for Best Results")
st.markdown("""
- 🧠 Try different languages to enhance your learning and pronunciation skills.  
- 🎧 Use short and clear sentences for better translation and speech output.  
- 💾 Save your audio and replay it to improve pronunciation.  
""")

st.divider()

# --- Footer ---
st.caption("✨ Built with ❤️ using Streamlit, gTTS & Google Translator ✨")
