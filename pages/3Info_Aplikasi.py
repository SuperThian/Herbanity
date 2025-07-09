import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Info Aplikasi | Herbanity", 
    page_icon="📄",
    layout="centered"
)

# Enhanced Custom CSS with beautiful green color palette
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0a0f0d 0%, #1a2e23 50%, #0d1b11 100%);
        min-height: 100vh;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #00ff88, #22ff00, #44ff22);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-align: center;
        text-shadow: 0 0 30px rgba(34, 255, 0, 0.3);
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { filter: drop-shadow(0 0 5px rgba(34, 255, 0, 0.3)); }
        to { filter: drop-shadow(0 0 15px rgba(34, 255, 0, 0.6)); }
    }
    
    .section {
        background: linear-gradient(145deg, #1e3a2a, #0f2318);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(34, 255, 0, 0.2);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1),
            0 0 20px rgba(34, 255, 0, 0.1);
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, #22ff00, transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    
    .section-title {
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        color: #00ff88;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .text-content {
        text-align: justify; 
        font-size: 1.1rem;
        line-height: 1.8;
        color: #e8f5e8;
        font-weight: 400;
    }
    
    .benefits-box {
        background: linear-gradient(145deg, #0f2318, #1a3426);
        border-radius: 15px;
        padding: 1.5rem;
        margin-top: 1.5rem;
        border: 1px solid rgba(0, 255, 136, 0.3);
        box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    .benefit-item {
        margin-bottom: 1.2rem;
        padding: 1rem;
        background: rgba(34, 255, 0, 0.05);
        border-radius: 10px;
        border-left: 3px solid #00ff88;
        transition: all 0.3s ease;
    }
    
    .benefit-item:hover {
        background: rgba(34, 255, 0, 0.1);
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(34, 255, 0, 0.2);
    }
    
    .highlight {
        font-weight: 600;
        color: #00ff88;
        text-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
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
    
    .back-button {
        margin-top: 3rem;
        text-align: center;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #22ff00, #00ff88) !important;
        color: #0a0f0d !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        box-shadow: 0 6px 25px rgba(34, 255, 0, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 35px rgba(34, 255, 0, 0.4) !important;
        background: linear-gradient(135deg, #00ff88, #44ff22) !important;
    }
    
    .stButton > button:active {
        transform: translateY(-1px) !important;
    }
    
    .footer hr {
        border: none;
        height: 2px;
        background: linear-gradient(135deg, #4CAF50 0%, #66BB6A 100%);
        border-radius: 2px;
        margin: 1.5rem 0;
        box-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Custom animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .slide-in-left {
        animation: slideInLeft 0.6s cubic-bezier(0.4, 0, 0.2, 1);
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
    
    /* Enhanced floating animation for emojis */
    .floating-emoji {
        animation: float 3s ease-in-out infinite;
        display: inline-block;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0f0d;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #22ff00, #00ff88);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #00ff88, #44ff22);
    }
    
    /* Additional enhancements */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1000px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.2rem;
        }
        
        .section {
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }
        
        .section-title {
            font-size: 1.5rem;
        }
        
        .text-content {
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header with enhanced styling
st.markdown("<div class='main-title'><span class='floating-emoji'>📄</span> Tentang Herbanity <span class='floating-emoji'>🌿</span></div>", unsafe_allow_html=True)

# Main Description Section
st.markdown("""
<div class='section'>
    <div class='section-title'><span class='floating-emoji'>🌿</span> Apa itu Herbanity?</div>
    <div class='text-content'>
        Herbanity adalah aplikasi berbasis kecerdasan buatan yang dikembangkan khusus untuk mengenali dan mengklasifikasikan jenis tanaman herbal lokal Indonesia. 
        Aplikasi ini dapat mengidentifikasi berbagai jenis tanaman herbal seperti <span class='highlight'>jahe</span>, 
        <span class='highlight'>kunyit</span>, <span class='highlight'>kencur</span>, dan <span class='highlight'>temulawak</span> 
        berdasarkan gambar yang diunggah oleh pengguna.
    </div>
</div>
""", unsafe_allow_html=True)

# Technology Section
st.markdown("""
<div class='section'>
    <div class='section-title'><span class='floating-emoji'>🔬</span> Teknologi yang Digunakan</div>
    <div class='text-content'>
        Model klasifikasi menggunakan Convolutional Neural Network (CNN) dengan arsitektur <span class='highlight'>ResNet50</span>. 
        Model ini dilatih menggunakan dataset yang terdiri dari 1200 gambar tanaman herbal yang telah diproses ke ukuran standar 224x224 piksel 
        untuk memastikan konsistensi dan akurasi dalam pengenalan pola.
        <br><br>
        Teknologi yang diimplementasikan:
    </div>
    <div style='margin-top: 1.5rem;'>
        <span class='tech-badge'>🧠 Deep Learning</span>
        <span class='tech-badge'>🐍 Python</span>
        <span class='tech-badge'>🔧 PyTorch</span>
        <span class='tech-badge'>⚡ ResNet50</span>
        <span class='tech-badge'>🚀 Streamlit</span>
        <span class='tech-badge'>👁️ Computer Vision</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Benefits Section
st.markdown("""
<div class='section'>
    <div class='section-title'><span class='floating-emoji'>🎯</span> Manfaat Aplikasi</div>
    <div class='text-content'>
        Herbanity dirancang untuk memberikan berbagai manfaat baik dalam bidang pendidikan, 
        penelitian, maupun penerapan teknologi dalam pertanian:
    </div>
    <div class='benefits-box'>
        <div class='benefit-item'>
            <span class='highlight'>📱 Digitalisasi identifikasi tanaman obat</span>
            <br><br>
            Mempermudah proses identifikasi tanaman herbal tradisional menggunakan teknologi modern yang mudah diakses melalui smartphone.
        </div>
        <div class='benefit-item'>
            <span class='highlight'>🔍 Mendukung edukasi dan riset herbal</span>
            <br><br>
            Menyediakan alat bantu untuk peneliti, mahasiswa, dan praktisi herbal dalam mengidentifikasi jenis tanaman dengan cepat dan akurat.
        </div>
        <div class='benefit-item'>
            <span class='highlight'>🌱 Aplikasi pertanian pintar dan agritech</span>
            <br><br>
            Mendukung perkembangan pertanian pintar dengan implementasi kecerdasan buatan untuk peningkatan produktivitas dan kualitas hasil panen.
        </div>
        <div class='benefit-item'>
            <span class='highlight'>🏥 Pengembangan pengobatan tradisional</span>
            <br><br>
            Membantu pelestarian dan pengembangan pengetahuan pengobatan tradisional dengan memudahkan identifikasi bahan-bahan herbal.
        </div>
        <div class='benefit-item'>
            <span class='highlight'>🧠 Transfer knowledge</span>
            <br><br>
            Mentransfer pengetahuan dari generasi ke generasi mengenai kekayaan tanaman obat Indonesia melalui platform digital yang modern.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Dataset Information
st.markdown("""
<div class='section'>
    <div class='section-title'><span class='floating-emoji'>📊</span> Informasi Dataset</div>
    <div class='text-content'>
        Dataset yang digunakan untuk pelatihan model terdiri dari total <span class='highlight'>400 citra</span> tanaman herbal yang terbagi ke dalam 4 kelas utama, yaitu: <span class='highlight'>jahe</span>, <span class='highlight'>kencur</span>, <span class='highlight'>kunyit</span>, dan <span class='highlight'>temulawak</span>.
        <br><br>
        Seluruh gambar dikumpulkan melalui proses dokumentasi manual menggunakan kamera smartphone, dengan memperhatikan berbagai sudut pengambilan, pencahayaan alami, dan latar belakang yang bervariasi untuk meningkatkan keragaman visual. Hal ini bertujuan agar model mampu mengenali objek dalam kondisi nyata secara lebih akurat.
        <br><br>
        Semua gambar ini juga telah melalui proses <span class='highlight'>augmentasi data</span> untuk meningkatkan variasi dataset, termasuk rotasi, 
        pergeseran, pembesaran, dan normalisasi untuk mengoptimalkan kinerja model.
    </div>
</div>
""", unsafe_allow_html=True)

# Back Button
st.markdown("<div class='back-button'>", unsafe_allow_html=True)
if st.button("🏠 Kembali ke Home", use_container_width=True):
    st.switch_page("0Home.py")
st.markdown("</div>", unsafe_allow_html=True)

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