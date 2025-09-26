# 🌍 FIFA World Cup Winners Dashboard

Live Demo: [View on Render](https://cp321-a7-0ywd.onrender.com)

This is an interactive dashboard built with **Dash**, **Plotly**, and **Pandas** to explore FIFA World Cup winners from 1930 to 2018.
It allows users to visualize total World Cup wins by country, select a country to see how many times it has won, and pick a year to see the tournament’s winner and runner-up.

---

## 📊 Features
- **Choropleth Map**: Visualizes the number of World Cup wins by country.
- **Country Dropdown**: Select a country to display how many times it has won.
- **Year Dropdown**: Select a specific year to display the winner and runner-up.
- **Interactive Dashboard**: Built with Dash callbacks to dynamically update content.

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) – Data handling
- [Plotly Express](https://plotly.com/python/plotly-express/) – Choropleth maps & visualization
- [Dash](https://dash.plotly.com/) – Web application framework

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/world-cup-dashboard.git
cd world-cup-dashboard
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App Locally
```bash
python app.py
```

The app will run at:
👉 http://127.0.0.1:8050/

---

## 📂 Project Structure
```
.
├── app.py              # Main Dash application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📖 Data Source
The dataset is hardcoded in the project as a list of dictionaries, containing FIFA World Cup results from 1930 to 2018.

Example:
```python
{"Year": 2018, "Winner": "France", "Runner-Up": "Croatia"}
```

---

## 🌟 Future Improvements
- Add more detailed statistics (top scorers, goals scored, etc.).
- Fetch live or historical data from an API instead of hardcoding.
- Add bar/line charts to show trends over time.

---

## 👨‍💻 Author
Developed by **[Your Name]**
