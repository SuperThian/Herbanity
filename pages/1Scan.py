import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import altair as alt
import torch
import torch.nn as nn
import torchvision.models as models
import torch.nn.functional as F
from torchvision import transforms

# Page configuration
st.set_page_config(page_title="Scan Tanaman Herbal | Herbanity", page_icon="🌿", layout="centered")

# Modern CSS with animations matching the theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Orbitron:wght@400;500;600;700&display=swap');
    
    /* Root variables for dark green theme */
    :root {
        --bg-dark: #0a0f0a;
        --bg-gradient-start: #0f1f0f;
        --bg-gradient-end: #1a2f1a;
        --primary-green: #39ff14;
        --secondary-green: #00ff41;
        --accent-green: #32cd32;
        --dark-green: #004d00;
        --card-bg: rgba(15, 31, 15, 0.9);
        --card-border: rgba(57, 255, 20, 0.3);
        --text-primary: #ffffff;
        --text-secondary: #b8f5b8;
        --glow: 0 0 20px rgba(57, 255, 20, 0.5);
        --glow-strong: 0 0 30px rgba(57, 255, 20, 0.8);
        --shadow-neon: 0 0 40px rgba(57, 255, 20, 0.3);
    }
    
    /* Global styling with dark theme */
    .stApp {
        background: radial-gradient(ellipse at center, var(--bg-gradient-start) 0%, var(--bg-dark) 100%);
        color: var(--text-primary);
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
    }
    
    /* Animated background particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, var(--primary-green), transparent),
            radial-gradient(2px 2px at 40px 70px, var(--secondary-green), transparent),
            radial-gradient(1px 1px at 90px 40px, var(--accent-green), transparent),
            radial-gradient(1px 1px at 130px 80px, var(--primary-green), transparent),
            radial-gradient(2px 2px at 160px 30px, var(--secondary-green), transparent);
        background-repeat: repeat;
        background-size: 200px 100px;
        animation: sparkle 20s linear infinite;
        opacity: 0.3;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes sparkle {
        0% { transform: translateY(0px) translateX(0px); }
        100% { transform: translateY(-100px) translateX(100px); }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header[data-testid="stHeader"] {display: none;}
    
    /* Main header with glow effect */
    .page-header {
        text-align: center;
        padding: 3rem 2rem;
        background: var(--card-bg);
        border-radius: 20px;
        box-shadow: var(--shadow-neon);
        margin-bottom: 2rem;
        border: 2px solid var(--card-border);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .page-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(57, 255, 20, 0.1), transparent);
        animation: scan 3s linear infinite;
    }
    
    @keyframes scan {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
    }
    
    .page-title {
        font-size: 3.5rem;
        font-weight: 800;
        font-family: 'Orbitron', monospace;
        background: linear-gradient(135deg, var(--primary-green) 0%, var(--secondary-green) 50%, var(--accent-green) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        text-shadow: var(--glow);
        animation: glow-pulse 2s ease-in-out infinite alternate;
        position: relative;
        z-index: 1;
    }
    
    @keyframes glow-pulse {
        0% { filter: brightness(1) drop-shadow(0 0 10px var(--primary-green)); }
        100% { filter: brightness(1.2) drop-shadow(0 0 20px var(--secondary-green)); }
    }
    
    .page-subtitle {
        color: var(--text-secondary);
        font-size: 1.3rem;
        font-weight: 400;
        position: relative;
        z-index: 1;
        text-shadow: 0 0 10px rgba(184, 245, 184, 0.5);
    }
    
    /* Camera toggle button with modern design */
    .camera-toggle-container {
        text-align: center;
        margin: 2rem 0;
    }
    
    .toggle-btn {
        background: linear-gradient(135deg, var(--dark-green) 0%, var(--primary-green) 100%);
        color: var(--bg-dark);
        padding: 1.2rem 2.5rem;
        border-radius: 15px;
        font-size: 1.2rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: var(--glow);
        border: 2px solid var(--primary-green);
        display: inline-block;
        text-decoration: none;
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .toggle-btn::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .toggle-btn:hover::before {
        left: 100%;
    }
    
    .toggle-btn:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--glow-strong);
        background: linear-gradient(135deg, var(--primary-green) 0%, var(--secondary-green) 100%);
    }
    
    .camera-active {
        background: linear-gradient(135deg, #ff4444 0%, #ff6b6b 100%);
        border-color: #ff4444;
        animation: pulse-red 2s infinite;
    }
    
    @keyframes pulse-red {
        0% { box-shadow: 0 0 20px rgba(255, 68, 68, 0.5); }
        50% { box-shadow: 0 0 30px rgba(255, 68, 68, 0.8); }
        100% { box-shadow: 0 0 20px rgba(255, 68, 68, 0.5); }
    }
    
    /* Input sections with neon styling */
    .input-section {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow-neon);
        border: 2px solid var(--card-border);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .input-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--primary-green), transparent);
        animation: scan-line 2s linear infinite;
    }
    
    @keyframes scan-line {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .input-section:hover {
        transform: translateY(-5px);
        box-shadow: var(--glow-strong);
        border-color: var(--primary-green);
    }
    
    .section-header {
        font-size: 1.6rem;
        font-weight: 700;
        color: var(--primary-green);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        text-shadow: var(--glow);
        font-family: 'Orbitron', monospace;
    }
    
    .upload-area {
        border: 3px dashed var(--card-border);
        border-radius: 15px;
        padding: 3rem;
        text-align: center;
        background: linear-gradient(135deg, rgba(57, 255, 20, 0.05) 0%, rgba(0, 255, 65, 0.05) 100%);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .upload-area:hover {
        border-color: var(--primary-green);
        background: linear-gradient(135deg, rgba(57, 255, 20, 0.1) 0%, rgba(0, 255, 65, 0.1) 100%);
        box-shadow: inset var(--glow);
    }
    
    .camera-inactive {
        background: rgba(100, 100, 100, 0.1);
        color: #666;
        border-color: #444;
    }
    
    /* Results section with enhanced styling */
    .result-container {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: var(--shadow-neon);
        border-left: 5px solid var(--accent-green);
        border: 2px solid var(--card-border);
        backdrop-filter: blur(15px);
        position: relative;
    }
    
    .result-header {
        font-size: 2rem;
        font-weight: 700;
        color: var(--primary-green);
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        text-shadow: var(--glow);
        font-family: 'Orbitron', monospace;
    }
    
    .prediction-success {
        background: linear-gradient(135deg, var(--accent-green) 0%, var(--secondary-green) 100%);
        color: var(--bg-dark);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: var(--glow);
        animation: success-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes success-glow {
        0% { box-shadow: var(--glow); }
        100% { box-shadow: var(--glow-strong); }
    }
    
    .prediction-failed {
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(57, 255, 20, 0.1) 0%, var(--card-bg) 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-top: 1.5rem;
        border: 2px solid var(--card-border);
        backdrop-filter: blur(10px);
    }
    
    .info-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--primary-green);
        margin-bottom: 1rem;
        text-shadow: var(--glow);
    }
    
    .confidence-badge {
        background: var(--accent-green);
        color: var(--bg-dark);
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-weight: 700;
        display: inline-block;
        margin-top: 1rem;
        box-shadow: var(--glow);
        font-size: 1.1rem;
    }
    
    /* Chart styling with neon theme */
    .chart-container {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: var(--shadow-neon);
        border: 2px solid var(--card-border);
        backdrop-filter: blur(10px);
    }
    
    .chart-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--primary-green);
        margin-bottom: 1.5rem;
        text-align: center;
        text-shadow: var(--glow);
        font-family: 'Orbitron', monospace;
    }
    
    /* Navigation buttons */
    .nav-buttons {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-top: 3rem;
    }
    
    /* Button styling with neon effect */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, var(--dark-green) 0%, var(--primary-green) 100%);
        color: var(--bg-dark);
        font-weight: 700;
        border: 2px solid var(--primary-green);
        border-radius: 12px;
        padding: 1rem 2rem;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: var(--glow);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, var(--primary-green) 0%, var(--secondary-green) 100%);
        transform: translateY(-3px);
        box-shadow: var(--glow-strong);
    }
    
    /* Loading spinner */
    .stSpinner > div {
        border-top-color: var(--primary-green) !important;
        filter: drop-shadow(var(--glow));
    }
    
    /* Success/Error messages */
    .stSuccess {
        background: linear-gradient(135deg, var(--accent-green) 0%, var(--secondary-green) 100%) !important;
        color: var(--bg-dark) !important;
        border: 2px solid var(--primary-green);
        box-shadow: var(--glow);
    }
    
    .stWarning {
        background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%) !important;
        color: white !important;
        box-shadow: 0 0 20px rgba(255, 107, 53, 0.5);
    }
    
    /* Footer with neon styling */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2rem;
        color: var(--text-secondary);
        border-top: 2px solid var(--card-border);
        background: var(--card-bg);
        border-radius: 15px;
        box-shadow: var(--shadow-neon);
        backdrop-filter: blur(10px);
    }
    
    .tech-badge {
        display: inline-block;
        background: linear-gradient(135deg, #22ff00, #00ff88);
        color: #0a0f0d;
        border-radius: 25px;
        padding: 0.5rem 1rem;
        margin-right: 0.8rem;
        margin-bottom: 0.8rem;
        font-size: 0.9rem;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(34, 255, 0, 0.3);
        transition: all 0.3s ease;
        cursor: default;
    }
    
    .tech-badge:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(34, 255, 0, 0.4);
    }
            
    /* Glowing text animation */
    .glow-text {
        animation: text-glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes text-glow {
        0% { text-shadow: 0 0 10px var(--primary-green); }
        100% { text-shadow: 0 0 20px var(--secondary-green), 0 0 30px var(--primary-green); }
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .page-title {
            font-size: 2.5rem;
        }
        
        .nav-buttons {
            grid-template-columns: 1fr;
        }
        
        .input-section {
            padding: 1.5rem;
        }
        
        .result-container {
            padding: 1.5rem;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-green);
        border-radius: 4px;
        box-shadow: var(--glow);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--secondary-green);
    }
</style>
""", unsafe_allow_html=True)

# Page header with enhanced design
st.markdown("""
<div class="page-header">
    <div class="page-title">🌿 Scan & Identifikasi Tanaman Herbal</div>
    <div class="page-subtitle">Pilih metode input untuk memulai proses identifikasi dengan teknologi AI</div>
</div>
""", unsafe_allow_html=True)

# Custom ResNet50 model dari training
class ResNet50Classifier(nn.Module):
    def __init__(self, num_classes=4, pretrained=False):
        super(ResNet50Classifier, self).__init__()
        self.backbone = models.resnet50(pretrained=pretrained)
        self.backbone = nn.Sequential(*list(self.backbone.children())[:-1])
        self.classifier = nn.Sequential(
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(2048, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        features = self.backbone(x)
        out = self.classifier(features)
        return out

# Load model and class information
try:
    model = ResNet50Classifier(num_classes=4)
    model.load_state_dict(torch.load("model70.pt", map_location="cpu"))
    model.eval()
    
    class_names = ['Jahe', 'Kencur', 'Kunyit', 'Temulawak']
    class_info = {
        'Jahe': "🔬 Rasa paling pedas dengan bentuk bercabang dan aroma khas yang menyengat. Kaya akan gingerol yang bermanfaat untuk kesehatan.",
        'Kencur': "🔬 Bentuk lebih bulat dan kecil dengan aroma khas yang berbeda dari jahe. Mengandung minyak atsiri yang berkhasiat.",
        'Kunyit': "🔬 Warna jingga cerah di bagian dalam dengan rasa agak pahit namun harum. Mengandung curcumin yang antioksidan tinggi.",
        'Temulawak': "🔬 Rimpang besar dengan warna jingga pucat, rasa pahit dan aroma kuat. Berkhasiat untuk kesehatan liver dan pencernaan."
    }
    threshold = 0.7
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# Initialize camera state
if 'camera_enabled' not in st.session_state:
    st.session_state.camera_enabled = False

# Camera toggle function
def toggle_camera():
    st.session_state.camera_enabled = not st.session_state.camera_enabled

# Camera toggle button with modern styling
st.markdown('<div class="camera-toggle-container">', unsafe_allow_html=True)
if st.session_state.camera_enabled:
    toggle_text = "📷 KAMERA AKTIF - KLIK UNTUK MATIKAN"
    toggle_class = "toggle-btn camera-active"
else:
    toggle_text = "📸 AKTIFKAN KAMERA SCANNER"
    toggle_class = "toggle-btn"

if st.button(toggle_text, key="camera_toggle", on_click=toggle_camera):
    pass

st.markdown('</div>', unsafe_allow_html=True)

def preprocess_image(img):
    """Preprocess image for PyTorch model prediction"""
    try:
        if not isinstance(img, Image.Image):
            img = Image.open(img)

        img = img.convert("RGB")

        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),  # Convert to Tensor [0,1]
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        tensor = transform(img).unsqueeze(0)  # Add batch dim

        return tensor.to(device)

    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

# Prediction function
def predict_herbal(img):
    try:
        if not isinstance(img, Image.Image):
            img = Image.open(img)
        img = img.convert("RGB")

        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        tensor = transform(img).unsqueeze(0)  # Add batch dimension
        outputs = model(tensor)
        probs = F.softmax(outputs, dim=1).detach().numpy()[0]

        predicted_class_index = int(np.argmax(probs))
        confidence = float(probs[predicted_class_index])
        predicted_class = class_names[predicted_class_index]

        return predicted_class, confidence, probs

    except Exception as e:
        st.error(f"Error during prediction: {e}")
        return None, None, None

# Create visualization chart with neon styling
def create_prediction_chart(predictions, class_names):
    """Create a bar chart for prediction probabilities"""
    df = pd.DataFrame({
        'Jenis Tanaman Herbal': class_names,
        'Probabilitas': predictions * 100
    })
    
    chart = alt.Chart(df).mark_bar(
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='#39ff14', offset=0),
                   alt.GradientStop(color='#00ff41', offset=1)]
        ),
        cornerRadiusTopLeft=8,
        cornerRadiusTopRight=8,
        stroke='#39ff14',
        strokeWidth=2
    ).add_selection(
        alt.selection_single()
    ).encode(
        x=alt.X('Jenis Tanaman Herbal:N', sort='-y', title='Jenis Tanaman Herbal'),
        y=alt.Y('Probabilitas:Q', title='Probabilitas (%)'),
        tooltip=['Jenis Tanaman Herbal:N', alt.Tooltip('Probabilitas:Q', format='.1f')]
    ).properties(
        width=400,
        height=300,
        title=alt.TitleParams(
            text='Distribusi Probabilitas Analisis AI',
            fontSize=18,
            fontWeight='bold',
            color='#39ff14'
        )
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14,
        titleColor='#39ff14',
        labelColor='#b8f5b8',
        gridColor='#2a4a2a'
    ).configure_title(
        fontSize=18,
        fontWeight='bold',
        color='#39ff14'
    ).configure_view(
        strokeWidth=0
    )
    
    return chart

# Input sections with enhanced styling
col1, col2 = st.columns(2)

# Camera input
with col1:
    st.markdown('''
    <div class="input-section">
        <div class="section-header">📷 AMBIL GAMBAR</div>
    </div>
    ''', unsafe_allow_html=True)
    
    camera_image = None
    if st.session_state.camera_enabled:
        camera_image = st.camera_input("🎯 Arahkan kamera ke tanaman herbal", help="Pastikan pencahayaan optimal dan objek terlihat jelas")
    else:
        st.markdown("""
        <div class="upload-area camera-inactive">
            <p style="font-size: 1.3rem; margin-bottom: 1rem;">📵 KAMERA TIDAK AKTIF</p>
            <p style="font-size: 1rem; opacity: 0.8;">Aktifkan kamera untuk menggunakan kamera real-time</p>
        </div>
        """, unsafe_allow_html=True)

# File upload input
with col2:
    st.markdown('''
    <div class="input-section">
        <div class="section-header">📁 UPLOAD GAMBAR</div>
    </div>
    ''', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "🎯 Pilih file gambar tanaman herbal...",
        type=['jpg', 'jpeg', 'png'],
        help="Format yang didukung: JPG, JPEG, PNG (Max: 200MB)"
    )

# Process the image
selected_image = None
image_source = ""

if camera_image is not None:
    selected_image = camera_image
    image_source = "scanner real-time"
elif uploaded_file is not None:
    selected_image = uploaded_file
    image_source = "upload digital"

# Display results if image is provided
if selected_image is not None:
    st.markdown("""
    <div class="result-container">
        <div class="result-header">🔍 HASIL ANALISIS AI</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display the image
    col_img, col_result = st.columns([1, 1])
    
    with col_img:
        st.image(selected_image, caption=f"📊 Input dari {image_source}", use_container_width=True)
    
    with col_result:
        with st.spinner("🧠 AI sedang menganalisis gambar..."):
            # Konversi image ke PIL.Image terlebih dahulu
            image_pil = Image.open(selected_image)

            # Make prediction
            predicted_class, confidence, all_predictions = predict_herbal(image_pil)
            
            if predicted_class is not None:
                # Check if confidence meets threshold
                if confidence >= threshold:
                    st.markdown(f"""
                    <div class="prediction-success">
                        <h3 style="margin: 0; font-size: 1.6rem;">✅ TERIDENTIFIKASI SEBAGAI</h3>
                        <h2 style="margin: 1rem 0; font-size: 2.5rem; font-family: 'Orbitron', monospace;">{predicted_class}</h2>
                        <div class="confidence-badge">Akurasi AI: {confidence:.1%}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display class information
                    st.markdown(f"""
                    <div class="info-box">
                        <div class="info-title glow-text">🧬 Analisis {predicted_class}</div>
                        <p style="margin: 0; line-height: 1.8; font-size: 1.1rem;">{class_info[predicted_class]}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                else:
                    st.markdown(f"""
                        <div class="prediction-failed" style="animation: shake 0.5s; border-left: 5px solid #ff6b35;">
                        <h3 style="margin: 0; font-size: 1.6rem;">⚠️ PREDIKSI TIDAK OPTIMAL</h3>
                        <h4 style="margin: 0.5rem 0 1rem 0; font-size: 1.2rem; color: #fff;">🤔 AI mendeteksi <b>{predicted_class}</b> namun dengan confidence score yang rendah.</h4>
                        <p style="font-size: 1.1rem; margin: 0.5rem 0;">🎯 Akurasi Terdeteksi: <span style="font-weight: bold; color: #ffdd57;">{confidence:.1%}</span></p>
                        <p style="font-size: 1rem; margin-top: 1rem;">📸 Tips untuk hasil lebih baik:</p>
                        <ul style="font-size: 0.95rem; line-height: 1.6; margin-left: 1.2rem; color: #eee;">
                            <li>Pastikan pencahayaan cukup terang</li>
                            <li>Fokuskan kamera pada 1 tanaman herbal saja</li>
                            <li>Gunakan background netral agar tidak membingungkan model</li>
                            <li>Ambil gambar dari dekat tanpa blur</li>
                        </ul>
                        <p style="margin-top: 1rem; font-style: italic; color: #ccc;">🔁 Silakan coba lagi dengan gambar lain yang lebih jelas</p>
                    </div>
                """, unsafe_allow_html=True)

                # CSS output — tidak pakai f-string
                st.markdown("""
                <style>
                @keyframes shake {
                    0%   { transform: translateX(0); }
                    25%  { transform: translateX(-5px); }
                    50%  { transform: translateX(5px); }
                    75%  { transform: translateX(-5px); }
                    100% { transform: translateX(0); }
                }
                </style>
                """, unsafe_allow_html=True)
    
    # Display prediction chart
    if all_predictions is not None:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">📊 VISUALISASI DATA ANALISIS</div>
        </div>
        """, unsafe_allow_html=True)
        
        chart = create_prediction_chart(all_predictions, class_names)
        st.altair_chart(chart, use_container_width=True)
        
        # Show detailed probabilities
        st.markdown("### 🎯 Detail Probabilitas AI")
        prob_df = pd.DataFrame({
            'Jenis Tanaman Herbal': class_names,
            'Probabilitas': [f"{prob:.1%}" for prob in all_predictions],
            'Status': ['✅ TINGGI' if prob > 0.5 else '📊 SEDANG' if prob > 0.2 else '❌ RENDAH' for prob in all_predictions]
        })
        st.dataframe(prob_df, use_container_width=True, hide_index=True)

# Navigation buttons
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col_nav1, col_nav2 = st.columns(2)

with col_nav1:
    if st.button("🏠 KEMBALI KE HOME", use_container_width=True):
        st.switch_page("0Home.py")

with col_nav2:
    if st.button("📚 INFO TANAMAN HERBAL", use_container_width=True):
        st.switch_page("pages/2Info_Herbal.py")

st.markdown('</div>', unsafe_allow_html=True)

# Footer section with modern tech styling
st.markdown("""
<div class="footer fade-in-up">
    <h2 style="
    background: linear-gradient(135deg, #00ff88, #22ff00, #44ff22);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    text-align: center;
    margin-bottom: 1rem;
    font-size: 2.2rem;
    font-weight: 700;
    text-shadow: 0 0 30px rgba(34, 255, 0, 0.3);
    animation: glow 2s ease-in-out infinite alternate;
">
    🌿 HERBANITY
</h2>

<p style="color: #e8f5e8; opacity: 0.9; font-size: 1.1rem; line-height: 1.6;">
    Menjelajahi kekayaan alam Indonesia melalui teknologi modern.<br>
    Setiap tanaman herbal memiliki cerita dan manfaat yang luar biasa untuk kesehatan Anda.
</p>
<hr>
<div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap; margin-top: 1.5rem;">
    <span class="tech-badge">🌱 100% Natural</span>
    <span class="tech-badge">🔬 Science-Based</span>
    <span class="tech-badge">💚 Indonesian Heritage</span>
</div>
<p style="margin-top: 2rem; color: #66BB6A; font-size: 0.95rem; opacity: 0.8;">
    © 2025 Herbanity | Powered by Kenny Corenthian
</p>
</div>
""", unsafe_allow_html=True)

# Additional JavaScript for enhanced interactivity
st.markdown("""
<script>
// Add smooth scrolling behavior
document.documentElement.style.scrollBehavior = 'smooth';

// Add loading animation for buttons
document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
});

// Add keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Press 'C' to toggle camera
    if (e.key.toLowerCase() === 'c' && !e.ctrlKey && !e.altKey) {
        const cameraButton = document.querySelector('[data-testid="baseButton-secondary"]');
        if (cameraButton && cameraButton.textContent.includes('KAMERA')) {
            cameraButton.click();
        }
    }
    
    // Press 'H' to go to home
    if (e.key.toLowerCase() === 'h' && !e.ctrlKey && !e.altKey) {
        const homeButton = document.querySelector('button[kind="secondary"]:contains("BERANDA")');
        if (homeButton) {
            homeButton.click();
        }
    }
});

// Add image preview enhancement
function enhanceImagePreview() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.style.transition = 'all 0.3s ease';
        img.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
            this.style.boxShadow = '0 0 30px rgba(57, 255, 20, 0.5)';
        });
        img.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
            this.style.boxShadow = 'none';
        });
    });
}

// Call enhancement function
setTimeout(enhanceImagePreview, 1000);

// Add performance monitoring
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
});

// Observe all sections for smooth reveal
document.querySelectorAll('.input-section, .result-container, .chart-container').forEach(section => {
    section.style.opacity = '0';
    section.style.transform = 'translateY(20px)';
    section.style.transition = 'all 0.6s ease';
    observer.observe(section);
});
</script>
""", unsafe_allow_html=True)