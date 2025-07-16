import os
import ctypes
import requests
from textblob import TextBlob
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import messagebox

# ========== PEXELS API KEY ==========
PEXELS_API_KEY = ""  # <- Replace this with your API key
# ====================================

# 30+ Emotion-to-image mappings
EMOTION_KEYWORDS = {
    "happy": "sunrise",
    "joyful": "flowers",
    "peaceful": "serene landscape",
    "calm": "forest mist",
    "relaxed": "beach sunset",
    "energetic": "mountain hike",
    "motivated": "trail run",
    "hopeful": "sunlight through trees",
    "confident": "city skyline",
    "grateful": "nature closeup",
    "romantic": "candlelight",
    "excited": "colorful lights",
    "lonely": "rain on window",
    "anxious": "foggy street",
    "sad": "stormy clouds",
    "overwhelmed": "waves crashing",
    "angry": "thunderstorm",
    "bored": "monochrome wall",
    "curious": "bookshelf",
    "nostalgic": "vintage photo",
    "scared": "dark alley",
    "tired": "pillows",
    "blank": "empty road",
    "confused": "labyrinth",
    "shy": "quiet corner",
    "free": "open sky",
    "creative": "abstract art",
    "inspired": "sunlight burst",
    "burned out": "desert",
    "serene": "still lake"
}

# ========== Wallpaper Logic ==========
def detect_mood(text):
    text = text.lower()
    for emotion, image_keyword in EMOTION_KEYWORDS.items():
        if emotion in text:
            return image_keyword, emotion

    # Fallback using TextBlob
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity < -0.3:
        return "stormy sky", "negative (fallback)"
    elif polarity < 0.1:
        return "calm fog", "neutral (fallback)"
    else:
        return "vibrant morning", "positive (fallback)"

def fetch_image(mood_keyword):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": mood_keyword, "per_page": 1}
    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)
    data = response.json()

    if not data['photos']:
        return None

    image_url = data['photos'][0]['src']['original']
    img_response = requests.get(image_url)
    image = Image.open(BytesIO(img_response.content))
    filename = "mood_wallpaper.jpg"
    image.save(filename)
    return os.path.abspath(filename)

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# ========== GUI Setup ==========
def on_change_wallpaper():
    user_input = entry.get()
    if not user_input.strip():
        messagebox.showerror("Error", "Please enter how you're feeling.")
        return

    status_label.config(text="Analyzing mood...")
    root.update()

    try:
        mood_keyword, detected_emotion = detect_mood(user_input)
        status_label.config(text=f"Detected emotion: {detected_emotion}")

        image_path = fetch_image(mood_keyword)
        if image_path:
            set_wallpaper(image_path)
            status_label.config(text="✅ Wallpaper changed successfully!")
        else:
            status_label.config(text="❌ No image found for that emotion.")
    except Exception as e:
        status_label.config(text=f"❌ Error: {str(e)}")

# ========== Main Window ==========
root = tk.Tk()
root.title("Mood-Based Wallpaper Changer")
root.geometry("500x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Mood-Based Wallpaper Changer", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="How are you feeling today?")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

btn = tk.Button(root, text="Change Wallpaper", command=on_change_wallpaper, bg="#4CAF50", fg="white", font=("Arial", 12))
btn.pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 10), fg="gray")
status_label.pack(pady=10)

root.mainloop()
