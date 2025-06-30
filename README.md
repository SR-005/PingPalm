# PingPalm

**PingPalm** is an interactive, hand-tracking multiplayer Pong game that transforms your palms into game controllers. Built using **OpenCV**, **MediaPipe**, and **Pygame**, the game replaces traditional controls with real-time hand gestures captured via webcam, delivering a modern, immersive twist to the classic arcade experience.

> *"Because your palm deserves to play too."*

---

## 🎮 Features

* 🖐️ **Gesture-Based Control**: Move paddles using your index fingers—no mouse or keyboard needed
* 🎯 **Real-Time Hand Tracking** powered by **MediaPipe**
* ⚽ **Obstacle Mechanics**: Speed-triggered center-blocks increase challenge mid-game
* 🧠 **Dynamic Physics & Collision** using **Pygame Rects**
* 🌈 **Ball Color Feedback**: Ball changes color based on court side
* 🎥 **Live Webcam Feed**: Displayed in-game for real-time gesture feedback
* 🧮 **Score Tracking** with auto-reset after each point
* ⏱️ **Round Countdown** before every serve to prepare players
* 🛑 **Game Over Screen** with Restart and Quit options
* 🔁 **Smooth Restart Flow** without exiting the game

---

Let me know if you’d like to add a **single-player mode**, **AI opponent**, or **difficulty levels** section too!


---

## 🛠 Built With

* **Computer Vision:** OpenCV
* **Hand Tracking:** MediaPipe
* **Game Engine/UI:** Pygame
* **Language:** Python 3

---

## 🖼️ Screenshots
![Screenshot 2025-06-30 220410](https://github.com/user-attachments/assets/fe0d9179-ec82-4d6a-940e-de0a0ff4198c)
![Screenshot 2025-06-30 220529](https://github.com/user-attachments/assets/54193b7d-24e7-4101-9e0e-9ae9900ba1c4)
![Screenshot 2025-06-30 220831](https://github.com/user-attachments/assets/0e11efe7-283c-4d35-8532-754133fa27b7)
![Screenshot 2025-06-30 220539](https://github.com/user-attachments/assets/58aea0d4-bb49-45e2-9165-d7e029582c88)

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

*[Download](https://drive.google.com/file/d/1ECw4wyPJR6kC-1io9MlHVXY6RDaKEnMt/view?usp=sharing) the .RAR file, extract it and run the .exe file


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

