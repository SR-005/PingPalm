# PingPalm

**PingPalm** is a creative hand-tracking multiplayer Pong game built using **OpenCV**, **MediaPipe**, and **Pygame**. Instead of using traditional keyboard controls, players control their paddles in real-time using hand gestures captured through their webcam. This brings a fresh, interactive, and modern twist to the classic Pong experience.

> "Because your palm deserves to play too."

---

## 🎮 Features

* Play Pong with your bare hands using webcam-based tracking
* Real-time hand tracking powered by **MediaPipe**
* Smooth collision detection and physics using **Pygame Rects**
* Paddle control using index finger positions
* Dynamic ball color based on screen side
* Score tracking with endgame conditions
* Countdown before each round
* Game Over screen with restart and quit options
* Live camera feed displayed at bottom center for added immersion

---

## 🛠 Built With

* **Computer Vision:** OpenCV
* **Hand Tracking:** MediaPipe
* **Game Engine/UI:** Pygame
* **Language:** Python 3

---

## 🖼️ Screenshots

*(Add your screenshots here)*

---

## ⚙️ How It Works

### 1. Hand Detection

* Uses MediaPipe to detect both left and right hands.
* Tracks the y-coordinate of index fingertips (landmark 8).
* Maps fingertip y-position to paddle movement.

### 2. Game Mechanics

* Ball bounces off top, bottom, and paddles.
* Paddle collision speed increases slightly with each hit.
* Ball resets and score updates when it crosses screen sides.
* After each point, a countdown shows before the round starts.

### 3. Visual Feedback

* Ball changes color depending on which side of the screen it's on.
* Camera feed shows player movements at the bottom center.
* Game ends when either player scores 10 points.

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

*[Download](https://drive.google.com/file/d/1GyBvsdgNBtoMZ_nXj8_VMn_BIg_MJteC/view?usp=sharing) the .RAR file, extract it and run the .exe file


---

## ✨ Future Enhancements

* Add sound effects and music

---

## 🙌 Acknowledgements

* [MediaPipe](https://google.github.io/mediapipe/)
* [OpenCV](https://opencv.org/)
* [Pygame](https://www.pygame.org/)
* [Python](https://python.org)

---

Enjoy playing with your palms!

