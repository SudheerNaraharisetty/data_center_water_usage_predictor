# **AI-Data Centers Water Usage Predictor 🌊💡**

![Water Usage Predictor](https://img.shields.io/badge/Status-Completed-brightgreen)  
📌 **Author:** [Sai Sudheer Naraharisetty](https://github.com/SudheerNaraharisetty)  
📌 **License:** MIT  
📌 **Project Type:** Embedded Analytics, ESG, Predictive Modeling, Data Science  
📌 **Technologies Used:** Python, XGBoost, Streamlit, Tableau, Pandas, Matplotlib, Seaborn  

---

## 📖 **Project Overview**
This project focuses on analyzing and predicting **water consumption (L/kWh) in data centers** based on different energy sources used in power generation. The goal is to **optimize water efficiency** using **predictive analytics (XGBoost)** and **prescriptive analytics** to simulate the impact of energy source adjustments.  

Data centers consume substantial water, both **on-site** (cooling) and **off-site** (power generation). By leveraging **machine learning and ESG analytics**, this tool provides actionable insights to **reduce water usage** and promote sustainability.

---
## 📊 **Key Features**
✔ **Descriptive Analytics** – Visualizing water consumption trends across energy grids, cities, and energy sources.  
✔ **Predictive Analytics** – XGBoost-based model predicting total water consumption (L/kWh).  
✔ **Prescriptive Analytics** – Simulating how energy mix changes can reduce water consumption.  
✔ **Web App** – Interactive **Streamlit app** for real-time water usage simulation.  
✔ **Tableau Dashboard** – Data visualizations for trend analysis.  
✔ **GitHub Repository** – Open-source code for easy reproducibility.  

---
## 🗂️ **Project Structure**
```
📂 data_center_water_usage_predictor
│── app.py                    # Streamlit Web App for predictions  
│── data_center_water_usage_predictor.ipynb  # Jupyter Notebook for analysis  
│── xgboost_model.json         # Trained XGBoost model  
│── requirements.txt           # Python dependencies  
│── README.md                  # Project Documentation  
│── /data (if applicable)      # Raw dataset (if included)  
```

---
## 🏗️ **Setup & Installation**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/SudheerNaraharisetty/data_center_water_usage_predictor.git
cd data_center_water_usage_predictor
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Web App**
```bash
streamlit run app.py
```
The application will launch in your browser. 🎉  

---
## 🚀 **How to Use the Web App**
1. **Adjust energy source percentages** (Hydropower, Natural Gas, Nuclear, Coal)  
2. **Modify power generation water usage percentage**  
3. **Click ‘Predict’** to see the estimated **total water consumption (L/kWh)**  
4. **Check recommendations** for reducing water usage  
5. **View projected annual water savings** if adjustments are made  

---
## 🔬 **Predictive Model Details**
### ✅ **Machine Learning Model: XGBoost**
- **Target Variable:** `TOTAL_WUE (L/kWh)` = `ONSITE_WUE + OFFSITE_WUE`
- **Top Features:** OFFSITE_WUE, Hydropower, ZIP Code, Nuclear, Natural Gas, Coal  
- **Best Model Performance:**
  - **MAE:** 0.2564  
  - **RMSE:** 0.4068  
  - **R² Score:** 0.9706  

---
## 📊 **Visualizations & Insights**
### 🔹 **Tableau Visualizations**
1️⃣ **Water Consumption by Energy Grid Region**  
2️⃣ **Energy Source Contribution to Water Consumption**  

### 🔹 **Python-Generated Visualizations**
3️⃣ **Water Usage by City**  
4️⃣ **Feature Correlation Heatmap**  
5️⃣ **Projected Water Savings from OFFSITEWUE Reduction**  

---
## 🤝 **Contributing**
We welcome contributions!  
1. **Fork the repository**  
2. **Create a new branch** (`feature-new-analysis`)  
3. **Commit your changes**  
4. **Push to GitHub and create a Pull Request**  

---
## ⚖️ **License**
This project is licensed under the **MIT License**.

---
## 📩 **Contact & Support**
For any queries or collaborations, reach out via:  
📧 Email: [your-email@example.com]  
📌 GitHub: [SudheerNaraharisetty](https://github.com/SudheerNaraharisetty)  

---
## ⭐ **Acknowledgments**
- **Python Libraries:** Scikit-learn, XGBoost, Streamlit, Pandas, Matplotlib  
- **Data Source:** Environmental, Social & Governance (ESG) Datasets  
- **Inspiration:** Sustainable energy and climate change research  

🔗 **Star this repository** ⭐ if you found it useful! 🚀  

