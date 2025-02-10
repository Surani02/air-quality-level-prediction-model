# 🌍 Air Quality Level Prediction Model  

This repository contains a **Streamlit-based web application** that predicts **air quality levels** based on various environmental parameters. The model is built using a **Voting Classifier** that combines **Random Forest, XGBoost, and LightGBM** for robust classification.

## ⭐ Features  
✅ **Predicts air quality levels** based on input features  
✅ **Uses an ensemble learning approach** for better accuracy  
✅ **Deployed** using **Streamlit** for an interactive and user-friendly experience and easy accessibility 

## 📊 Dataset  
The model is trained on the **Air Quality and Pollution Assessment** dataset from Kaggle:  
🔗 [Dataset Link](https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment)  

The full **training process and model development** is available in the **my Kaggle Notebook**:  
🔗 [Kaggle Notebook](https://www.kaggle.com/code/suraninaranpanawa/air-quality-level-prediction-model)  

## 🧠 Model Details  
The air quality classification model is trained on environmental data, including:  
- 🌡 **Temperature (°C)**  
- 💧 **Humidity (%)**  
- 🫁 **PM2.5 (µg/m³)**  
- 🌫 **PM10 (µg/m³)**  
- 🌪 **NO₂ (ppm)**  
- ☠ **SO₂ (ppm)**  
- 🚗 **CO (ppm)**  
- 🏭 **Proximity to Industrial Areas**  
- 👥 **Population Density (people/km²)**  

The model predicts air quality categories:  
- 🟢 **Good**  
- 🟡 **Moderate**  
- 🟠 **Poor**  
- 🔴 **Hazardous**  

## 📊 Model Overview  
- **Algorithm**: Voting Classifier (Random Forest, XGBoost, LightGBM)  
- **Deployment**: Streamlit  

## 📂 Project Structure  
```
📁 air-quality-level-prediction  
 ├── 📄 app.py                # Streamlit UI  
 ├── 📄 model_loader.py       # Model loading function  
 ├── 📄 air_quality_model.pkl # Trained model file  
 ├── 📄 requirements.txt      # Dependencies  
 ├── 📄 README.md             # Project documentation    
```  

## ⚡ Installation & Usage  

### 1️⃣ Clone the repository and navigate to the project directory 
```bash
git clone https://github.com/your-username/air-quality-level-prediction-model.git
cd air-quality-level-prediction-model
```

### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application  
```bash
streamlit run app.py
```

## 🚀 Live Demo  
Try the **Air Quality Level Prediction Model** here: [https://air-quality-level-prediction-model-druvgyjsboxx559z4r4rrf.streamlit.app/]  

## 🎯 Usage  
1. **Enter environmental factors** such as temperature, humidity, and pollutant levels.  
2. **Click "Predict Air Quality"** to classify the air quality level.  
3. **Get an instant prediction** from the trained model.  

## 🤝 Contributing  
Contributions are welcome! Feel free to **fork**, **open issues**, or **submit pull requests**.  

## 🛡️ License  
This project is **open-source** under the **MIT License**. 
