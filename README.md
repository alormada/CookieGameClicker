# 🍪 Cookie Clicker Bot (Selenium Edition)

This Python script automates the popular [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) game using Selenium. It simulates rapid clicking and intelligently buys upgrades to maximize cookies per second over a 5-minute session.

---

## 🚀 What It Does

- Opens the Cookie Clicker game in a Chrome browser.
- Continuously clicks the cookie to generate cookies.
- Every 5 seconds:
  - Checks available upgrades.
  - Purchases the most expensive upgrade you can afford to maximize growth.
- After 5 minutes, prints your **cookies per second** and closes the browser.

---

## 📁 Project Structure

```
.
├── cookie_clicker_bot.py   # The main automation script
└── README.md               # You're here!
```

---

## ▶️ How to Run

1. **Install dependencies** (Selenium and ChromeDriver).
2. Make sure ChromeDriver is installed and matches your browser version.
3. Run the script:

```bash
python cookie_clicker_bot.py
```

---

## ⚙️ Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (in PATH)
- Selenium (`pip install selenium`)

---

## ⏱️ Runtime

- The script runs for **5 minutes** by default.
- You can adjust the duration by changing this line:

```python
timeout = beginning_time + 60*5  # 5 minutes
```

---

## 📊 Output

At the end, it prints the number of **cookies per second** you achieved:

```bash
Final result: 234.5 cookies/second
```

---

## 📌 Notes

- This is just a fun automation project to demonstrate how Selenium interacts with dynamic web pages.
- The script parses upgrade costs and prioritizes the most expensive affordable upgrade for best efficiency.
- The game must stay open and in focus for proper execution.
