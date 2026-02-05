# Mario CGPA Tracker - Portfolio Section

A retro Super Mario-themed GPA tracker for your portfolio, featuring automatic animations and interactive gameplay!

## 🎮 Features

### Automatic Mode (Default)
- Mario automatically walks across the screen
- Hits each semester brick one by one to reveal SGPA
- Captures the flag at the end to reveal overall CGPA
- Smooth animations and particle effects
- Retro pixel-art styling inspired by Super Mario Bros (1984)

### Interactive Play Mode
- Click the **PLAY** button in the top right corner
- Control Mario with keyboard:
  - **← →** Arrow keys to move left/right
  - **SPACE** to jump
- Hit bricks yourself to reveal grades
- Reach the flag to complete the game

## 🚀 Quick Start

### Installation

1. **Clone or navigate to the repository:**
```bash
cd D:\GitREPOS\Mario_Cgpa
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

Open your browser and visit: **http://127.0.0.1:5000**

## 📁 Project Structure

```
Mario_Cgpa/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── templates/
│   └── index.html                 # Main game template
├── stitch_mario_retro_gpa_tracker_section/
│   └── code.html                  # Original reference design
└── README.md                      # This file
```

## 🎨 Customization

### Changing Your Grades

Edit the `semester_data` in `app.py`:

```python
semester_data = [
    {"semester": 1, "sgpa": 9.0},
    {"semester": 2, "sgpa": 8.8},
    # ... add or modify semesters
]
```

The CGPA is automatically calculated.

### Styling

The template uses:
- **Tailwind CSS** for responsive design
- **Press Start 2P** font for retro pixel text
- Custom CSS animations for Mario physics
- Dark mode support (toggle in navbar)

### Colors

Key color variables in the Tailwind config:
- `mario-sky`: #5c94fc (Sky blue)
- `mario-ground`: #d45b12 (Orange/brown ground)
- `mario-block`: #fb923c (Question block orange)

## 🎵 Adding Sound Effects (Optional)

To add authentic Mario sound effects:

1. Download retro sound effects (jump.mp3, coin.mp3, flagpole.mp3)
2. Create a `static/sounds/` directory
3. Update the sound functions in `index.html`:

```javascript
function playJumpSound() {
    new Audio('/static/sounds/jump.mp3').play();
}

function playHitSound() {
    new Audio('/static/sounds/coin.mp3').play();
}

function playVictorySound() {
    new Audio('/static/sounds/flagpole.mp3').play();
}
```

## 🔧 API Endpoint

The app includes a REST API endpoint:

```
GET /api/grades
```

Returns JSON with all semester data and CGPA:
```json
{
  "semesters": [
    {"semester": 1, "sgpa": 9.0},
    ...
  ],
  "cgpa": 9.35
}
```

## 🌐 Deployment

### For Production

Set `debug=False` in `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Embedding in Your Portfolio

You can embed this section in your portfolio by:

1. **iFrame approach:**
```html
<iframe src="http://your-domain.com:5000" width="100%" height="600px"></iframe>
```

2. **Direct integration:**
Copy the HTML from `templates/index.html` and integrate into your portfolio's template system.

## 🎮 Game Controls

| Key | Action |
|-----|--------|
| ← | Move Left |
| → | Move Right |
| SPACE | Jump |

## 📱 Responsive Design

The game is fully responsive and works on:
- Desktop browsers (recommended)
- Tablets
- Mobile devices (touch controls coming in future update)

## 🐛 Troubleshooting

**Port already in use:**
```bash
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

**Mario not moving in play mode:**
- Make sure you clicked the PLAY button
- Check that your browser window is focused
- Try clicking on the game area first

**Animations not smooth:**
- Close other resource-heavy applications
- Try a different browser (Chrome/Firefox recommended)
- Disable browser extensions

## 🎯 Future Enhancements

- [ ] Add sound effects
- [ ] Touch controls for mobile
- [ ] Multiple themes (Dark World, Castle, etc.)
- [ ] Score system
- [ ] Leaderboard
- [ ] Social sharing
- [ ] More characters (Luigi, Princess Peach)
- [ ] Custom background music

## 📝 Credits

- Design inspired by Super Mario Bros (1984) by Nintendo
- Built with Flask, Tailwind CSS, and vanilla JavaScript
- Pixel art styling with Press Start 2P font

## 📄 License

This is a personal portfolio project. Feel free to use and modify for your own portfolio!

---

**Enjoy your retro academic journey! 🍄⭐**
