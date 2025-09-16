# MealMind 🍴

**MealMind** is a project that combines a Flutter-based mobile app and a Python backend server.  
It is designed for food recommendations, user preference tracking, and testing machine learning models for food-related data.

---

## 📥 Clone the Repository

First, clone the repository from GitHub and move into the project folder:

```bash
git clone https://github.com/kml-coder/MealMind.git
cd MealMind

## 📂 Project Structure

```
food_recommender_app/   # Flutter app (mobile frontend)
food_server/            # Python backend server (Flask-based API)
```

---

## 🖥 How to Run the Python Server

> **You should start this inside `food_server` folder**

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate environment
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Move to food server
cd food_server

# 5. Run the server
python app.py
```

- Default port: **5000**
- Change the port by editing `app.py` (`app.run(port=XXXX)`)

---

## 📱 How to Run the Flutter App

> **You should start this inside `food_recommender_app` folder**

```bash
# Install dependencies
flutter pub get

# Run app on connected device/emulator
flutter run
```

- To run on Chrome (Web):
  ```bash
  flutter run -d chrome
  ```

- To run on iOS Simulator:
  ```bash
  flutter run -d ios
  ```

- To run on Android Emulator:
  ```bash
  flutter run -d android
  ```

---

## 🔧 Requirements
- Python 3.8+
- Flutter SDK (check with `flutter doctor`)
- Xcode (for iOS)
- Android Studio (for Android)
- Chrome (for web)

---
