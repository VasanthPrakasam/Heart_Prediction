# 🫀 Heart Disease Prediction - Complete Setup Guide
## *Step-by-Step Instructions for VasanthPrakasam/Heart_Prediction*

<div align="center">

![Setup Guide](https://img.shields.io/badge/Setup-Complete%20Guide-success?style=for-the-badge)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner%20Friendly-green?style=for-the-badge)
![Time](https://img.shields.io/badge/Setup%20Time-15%20minutes-blue?style=for-the-badge)

**🚀 From Zero to Running Application in 15 Minutes!**

</div>

---

## 📋 **Table of Contents**
1. [Prerequisites Check](#-prerequisites-check)
2. [Repository Setup](#-repository-setup)
3. [Environment Configuration](#-environment-configuration)
4. [Dependencies Installation](#-dependencies-installation)
5. [Project Structure Overview](#-project-structure-overview)
6. [Running the Application](#-running-the-application)
7. [Testing the Setup](#-testing-the-setup)
8. [Troubleshooting](#-troubleshooting)
9. [Advanced Configuration](#-advanced-configuration)

---

## 🔍 **Prerequisites Check**

Before starting, ensure you have the following installed on your system:

### **System Requirements**
| Component | Minimum Version | Recommended | Check Command |
|-----------|----------------|-------------|---------------|
| **Python** | 3.8+ | 3.9+ | `python --version` |
| **pip** | 21.0+ | Latest | `pip --version` |
| **Git** | 2.0+ | Latest | `git --version` |
| **RAM** | 4GB | 8GB+ | - |
| **Storage** | 500MB | 1GB+ | - |

### **Verification Commands**
```bash
# Check Python installation
python --version
# or on some systems
python3 --version

# Check pip installation
pip --version
# or
pip3 --version

# Check Git installation
git --version
```

### **Installing Missing Prerequisites**

<details>
<summary><strong>🐍 Python Installation</strong></summary>

**Windows:**
1. Download from [python.org](https://python.org/downloads/)
2. Run installer with "Add Python to PATH" checked
3. Verify: `python --version`

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

</details>

<details>
<summary><strong>📦 Git Installation</strong></summary>

**Windows:**
- Download from [git-scm.com](https://git-scm.com/downloads)

**macOS:**
```bash
# Using Homebrew
brew install git
```

**Linux:**
```bash
sudo apt install git
```

</details>

---

## 📂 **Repository Setup**

### **Step 1: Clone the Repository**

Open your terminal/command prompt and run:

```bash
# Navigate to your desired directory
cd Desktop  # or wherever you want to store the project

# Clone the repository
git clone https://github.com/VasanthPrakasam/Heart_Prediction.git

# Navigate into the project directory
cd Heart_Prediction
```

### **Step 2: Verify Repository Contents**

Check that you have all necessary files:

```bash
# List all files in the directory
ls -la  # On Windows: dir

# Expected files structure:
# ├── app.py                    # Main Streamlit application
# ├── heart_disease_model.pkl   # Pre-trained ML model
# ├── requirements.txt          # Python dependencies
# ├── README.md                 # Project documentation
# ├── data/                     # Dataset folder (optional)
# └── notebooks/                # Jupyter notebooks (optional)
```

### **Step 3: Check Repository Status**

```bash
# Verify you're in the correct repository
git remote -v

# Should show:
# origin  https://github.com/VasanthPrakasam/Heart_Prediction.git (fetch)
# origin  https://github.com/VasanthPrakasam/Heart_Prediction.git (push)
```

---

## 🌍 **Environment Configuration**

### **Step 1: Create Virtual Environment**

**Why Virtual Environment?**
- Isolates project dependencies
- Prevents conflicts with other projects
- Easy to manage and reproduce

```bash
# Create virtual environment
python -m venv heart_disease_env

# Alternative name options:
# python -m venv venv
# python -m venv .env
```

### **Step 2: Activate Virtual Environment**

**Windows:**
```bash
# Command Prompt
heart_disease_env\Scripts\activate

# PowerShell
heart_disease_env\Scripts\Activate.ps1

# Git Bash
source heart_disease_env/Scripts/activate
```

**macOS/Linux:**
```bash
source heart_disease_env/bin/activate
```

### **Step 3: Verify Activation**

```bash
# Your prompt should change to show (heart_disease_env)
# Example: (heart_disease_env) C:\Users\YourName\Desktop\Heart_Prediction>

# Verify Python path
which python  # Should point to virtual environment

# Check pip location
which pip     # Should point to virtual environment
```

---

## 📦 **Dependencies Installation**

### **Step 1: Upgrade pip (Recommended)**

```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip
```

### **Step 2: Install from requirements.txt**

If `requirements.txt` exists:
```bash
# Install all dependencies at once
pip install -r requirements.txt
```

### **Step 3: Manual Installation (if requirements.txt missing)**

```bash
# Core dependencies
pip install streamlit==1.28.0
pip install pandas==2.0.3
pip install numpy==1.24.3
pip install scikit-learn==1.3.0

# Visualization dependencies
pip install plotly==5.15.0
pip install matplotlib==3.7.1
pip install seaborn==0.12.2

# Additional utilities
pip install pickle-mixin==1.0.2
```

### **Step 4: Verify Installation**

```bash
# Check installed packages
pip list

# Verify specific packages
python -c "import streamlit; print(f'Streamlit: {streamlit.__version__}')"
python -c "import pandas; print(f'Pandas: {pandas.__version__}')"
python -c "import numpy; print(f'NumPy: {numpy.__version__}')"
python -c "import sklearn; print(f'Scikit-learn: {sklearn.__version__}')"
```

---

## 🏗️ **Project Structure Overview**

### **Expected Directory Structure**

```
Heart_Prediction/
│
├── 📄 app.py                     # Main Streamlit application
├── 🤖 heart_disease_model.pkl    # Trained ML model
├── 📋 requirements.txt           # Dependencies list
├── 📖 README.md                  # Project documentation
│
├── 📁 data/                      # Dataset directory
│   ├── heart_disease_data.csv    # Training dataset
│   └── sample_data.csv           # Test samples
│
├── 📁 notebooks/                 # Jupyter notebooks
│   ├── data_exploration.ipynb    # EDA notebook
│   ├── model_training.ipynb      # Model development
│   └── model_evaluation.ipynb    # Performance analysis
│
├── 📁 models/                    # Model artifacts
│   ├── heart_disease_model.pkl   # Main model
│   └── model_metrics.json        # Performance metrics
│
└── 📁 utils/                     # Utility functions
    ├── data_preprocessing.py     # Data processing
    └── model_utils.py            # Model utilities
```

### **Key Files Explanation**

| File | Purpose | Critical |
|------|---------|----------|
| `app.py` | Main Streamlit web application | ✅ Essential |
| `heart_disease_model.pkl` | Pre-trained ML model | ✅ Essential |
| `requirements.txt` | Python package dependencies | ✅ Essential |
| `README.md` | Project documentation | 📖 Helpful |
| `data/` | Dataset files | 📊 Optional |
| `notebooks/` | Development notebooks | 🔬 Optional |

---

## 🚀 **Running the Application**

### **Step 1: Navigate to Project Directory**

```bash
# Ensure you're in the correct directory
pwd  # Should show: /path/to/Heart_Prediction

# List files to confirm
ls -la
```

### **Step 2: Check Model File**

```bash
# Verify model file exists
ls -la *.pkl

# Expected output:
# heart_disease_model.pkl

# Check file size (should be > 0 bytes)
ls -lh heart_disease_model.pkl
```

### **Step 3: Launch Streamlit Application**

```bash
# Start the application
streamlit run app.py

# Alternative if above doesn't work:
python -m streamlit run app.py
```

### **Step 4: Access the Application**

After running the command, you should see output like:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501
```

**Access Methods:**
1. **Automatic**: Browser should open automatically
2. **Manual**: Copy and paste `http://localhost:8501` into your browser
3. **Network**: Use the Network URL to access from other devices

---

## 🧪 **Testing the Setup**

### **Step 1: Application Loading Test**

✅ **Expected Results:**
- Browser opens to Streamlit application
- Title displays: "❤️ Heart Disease Prediction App"
- No error messages in terminal
- All input widgets load properly

### **Step 2: Model Prediction Test**

**Quick Test Case:**
1. **Age**: 45
2. **Sex**: Male
3. **Chest Pain**: Typical Angina
4. **Blood Pressure**: 140
5. **Cholesterol**: 250
6. **Blood Sugar**: Yes
7. **ECG**: Normal
8. **Max Heart Rate**: 150
9. **Exercise Angina**: Yes
10. **ST Depression**: 2.0
11. **ST Slope**: Flat
12. **Vessels**: 1
13. **Thalassemia**: Fixed Defect

**Click "🔍 Predict"**

✅ **Expected Result:** Application should display either:
- "✅ The person is likely **not** suffering from heart disease."
- "⚠️ The person **may have heart disease**. Please consult a doctor."

### **Step 3: Performance Test**

- **Loading Time**: Should be < 5 seconds
- **Prediction Time**: Should be < 2 seconds
- **UI Responsiveness**: Smooth interactions

---

## 🔧 **Troubleshooting**

### **Common Issues & Solutions**

<details>
<summary><strong>❌ Issue: "streamlit: command not found"</strong></summary>

**Cause:** Streamlit not installed or virtual environment not activated

**Solutions:**
```bash
# 1. Check if virtual environment is activated
# Look for (heart_disease_env) in prompt

# 2. Activate virtual environment
source heart_disease_env/bin/activate  # macOS/Linux
# or
heart_disease_env\Scripts\activate     # Windows

# 3. Install streamlit
pip install streamlit

# 4. Try alternative command
python -m streamlit run app.py
```

</details>

<details>
<summary><strong>❌ Issue: "ModuleNotFoundError: No module named 'pandas'"</strong></summary>

**Cause:** Required packages not installed

**Solutions:**
```bash
# 1. Activate virtual environment
source heart_disease_env/bin/activate

# 2. Install missing packages
pip install pandas numpy scikit-learn plotly

# 3. Or install from requirements
pip install -r requirements.txt
```

</details>

<details>
<summary><strong>❌ Issue: "FileNotFoundError: heart_disease_model.pkl"</strong></summary>

**Cause:** Model file missing or in wrong location

**Solutions:**
```bash
# 1. Check if file exists
ls -la *.pkl

# 2. If missing, check if it's in a subdirectory
find . -name "*.pkl"

# 3. If found in subdirectory, move to main directory
mv models/heart_disease_model.pkl .

# 4. If completely missing, you may need to train the model
# Check if there's a training notebook in the notebooks/ directory
```

</details>

<details>
<summary><strong>❌ Issue: "Port 8501 is already in use"</strong></summary>

**Cause:** Another Streamlit application is running

**Solutions:**
```bash
# 1. Use different port
streamlit run app.py --server.port 8502

# 2. Kill existing Streamlit processes
# Find process ID
ps aux | grep streamlit

# Kill process (replace XXXX with actual PID)
kill XXXX

# 3. Or restart terminal/command prompt
```

</details>

<details>
<summary><strong>❌ Issue: Application loads but predictions fail</strong></summary>

**Cause:** Model file corrupted or incompatible

**Solutions:**
```bash
# 1. Check model file size
ls -lh heart_disease_model.pkl

# 2. Test loading model in Python
python -c "import pickle; model = pickle.load(open('heart_disease_model.pkl', 'rb')); print('Model loaded successfully')"

# 3. If error occurs, you may need to retrain the model
# Check for training scripts or notebooks
```

</details>

### **Performance Issues**

<details>
<summary><strong>🐌 Issue: Slow application loading</strong></summary>

**Solutions:**
```bash
# 1. Check system resources
# Ensure sufficient RAM (4GB+)

# 2. Close unnecessary applications

# 3. Try running with optimizations
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false

# 4. Check for large files in directory
du -sh *
```

</details>

---

## ⚙️ **Advanced Configuration**

### **Custom Port Configuration**

```bash
# Run on specific port
streamlit run app.py --server.port 8080

# Run on all network interfaces
streamlit run app.py --server.address 0.0.0.0

# Disable CORS (for development only)
streamlit run app.py --server.enableCORS false
```

### **Environment Variables Setup**

Create a `.streamlit/config.toml` file:

```toml
[server]
port = 8501
address = "localhost"
maxUploadSize = 200

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

### **Production Deployment**

<details>
<summary><strong>🌐 Deploy to Streamlit Cloud</strong></summary>

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect GitHub account
   - Select repository: `VasanthPrakasam/Heart_Prediction`
   - Click "Deploy"

</details>

<details>
<summary><strong>🐳 Docker Deployment</strong></summary>

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t heart-disease-app .
docker run -p 8501:8501 heart-disease-app
```

</details>

---

## 🎯 **Next Steps**

### **Immediate Actions:**
1. ✅ **Test the application** with different input combinations
2. 📊 **Explore the dashboard** features and visualizations  
3. 🧪 **Try edge cases** to understand model behavior
4. 📖 **Read the medical parameter** descriptions

### **Enhancement Ideas:**
- 🎨 **Customize UI** with personal branding
- 📊 **Add more visualizations** (confusion matrix, ROC curves)
- 🔍 **Implement model interpretation** (SHAP values)
- 💾 **Add data export** functionality
- 🔐 **Implement user authentication**

### **Learning Opportunities:**
- 📚 **Study the ML model** training process
- 🧠 **Learn about cardiovascular** risk factors
- 🔬 **Explore data science** concepts
- 🌐 **Practice web development** with Streamlit

---

## 🆘 **Getting Help**

### **Support Channels:**
- 🐛 **GitHub Issues**: [Report bugs](https://github.com/VasanthPrakasam/Heart_Prediction/issues)
- 💬 **Streamlit Community**: [community.streamlit.io](https://community.streamlit.io)
- 📚 **Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- 🎓 **Tutorials**: [streamlit.io/gallery](https://streamlit.io/gallery)

### **Useful Commands Summary:**

```bash
# Quick setup
git clone https://github.com/VasanthPrakasam/Heart_Prediction.git
cd Heart_Prediction
python -m venv heart_disease_env
source heart_disease_env/bin/activate  # or heart_disease_env\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py

# Troubleshooting
pip list                              # Check installed packages
python -c "import streamlit"         # Test streamlit import
ls -la *.pkl                        # Check model file
streamlit run app.py --server.port 8502  # Use different port
```

---

<div align="center">

**🎉 Congratulations! Your Heart Disease Prediction App is Ready! 🎉**

**⭐ Star the repository if this guide helped you! ⭐**

[🔝 Back to Top](#-heart-disease-prediction---complete-setup-guide)

</div>
