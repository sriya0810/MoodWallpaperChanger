
# 🌈 Mood-Based Wallpaper Changer

> A smart Python GUI app that changes your Windows desktop wallpaper based on how you're feeling using emotion detection + AI.

---

## 📌 What This App Does

- 🎯 Takes natural language input about your current mood
- 🔍 Analyzes the emotion using keyword mapping + TextBlob sentiment fallback
- 🌄 Fetches a matching image from the **Pexels API**
- 🖼️ Sets the image as your **desktop wallpaper instantly**
- 🧠 Works with 30+ custom emotion-to-image mappings

---

## 📦 Technologies Used

- 🐍 Python 3.11+
- 🧠 [TextBlob](https://textblob.readthedocs.io/en/dev/) – for sentiment fallback
- 🌐 [Requests](https://pypi.org/project/requests/) – for API calls
- 🖼️ [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/) – for image handling
- 🖱️ Tkinter – to build the GUI interface
- 📸 [Pexels API](https://www.pexels.com/api/) – for fetching high-res wallpapers

---

🔧 How to Set Up

1. ✅ Make sure **Python 3.11+** is installed
2. ✅ Clone or download this repo to your system
3. ✅ Open terminal/command prompt and install required packages:

   ```bash
   pip install textblob requests pillow
````

4. ✅ Replace the API key in the code with your own:

   ```python
   PEXELS_API_KEY = "your_actual_api_key_here"
````

   👉 Get your API key from: [pexels.com/api](https://www.pexels.com/api/)

---

## ▶️ How to Run the App

```bash
python mood_gui_app.py
```

💡 You’ll see a window asking:
**"How are you feeling today?"**
Enter your emotion → click **Change Wallpaper** → done!

---

## 🎭 Supported Emotions (Examples)

| Emotion      | Image Keyword |
| ------------ | ------------- |
| happy        | sunrise       |
| sad          | stormy clouds |
| relaxed      | beach sunset  |
| creative     | abstract art  |
| nostalgic    | vintage photo |
| anxious      | foggy street  |
| angry        | thunderstorm  |
| tired        | pillows       |
| confident    | city skyline  |
| burned out   | desert        |
| + 20 more... |               |

---

🧠 Behind the Scenes

* First checks if any **predefined emotion** is present in input
* If no match, falls back to **TextBlob sentiment polarity**:

  * Polarity < -0.3 → negative image
  * Polarity < 0.1 → neutral image
  * Else → positive image


---

📂 Folder Structure

```
MoodWallpaperChanger/
├── mood_gui_app.py
├── README.md
└── mood_wallpaper.jpg   # saved wallpaper (auto-generated)
```

---

🙋‍♀️ Created By

**Sriya Kamat**
Made with 💚 during a rollercoaster debugging ride

---

📜 License

This project is open-source for educational/personal use
Attribution appreciated 🌱

---

```

---


