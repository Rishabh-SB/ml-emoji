import pandas as pd

data = [
    # 😊 Happy
    ("I'm feeling so cheerful today!", "😊"),
    ("This made me really smile.", "😊"),
    ("Life is good right now.", "😊"),
    ("I'm in such a positive mood!", "😊"),
    ("Everything feels bright and wonderful.", "😊"),
    ("I'm grateful for this beautiful day.", "😊"),
    ("Spreading good vibes everywhere.", "😊"),
    ("This news just made my day.", "😊"),
    ("I'm filled with happiness.", "😊"),
    ("Joy is all around me.", "😊"),

    # 🌧️ Rainy
    ("It's raining cats and dogs outside.", "🌧️"),
    ("A gloomy day with grey clouds.", "🌧️"),
    ("Perfect weather to stay in and read.", "🌧️"),
    ("Listening to the sound of rain.", "🌧️"),
    ("The streets are soaked.", "🌧️"),
    ("Carrying my umbrella everywhere.", "🌧️"),
    ("A cold and drizzly morning.", "🌧️"),
    ("Puddles are forming everywhere.", "🌧️"),
    ("Watching raindrops on the window.", "🌧️"),
    ("A wet day, but still beautiful.", "🌧️"),

    # 💪 Workout
    ("Just finished my workout!", "💪"),
    ("Feeling stronger every day.", "💪"),
    ("Pushing my limits at the gym.", "💪"),
    ("Time to crush this workout.", "💪"),
    ("No pain, no gain.", "💪"),
    ("Strength training is my favorite.", "💪"),
    ("Building muscles step by step.", "💪"),
    ("Another set, another victory.", "💪"),
    ("Focused and determined.", "💪"),
    ("Working hard pays off.", "💪"),

    # 🏖️ Beach
    ("Relaxing by the ocean breeze.", "🏖️"),
    ("The sun feels amazing on my skin.", "🏖️"),
    ("Building sandcastles today.", "🏖️"),
    ("Waves crashing on the shore.", "🏖️"),
    ("Taking a peaceful walk on the beach.", "🏖️"),
    ("Beach days are the best days.", "🏖️"),
    ("Listening to the sound of the sea.", "🏖️"),
    ("Soaking up the sunshine.", "🏖️"),
    ("Enjoying my tropical getaway.", "🏖️"),
    ("Watching the sunset over the water.", "🏖️"),

    # ☕ Coffee
    ("Starting my day with a hot coffee.", "☕"),
    ("Nothing beats a fresh cup of coffee.", "☕"),
    ("Coffee keeps me energized.", "☕"),
    ("Sipping my favorite latte.", "☕"),
    ("Morning brew to kickstart the day.", "☕"),
    ("Espresso is life.", "☕"),
    ("A cozy moment with my coffee.", "☕"),
    ("The aroma of coffee is irresistible.", "☕"),
    ("Refueling with a cup of joy.", "☕"),
    ("Coffee break is the best break.", "☕"),

    # 🎉 Party
    ("Let’s get this party started!", "🎉"),
    ("Celebrating with friends tonight.", "🎉"),
    ("Cheers to good times.", "🎉"),
    ("The dance floor is calling!", "🎉"),
    ("Having a blast at the party.", "🎉"),
    ("Time to celebrate success.", "🎉"),
    ("Feeling festive tonight.", "🎉"),
    ("Music, lights, and laughter.", "🎉"),
    ("Enjoying every moment of this celebration.", "🎉"),
    ("Partying all night long.", "🎉")
]

df = pd.DataFrame(data, columns=["text", "emoji"])
df.to_csv("expanded_emoji_dataset.csv", index=False)
print("Dataset saved to 'expanded_emoji_dataset.csv'")
