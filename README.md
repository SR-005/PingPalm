# PingPalm

**PingPalm** is an interactive, hand-tracking multiplayer Pong game that transforms your palms into game controllers. Built using **OpenCV**, **MediaPipe**, and **Pygame**, the game replaces traditional controls with real-time hand gestures captured via webcam, delivering a modern, immersive twist to the classic arcade experience.

> *"Because your palm deserves to play too."*

---

## 🎮 Features
*  Play with Your Hands: Index finger controls—no keyboard or mouse
*  Real-Time Hand Tracking powered by MediaPipe
*  Mid-Game Obstacles that trigger at higher speeds
*  Dynamic Ball & Paddle Physics with smart collision and visual feedback
*  Live Webcam View and clean UI with scoring, countdowns, and Game Over screen
---

## 🛠 Built With

* **Computer Vision:** OpenCV
* **Hand Tracking:** MediaPipe
* **Game Engine/UI:** Pygame
* **Language:** Python 3

---
## Gameplay

https://github.com/user-attachments/assets/6684a64f-cbfe-40b2-8b29-2afbdb436370

## 🖼️ Screenshots

![Screenshot 2025-06-30 220831](https://github.com/user-attachments/assets/0e11efe7-283c-4d35-8532-754133fa27b7)
![Screenshot 2025-06-30 220539](https://github.com/user-attachments/assets/58aea0d4-bb49-45e2-9165-d7e029582c88)

---
---

## ⚙️ How It Works

###  Hand Detection

* Tracks index fingers (via MediaPipe) to control paddles in real-time.

###  Game Mechanics

* Ball bounces off walls, paddles, and mid-game obstacles.
* Speed increases with hits; scores reset ball with a quick countdown.

###  Visual Feedback

* Ball changes color by court side.
* Live webcam view + clean UI.
* Game ends when a player hits 10 points.

---
---

## 📁 Project Structure

```
pingpalm/
├── PingPalm_bg.jpg              # Background image
├── game.py                      # Main game logic
├── README.md                    # Project description
├── requirements.txt             # Python dependencies
```

### 3. Run the Game

*[Download](https://drive.google.com/file/d/1ECw4wyPJR6kC-1io9MlHVXY6RDaKEnMt/view?usp=sharing) the .RAR file, extract it and run the .exe file

---

Enjoy playing with your palms!

