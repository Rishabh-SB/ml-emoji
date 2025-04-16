import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import re
import os

DATA_PATH = "training_data.csv"
MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

initial_data = [
    ("I love programming", "❤️"),
    ("This is so funny", "😂"),
    ("What a beautiful day", "😊"),
    ("I am feeling sad", "😢"),
    ("This is surprising", "😮"),
    ("Good night everyone", "😴"),
    ("Let's party", "🎉"),
    ("This is frustrating", "😡"),
    ("Congratulations on your success", "🎉"),
    ("I am in love", "😍"),
]

if not os.path.exists(DATA_PATH):
    pd.DataFrame(initial_data, columns=["text", "emoji"]).to_csv(DATA_PATH, index=False)

def load_data():
    return pd.read_csv(DATA_PATH)

def save_data(df):
    df.to_csv(DATA_PATH, index=False)

def train_model(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['text'])
    y = df['emoji']
    model = MultinomialNB()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

def load_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return vectorizer, model
    else:
        return None, None

def is_valid_emoji(emoji):
    return bool(re.search(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF✀-➿]', emoji))

def process_input(input_text):
    parts = input_text.strip().rsplit(' ', 1)
    if len(parts) == 2:
        text, emoji = parts
        if is_valid_emoji(emoji):
            return text.strip(), emoji.strip()
    return None, None

st.title("🧹 Emoji Predictor & Trainer")

df = load_data()

st.header("🔍 Emoji Prediction")
user_input = st.text_input("Enter a sentence to predict its emoji")

vectorizer, model = load_model()

if user_input:
    if model and vectorizer:
        X_input = vectorizer.transform([user_input])
        prediction = model.predict(X_input)[0]
        st.markdown(f"**Predicted Emoji:** <span style='font-size:48px;'>{prediction}</span>", unsafe_allow_html=True)
    else:
        st.warning("Model not trained yet. Please retrain the model.")

st.header("➕ Add New Training Data")
new_data_input = st.text_input("Enter a new training sentence and emoji (e.g., 'I am happy 😊')")

if st.button("Add Entry"):
    text, emoji = process_input(new_data_input)
    if text and emoji:
        df = pd.concat([df, pd.DataFrame([{"text": text, "emoji": emoji}])], ignore_index=True)
        save_data(df)
        st.success(f"Added: {text} {emoji}")
    else:
        st.error("Invalid format. Make sure to include an emoji at the end.")

st.subheader("📦 Batch Add (Multi-line Input)")
batch_input = st.text_area("Enter multiple entries, each in a new line. Format: sentence emoji")

if st.button("Add Batch Entries"):
    new_entries = []
    for line in batch_input.strip().split('\n'):
        text, emoji = process_input(line)
        if text and emoji:
            new_entries.append({"text": text, "emoji": emoji})
    if new_entries:
        df = pd.concat([df, pd.DataFrame(new_entries)], ignore_index=True)
        save_data(df)
        st.success(f"Added {len(new_entries)} new entries!")
    else:
        st.error("No valid entries found.")

st.subheader("📁 Upload CSV to Add Data")
uploaded_file = st.file_uploader("Upload a CSV file with 'text' and 'emoji' columns", type=["csv"])

csv_data = None

if uploaded_file:
    try:
        temp_data = pd.read_csv(uploaded_file)
        if 'text' in temp_data.columns and 'emoji' in temp_data.columns:
            valid_data = temp_data[temp_data['emoji'].apply(is_valid_emoji)]
            if not valid_data.empty:
                csv_data = valid_data
                st.write("### Preview of Uploaded Data:")
                st.dataframe(csv_data)
            else:
                st.error("No valid emoji entries found in CSV.")
        else:
            st.error("CSV must have 'text' and 'emoji' columns.")
    except Exception as e:
        st.error(f"Error reading CSV: {e}")

if csv_data is not None:
    if st.button("Add Uploaded CSV Data"):
        df = pd.concat([df, csv_data], ignore_index=True)
        save_data(df)
        st.success(f"Added {len(csv_data)} entries from the CSV!")

st.header("📝 Training Data")

with st.expander("Click to view training data"):
    selected_indices = st.multiselect("Select entries to delete:", df.index, format_func=lambda x: f"{df.iloc[x]['text']} {df.iloc[x]['emoji']}")
    if st.button("Delete Selected"):
        if selected_indices:
            df = df.drop(selected_indices).reset_index(drop=True)
            save_data(df)
            st.success(f"Deleted {len(selected_indices)} entries.")
        else:
            st.warning("No entries selected for deletion.")

    for index, row in df.iterrows():
        col1, col2 = st.columns([5, 1])
        with col1:
            st.markdown(f"{row['text']} <span style='font-size:32px;'>{row['emoji']}</span>", unsafe_allow_html=True)
        with col2:
            if st.button("Delete", key=f"delete_{index}"):
                df = df.drop(index).reset_index(drop=True)
                save_data(df)
                st.success(f"Deleted entry: {row['text']} {row['emoji']}")

st.download_button("Download Training Data as CSV", data=df.to_csv(index=False).encode('utf-8'), file_name='training_data.csv', mime='text/csv')

st.header("🔧 Retrain Model")
if st.button("Retrain Model"):
    train_model(df)
    st.success("Model retrained successfully!")
