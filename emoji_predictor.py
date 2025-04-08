import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import numpy as np

# Expanded Dataset - Ensure both lists have 200 items
texts = [
    'Feeling happy today',
    'It\'s raining outside',
    'Just finished a workout',
    'Going to the beach',
    'Having a cup of coffee',
    'Celebrating a birthday',
    'Watching a movie',
    'Reading a book',
    'Feeling sleepy',
    'It\'s too hot',
    'On a road trip',
    'Feeling adventurous',
    'Lost in thought',
    'Feeling confident',
    'Having a picnic',
    'Cleaning the house',
    'Cooking dinner',
    'Feeling love',
    'At a party',
    'Celebrating an achievement',
    'Feeling excited',
    'Taking a nap',
    'Going shopping',
    'Feeling cold',
    'Attending a concert',
    'Having a barbecue',
    'Walking the dog',
    'Celebrating an anniversary',
    'Drinking a smoothie',
    'Exploring new places',
    'Feeling frustrated',
    'Having a lazy day',
    'Getting ready for a trip',
    'In a meeting',
    'Laughing with friends',
    'On a hike',
    'Enjoying the sunset',
    'Playing video games',
    'Feeling grateful',
    'Feeling surprised',
    'Getting a fresh haircut',
    'Waking up early',
    'At the gym',
    'Going for a run',
    'Feeling nervous',
    'Watching a sunset',
    'Sitting by the fireplace',
    'Going to a wedding',
    'Eating dessert',
    'Making art',
    'At a theme park',
    'Visiting a museum',
    'Going for a swim',
    'Trying new food',
    'Baking cookies',
    'Feeling creative',
    'Hanging out with family',
    'At a coffee shop',
    'Listening to music',
    'On a picnic date',
    'Making new friends',
    'Visiting the zoo',
    'Going to a spa',
    'Preparing for a presentation',
    'Reading the news',
    'Drinking tea',
    'Going to the gym',
    'Having a party',
    'Going to the park',
    'Feeling refreshed',
    'Taking a selfie',
    'Going to a bar',
    'Doing yoga',
    'Feeling artistic',
    'Going on a shopping spree',
    'Trying a new hobby',
    'Attending a conference',
    'Having a quiet day at home',
    'Cleaning up the room',
    'Learning something new',
    'Celebrating Christmas',
    'Feeling blessed',
    'Preparing for a road trip',
    'Waiting for a friend',
    'Stargazing',
    'Singing karaoke',
    'Building something',
    'Taking a walk in nature',
    'Spending time with pets',
    'Going to a football match',
    'Waiting for a package',
    'Playing chess',
    'Cooking a new recipe',
    'Watching the stars',
    'Feeling motivated',
    'Going on a date',
    'Cleaning up after a party',
    'Running errands',
    'Going on a bike ride',
    'Looking at old photos'
]

emojis = [
    '😊',
    '🌧️',
    '💪',
    '🏖️',
    '☕',
    '🎉',
    '🍿',
    '📚',
    '😴',
    '🥵',
    '🚗',
    '🧗‍♂️',
    '🤔',
    '😎',
    '🧺',
    '🧹',
    '🍳',
    '❤️',
    '🎶',
    '🏆',
    '🤩',
    '😴',
    '🛍️',
    '🥶',
    '🎤',
    '🍖',
    '🐕',
    '💍',
    '🥤',
    '🌍',
    '😤',
    '🛋️',
    '✈️',
    '💼',
    '😂',
    '🥾',
    '🌅',
    '🎮',
    '🙏',
    '😲',
    '💇‍♂️',
    '⏰',
    '🏋️‍♀️',
    '🏃‍♂️',
    '😬',
    '🌅',
    '🔥',
    '💒',
    '🍰',
    '🎨',
    '🎢',
    '🖼️',
    '🏊‍♀️',
    '🍣',
    '🍪',
    '💡',
    '👨‍👩‍👧‍👦',
    '☕',
    '🎧',
    '🍉',
    '🤝',
    '🦁',
    '💆‍♀️',
    '📊',
    '📰',
    '🍵',
    '🏋️‍♂️',
    '🎉',
    '🌳',
    '💆‍♂️',
    '🤳',
    '🍻',
    '🧘‍♀️',
    '🎨',
    '🛍️',
    '🎮',
    '🎤',
    '🏡',
    '🧹',
    '📖',
    '🎄',
    '🙏',
    '🚗',
    '👋',
    '🌠',
    '🎤',
    '🛠️',
    '🚶‍♂️',
    '🐱',
    '⚽',
    '📦',
    '♟️',
    '🍲',
    '🌌',
    '💪',
    '🍽️',
    '🧼',
    '🏃‍♀️',
    '🚴‍♂️',
    '📸'
]


# Check lengths before creating the DataFrame
assert len(texts) == len(emojis), f"Length mismatch: {len(texts)} texts, {len(emojis)} emojis"

# Create DataFrame
data = pd.DataFrame({
    'text': texts,
    'emoji': emojis
})

# Model
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(data['text'], data['emoji'])

# Streamlit App
st.title("Emoji Predictor 🎉")
st.write("Type a message, and I'll try to predict the right emoji for it! \n\nMade by Rishabh S. B. for Machine Learning mini-project")

user_input = st.text_input("Your Message", "")

if user_input:
    probabilities = model.predict_proba([user_input])[0]
    top_index = np.argmax(probabilities)
    top_emoji = model.classes_[top_index]
    st.write(f"**Suggested Emoji:** {top_emoji}", unsafe_allow_html=True)
