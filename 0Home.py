import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Herbanity 🌿", 
    page_icon="🌿", 
    layout="centered"
)

# Enhanced Custom CSS with modern design and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Root variables for dark green theme */
    :root {
        --primary-dark: #0D1B0F;
        --secondary-dark: #1A2E1D;
        --accent-green: #00E1BB;
        --bright-green: #26a953;
        --neon-green: #30c563;
        --dark-green: #0F2419;
        --card-bg: rgba(26, 46, 29, 0.8);
        --card-border: rgba(0, 255, 136, 0.3);
        --text-primary: #FFFFFF;
        --text-secondary: #B8E6B8;
        --text-accent: #00FF88;
        --shadow: 0 8px 32px rgba(0, 255, 136, 0.15);
        --shadow-hover: 0 16px 48px rgba(0, 255, 136, 0.25);
        --glow: 0 0 20px rgba(0, 255, 136, 0.5);
        --glow-strong: 0 0 40px rgba(0, 255, 136, 0.8);
    }
    
    /* Global styling with dark theme */
    .stApp {
        background: linear-gradient(135deg, var(--primary-dark) 0%, var(--secondary-dark) 50%, var(--dark-green) 100%);
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
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
            radial-gradient(circle at 20% 50%, rgba(0, 255, 136, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(57, 255, 20, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(0, 255, 65, 0.1) 0%, transparent 50%);
        animation: backgroundFloat 20s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes backgroundFloat {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg);
            opacity: 0.3;
        }
        33% { 
            transform: translateY(-20px) rotate(120deg);
            opacity: 0.6;
        }
        66% { 
            transform: translateY(-10px) rotate(240deg);
            opacity: 0.4;
        }
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header {visibility: hidden;}
    
    /* Main container */
    .main-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 2rem 1rem;
        position: relative;
        z-index: 1;
    }
    
    /* Hero section with advanced animations */
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(13, 27, 15, 0.95) 0%, rgba(15, 36, 25, 0.95) 100%);
        border-radius: 24px;
        box-shadow: var(--shadow);
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        border: 1px solid var(--card-border);
        backdrop-filter: blur(10px);
    }
    
    /* Glowing border animation */
    .hero-section::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, var(--accent-green), var(--bright-green), var(--neon-green), var(--accent-green));
        border-radius: 24px;
        z-index: -1;
        animation: borderGlow 3s linear infinite;
        background-size: 400% 400%;
    }
    
    @keyframes borderGlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Floating elements inside hero */
    .hero-section::after {
        content: '';
        position: absolute;
        top: 10%;
        left: 10%;
        font-size: 1.5rem;
        opacity: 0.3;
        animation: floatingElements 8s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes floatingElements {
        0%, 100% { 
            transform: translateY(0px) translateX(0px) rotate(0deg);
            opacity: 0.3;
        }
        25% { 
            transform: translateY(-20px) translateX(10px) rotate(90deg);
            opacity: 0.6;
        }
        50% { 
            transform: translateY(-10px) translateX(-10px) rotate(180deg);
            opacity: 0.4;
        }
        75% { 
            transform: translateY(-30px) translateX(15px) rotate(270deg);
            opacity: 0.5;
        }
    }
    
    /* Main title with glow effect */
    .main-title {
        font-size: 4rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 2;
        text-shadow: 
            0 0 10px var(--accent-green),
            0 0 20px var(--accent-green),
            0 0 30px var(--accent-green),
            0 0 40px var(--accent-green);
        animation: titlePulse 4s ease-in-out infinite;
        letter-spacing: -2px;
        filter: drop-shadow(0 0 20px var(--accent-green));
    }
    
    @keyframes titlePulse {
        0%, 100% { 
            transform: scale(1);
            filter: drop-shadow(0 0 20px var(--accent-green)) brightness(1);
            text-shadow: 
                0 0 10px var(--accent-green),
                0 0 20px var(--accent-green),
                0 0 30px var(--accent-green),
                0 0 40px var(--accent-green);
        }
        50% { 
            transform: scale(1.05);
            filter: drop-shadow(0 0 30px var(--bright-green)) brightness(1.3);
            text-shadow: 
                0 0 15px var(--bright-green),
                0 0 25px var(--bright-green),
                0 0 35px var(--bright-green),
                0 0 45px var(--bright-green);
        }
    }
    
    .subtitle {
        font-size: 1.4rem;
        color: #FFFFFF;
        font-weight: 500;
        line-height: 1.7;
        max-width: 700px;
        margin: 0 auto 2rem;
        position: relative;
        z-index: 2;
        animation: fadeInUp 1s ease-out 0.5s both;
        text-shadow: 
            0 0 5px rgba(255, 255, 255, 0.8),
            0 0 10px rgba(0, 255, 136, 0.6),
            0 0 15px rgba(0, 255, 136, 0.4);
        filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Section styling with glass morphism */
    .section-card {
        background: var(--card-bg);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        box-shadow: var(--shadow);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid var(--card-border);
        backdrop-filter: blur(15px);
        position: relative;
        overflow: hidden;
    }
    
    .section-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 255, 136, 0.1), transparent);
        transition: left 0.8s;
    }
    
    .section-card:hover::before {
        left: 100%;
    }
    
    .section-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: var(--shadow-hover);
        border-color: var(--accent-green);
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: var(--text-accent);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        text-shadow: var(--glow);
    }
    
    .section-description {
        color: var(--text-secondary);
        font-size: 1.2rem;
        line-height: 1.7;
        margin-bottom: 2rem;
    }
    
    /* Advanced button styling */
    .scan-button-container {
        position: center;
        margin: 2rem 0;
    }
    
    /* Feature highlights with hover animations */
    .feature-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-item {
        background: linear-gradient(135deg, var(--card-bg) 0%, rgba(0, 255, 136, 0.1) 100%);
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid var(--card-border);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.8s ease-out both;
    }
    
    .feature-item:nth-child(1) { animation-delay: 0.1s; }
    .feature-item:nth-child(2) { animation-delay: 0.2s; }
    .feature-item:nth-child(3) { animation-delay: 0.3s; }
    .feature-item:nth-child(4) { animation-delay: 0.4s; }
    
    .feature-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, transparent 0%, rgba(0, 255, 136, 0.2) 100%);
        opacity: 0;
        transition: opacity 0.3s;
        border-radius: 16px;
    }
    
    .feature-item:hover::before {
        opacity: 1;
    }
    
    .feature-item:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: var(--glow-strong);
        border-color: var(--accent-green);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        animation: bounce 2s infinite;
        filter: drop-shadow(var(--glow));
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-10px);
        }
        60% {
            transform: translateY(-5px);
        }
    }
    
    .feature-title {
        font-weight: 700;
        color: var(--text-accent);
        margin-bottom: 1rem;
        font-size: 1.2rem;
        text-shadow: var(--glow);
        position: relative;
        z-index: 1;
    }
    
    .feature-desc {
        color: var(--text-secondary);
        font-size: 1rem;
        line-height: 1.5;
        position: relative;
        z-index: 1;
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
            
    /* Footer styling with cyber aesthetics */
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 2.5rem;
        background: linear-gradient(135deg, #0d1a0d 0%, #1a2f1a 50%, #0a0f0a 100%);
        color: #4CAF50;
        border-radius: 20px;
        box-shadow: 
            0 8px 40px rgba(0, 0, 0, 0.4),
            inset 0 1px 0 rgba(76, 175, 80, 0.2);
        border: 1px solid rgba(76, 175, 80, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #4CAF50, transparent);
        animation: scanLine 2s linear infinite;
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
            
    /* Responsive design */
    @media (max-width: 768px) {
        .feature-list {
            grid-template-columns: 1fr;
        }
        
        .main-title {
            font-size: 2.8rem;
        }
        
        .subtitle {
            font-size: 1.2rem;
        }
        
        .hero-section {
            padding: 3rem 1.5rem;
        }
        
        .section-card {
            padding: 2rem;
        }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--primary-dark);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-green);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--bright-green);
    }
    
    /* Loading animation */
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .loading {
        animation: pulse 2s infinite;
    }
    
    /* LONG SCAN BUTTON STYLING - Main scan button with extended width */
    button[data-testid="baseButton-primary"].scan-button,
    div[data-testid="stButton"] button.scan-button {
        background: linear-gradient(135deg, #00ff41 0%, #32ff00 100%) !important;
        color: #0a0f0d !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 1.5rem 4rem !important;
        font-weight: 700 !important;
        font-size: 1.4rem !important;
        box-shadow: 
            0 8px 25px rgba(0, 255, 65, 0.4), 
            0 0 30px rgba(0, 255, 65, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        width: 100% !important;
        max-width: 600px !important;
        height: 80px !important;
        text-transform: none !important;
        letter-spacing: 1px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        position: relative !important;
        overflow: hidden !important;
        margin: 2rem auto !important;
        cursor: pointer !important;
    }
    
    /* Animated gradient background for scan button */
    button[data-testid="baseButton-primary"].scan-button::before,
    div[data-testid="stButton"] button.scan-button::before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: -100% !important;
        width: 100% !important;
        height: 100% !important;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent) !important;
        transition: left 0.8s !important;
        z-index: 1 !important;
    }
    
    button[data-testid="baseButton-primary"].scan-button:hover,
    div[data-testid="stButton"] button.scan-button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 
            0 12px 35px rgba(0, 255, 65, 0.5), 
            0 0 40px rgba(0, 255, 65, 0.4),
            inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
        background: linear-gradient(135deg, #22ff00 0%, #00ff41 100%) !important;
    }
    
    button[data-testid="baseButton-primary"].scan-button:hover::before,
    div[data-testid="stButton"] button.scan-button:hover::before {
        left: 100% !important;
    }
    
    button[data-testid="baseButton-primary"].scan-button:active,
    div[data-testid="stButton"] button.scan-button:active {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 
            0 6px 20px rgba(0, 255, 65, 0.6),
            0 0 25px rgba(0, 255, 65, 0.4) !important;
    }
    
    /* REGULAR BUTTONS STYLING - Smaller buttons for navigation */
    div[data-testid="stButton"] > button:not(.scan-button),
    .stButton > button:not(.scan-button),
    button[kind="primary"]:not(.scan-button),
    button[kind="secondary"]:not(.scan-button) {
        background: #00ff41 !important;
        color: #0a0f0d !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 1rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 4px 15px rgba(0, 255, 65, 0.4), 0 0 20px rgba(0, 255, 65, 0.2) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        height: auto !important;
        text-transform: none !important;
        letter-spacing: normal !important;
        min-height: 60px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    div[data-testid="stButton"] > button:not(.scan-button):hover,
    .stButton > button:not(.scan-button):hover,
    button[kind="primary"]:not(.scan-button):hover,
    button[kind="secondary"]:not(.scan-button):hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 8px 25px rgba(0, 255, 65, 0.5), 0 0 30px rgba(0, 255, 65, 0.3) !important;
        background: #22ff00 !important;
    }
</style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="hero-section">
    <div class="main-title">🌿 Herbanity 🌿</div>
    <div class="subtitle">
        Aplikasi pintar untuk mengidentifikasi tanaman herbal Indonesia menggunakan 
        teknologi <strong>Deep Learning</strong> dan <strong>Computer Vision</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# Feature highlights
st.markdown("""
<div class="feature-list">
    <div class="feature-item">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Akurasi Tinggi</div>
        <div class="feature-desc">Model CNN Xception dengan tingkat akurasi optimal</div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Proses Cepat</div>
        <div class="feature-desc">Hasil identifikasi dalam hitungan detik</div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">📱</div>
        <div class="feature-title">User Friendly</div>
        <div class="feature-desc">Interface sederhana dan mudah digunakan</div>
    </div>
    <div class="feature-item">
        <div class="feature-icon">🌱</div>
        <div class="feature-title">4 Jenis Tanaman</div>
        <div class="feature-desc">Jahe, Kencur, Kunyit, dan Temulawak</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main scan section
st.markdown("""
<div class="section-card">
    <div class="section-header">
        📸 Mulai Klasifikasi
    </div>
    <div class="section-description">
        Unggah foto tanaman herbal atau gunakan kamera untuk mendapatkan hasil identifikasi yang akurat beserta informasi lengkap tentang jenis tanaman herbal yang terdeteksi.
    </div>
</div>
""", unsafe_allow_html=True)

# Long scan button with special container and styling
st.markdown('<div class="scan-button-container" style="width: 100%;">', unsafe_allow_html=True)
if st.button("🔍 MULAI SCAN", key="scan_button", help="Klik untuk memulai proses identifikasi tanaman herbal", type="primary"):
    st.switch_page("pages/1Scan.py")
st.markdown('</div>', unsafe_allow_html=True)

# Information section
st.markdown("""
<div class="section-card">
    <div class="section-header">
        ℹ️ Informasi & Panduan
    </div>
    <div class="section-description">
        Pelajari lebih lanjut tentang aplikasi ini dan dapatkan informasi lengkap mengenai berbagai jenis tanaman herbal yang dapat diidentifikasi.
    </div>
</div>
""", unsafe_allow_html=True)

# Info buttons with regular styling
col1, col2 = st.columns(2)
with col1:
    if st.button("INFO APLIKASI", key="app_info", help="Informasi lengkap tentang Herbanity"):
        st.switch_page("pages/3Info_Aplikasi.py")
with col2:
    if st.button("INFO TANAMAN HERBAL", key="herbal_info", help="Panduan lengkap tentang jenis-jenis tanaman herbal"):
        st.switch_page("pages/2Info_Herbal.py")

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

st.markdown('</div>', unsafe_allow_html=True)