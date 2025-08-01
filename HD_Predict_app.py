import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main background and styling */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Custom header styling */
    .custom-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .custom-header h1 {
        color: white;
        text-align: center;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .custom-header p {
        color: rgba(255,255,255,0.9);
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 0;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    
    /* Results styling */
    .result-positive {
        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(238, 90, 82, 0.3);
    }
    
    .result-negative {
        background: linear-gradient(135deg, #51cf66, #40c057);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(64, 192, 87, 0.3);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load the saved machine learning model
@st.cache_resource
def load_model():
    try:
        return pickle.load(open('heart_disease_model.pkl', 'rb'))
    except FileNotFoundError:
        st.error("❌ Model file 'heart_disease_model.pkl' not found. Please ensure the model file is in the same directory.")
        return None

model = load_model()

# Function to predict heart disease based on input values
def predict_heart_disease(age, sex, chest_pain, bp, cholesterol, sugar, ecg, max_heart_rate,
                          angina, st_depression, st_slope, vessels, thalassemia):
    if model is None:
        return None
    
    # Convert all input values into a numpy array
    input_data = np.array([[age, sex, chest_pain, bp, cholesterol, sugar, ecg,
                            max_heart_rate, angina, st_depression, st_slope, vessels, thalassemia]])
    
    # Use the model to make a prediction (0 = No Disease, 1 = Disease)
    prediction = model.predict(input_data)
    return prediction[0]

# Function to create a risk assessment gauge
def create_risk_gauge(risk_score):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = risk_score * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Risk Level (%)"},
        delta = {'reference': 50},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 70
            }
        }
    ))
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Function to create input summary chart
def create_input_summary(inputs):
    categories = ['Age', 'BP', 'Cholesterol', 'Heart Rate', 'ST Depression']
    values = [
        inputs['age'] / 100 * 100,
        inputs['bp'] / 200 * 100,
        inputs['cholesterol'] / 600 * 100,
        inputs['max_heart_rate'] / 220 * 100,
        inputs['st_depression'] / 6 * 100
    ]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='rgb(102, 126, 234)',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        height=400,
        title="Health Parameters Overview"
    )
    return fig

# Streamlit web app starts here
def app():
    # Custom header
    st.markdown("""
    <div class="custom-header">
        <h1>❤️ Heart Disease Risk Predictor</h1>
        <p>Advanced AI-powered cardiovascular risk assessment tool</p>
    </div>
    """, unsafe_allow_html=True)
    
    if model is None:
        return
    
    # Sidebar for information
    with st.sidebar:
        st.markdown("### 📊 About This Tool")
        st.markdown("""
        <div class="info-card">
            <h4>🎯 Purpose</h4>
            <p>This application uses machine learning to assess cardiovascular risk based on clinical parameters.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4>⚠️ Important Notice</h4>
            <p>This tool is for educational purposes only. Always consult healthcare professionals for medical decisions.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-card">
            <h4>📅 Last Updated</h4>
            <p>{}</p>
        </div>
        """.format(datetime.now().strftime("%B %d, %Y")), unsafe_allow_html=True)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📝 Patient Information")
        
        # Basic Demographics
        with st.expander("👤 Demographics", expanded=True):
            col_age, col_sex = st.columns(2)
            with col_age:
                age = st.slider('Age (years)', 20, 100, 50, help="Patient's age in years")
            with col_sex:
                sex = st.selectbox('Sex', options=[('Male', 1), ('Female', 0)], format_func=lambda x: x[0])[1]
        
        # Cardiovascular Symptoms
        with st.expander("💓 Cardiovascular Symptoms", expanded=True):
            chest_pain = st.selectbox(
                'Chest Pain Type',
                options=[('Typical Angina', 0), ('Atypical Angina', 1), ('Non-Anginal Pain', 2), ('Asymptomatic', 3)],
                format_func=lambda x: x[0],
                help="Type of chest pain experienced"
            )[1]
            
            angina = st.selectbox('Exercise Induced Angina', 
                                options=[('Yes', 1), ('No', 0)], 
                                format_func=lambda x: x[0],
                                help="Does exercise induce chest pain?")[1]
        
        # Vital Signs
        with st.expander("🩺 Vital Signs & Lab Results", expanded=True):
            col_bp, col_chol = st.columns(2)
            with col_bp:
                bp = st.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120, 
                             help="Blood pressure when at rest")
            with col_chol:
                cholesterol = st.slider('Serum Cholesterol (mg/dL)', 100, 600, 200,
                                      help="Total cholesterol level in blood")
            
            col_sugar, col_hr = st.columns(2)
            with col_sugar:
                sugar = st.selectbox('Fasting Blood Sugar > 120 mg/dL?', 
                                   options=[('Yes', 1), ('No', 0)], 
                                   format_func=lambda x: x[0],
                                   help="Is fasting blood sugar elevated?")[1]
            with col_hr:
                max_heart_rate = st.slider('Maximum Heart Rate Achieved', 70, 220, 150,
                                         help="Highest heart rate during exercise test")
        
        # Diagnostic Tests
        with st.expander("🔬 Diagnostic Test Results", expanded=True):
            ecg = st.selectbox(
                'Resting ECG Result',
                options=[('Normal', 0), ('ST-T Abnormality', 1), ('Left Ventricular Hypertrophy', 2)],
                format_func=lambda x: x[0],
                help="Electrocardiogram findings at rest"
            )[1]
            
            col_dep, col_slope = st.columns(2)
            with col_dep:
                st_depression = st.slider('ST Depression (Oldpeak)', 0.0, 6.0, 1.0, step=0.1,
                                        help="ST depression induced by exercise relative to rest")
            with col_slope:
                st_slope = st.selectbox(
                    'ST Segment Slope',
                    options=[('Upsloping', 0), ('Flat', 1), ('Downsloping', 2)],
                    format_func=lambda x: x[0],
                    help="Slope of peak exercise ST segment"
                )[1]
            
            col_vessels, col_thal = st.columns(2)
            with col_vessels:
                vessels = st.selectbox('Major Vessels (Fluoroscopy)', [0, 1, 2, 3],
                                     help="Number of major vessels colored by fluoroscopy")
            with col_thal:
                thalassemia = st.selectbox(
                    'Thalassemia Type',
                    options=[('Normal', 1), ('Fixed Defect', 2), ('Reversible Defect', 3)],
                    format_func=lambda x: x[0],
                    help="Thalassemia blood disorder status"
                )[1]
        
        # Prediction button
        st.markdown("---")
        predict_button = st.button('🔍 Analyze Risk', type="primary")
    
    with col2:
        st.markdown("### 📈 Analysis Dashboard")
        
        # Input summary
        input_data = {
            'age': age,
            'bp': bp,
            'cholesterol': cholesterol,
            'max_heart_rate': max_heart_rate,
            'st_depression': st_depression
        }
        
        # Display radar chart
        fig_radar = create_input_summary(input_data)
        st.plotly_chart(fig_radar, use_container_width=True)
        
        # Risk factors summary
        st.markdown("#### 🎯 Key Metrics")
        
        # Color coding for metrics
        age_color = "🟡" if age > 60 else "🟢"
        bp_color = "🔴" if bp > 140 else "🟡" if bp > 120 else "🟢"
        chol_color = "🔴" if cholesterol > 240 else "🟡" if cholesterol > 200 else "🟢"
        
        st.markdown(f"""
        <div class="metric-card">
            {age_color} <strong>Age:</strong> {age} years<br>
            {bp_color} <strong>Blood Pressure:</strong> {bp} mm Hg<br>
            {chol_color} <strong>Cholesterol:</strong> {cholesterol} mg/dL
        </div>
        """, unsafe_allow_html=True)
    
    # Prediction results
    if predict_button:
        with st.spinner('🔄 Analyzing patient data...'):
            result = predict_heart_disease(age, sex, chest_pain, bp, cholesterol, sugar, ecg,
                                         max_heart_rate, angina, st_depression, st_slope, vessels, thalassemia)
            
            st.markdown("---")
            st.markdown("### 📊 Risk Assessment Results")
            
            col_result, col_gauge = st.columns([1, 1])
            
            with col_result:
                if result == 0:
                    st.markdown("""
                    <div class="result-negative">
                        ✅ LOW RISK<br>
                        <small>The analysis suggests a lower probability of heart disease</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.success("💚 **Good News!** Based on the provided parameters, the risk appears to be lower.")
                    st.info("🏥 **Recommendation:** Continue regular health checkups and maintain a healthy lifestyle.")
                    
                else:
                    st.markdown("""
                    <div class="result-positive">
                        ⚠️ ELEVATED RISK<br>
                        <small>The analysis indicates potential cardiovascular concerns</small>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.error("🚨 **Important:** The analysis suggests elevated risk factors.")
                    st.warning("🏥 **Urgent Recommendation:** Please consult a cardiologist for comprehensive evaluation.")
            
            with col_gauge:
                # Create risk gauge
                risk_score = result  # 0 or 1, can be converted to probability if model supports it
                fig_gauge = create_risk_gauge(risk_score)
                st.plotly_chart(fig_gauge, use_container_width=True)
            
            # Additional recommendations
            st.markdown("### 💡 Health Recommendations")
            
            recommendations = []
            if bp > 140:
                recommendations.append("🩺 Monitor blood pressure regularly")
            if cholesterol > 240:
                recommendations.append("🥗 Consider dietary changes to reduce cholesterol")
            if age > 60:
                recommendations.append("👨‍⚕️ Schedule regular cardiac screenings")
            if max_heart_rate < 100:
                recommendations.append("🏃‍♂️ Discuss exercise capacity with your doctor")
            
            if recommendations:
                for rec in recommendations:
                    st.markdown(f"- {rec}")
            else:
                st.markdown("- 💪 Maintain current healthy lifestyle")
                st.markdown("- 🏃‍♂️ Continue regular exercise routine")
                st.markdown("- 🥗 Keep balanced diet")

# Run the Streamlit app
if __name__ == '__main__':
    app()