import streamlit as st

st.set_page_config(page_title="Tentang Herbanity", page_icon="🌱", layout="wide")

# Enhanced CSS with modern green tech color scheme and animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
            
    /* Main app styling with dark green tech theme */
    .stApp {
        background: linear-gradient(135deg, #0a0f0a 0%, #1a2f1a 50%, #0d1a0d 100%);
        font-family: 'Inter', sans-serif;
        color: #e8f5e8;
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
            radial-gradient(circle at 20% 80%, rgba(76, 175, 80, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(129, 199, 132, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(102, 187, 106, 0.05) 0%, transparent 50%);
        animation: backgroundFloat 20s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes backgroundFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-20px) rotate(1deg); }
        66% { transform: translateY(10px) rotate(-1deg); }
    }
    
    /* Header styling with glow effect */
    .main-title {
        text-align: center;
        color: #4CAF50;
        font-weight: 800;
        font-size: 2.8rem;
        margin-bottom: 2rem;
        text-shadow: 0 0 20px rgba(76, 175, 80, 0.5), 0 0 40px rgba(76, 175, 80, 0.3);
        animation: titlePulse 3s ease-in-out infinite;
    }
    
    @keyframes titlePulse {
        0%, 100% { text-shadow: 0 0 20px rgba(76, 175, 80, 0.5), 0 0 40px rgba(76, 175, 80, 0.3); }
        50% { text-shadow: 0 0 30px rgba(76, 175, 80, 0.8), 0 0 60px rgba(76, 175, 80, 0.5); }
    }
    
    /* Custom container with glassmorphism */
    .content-container {
        background: rgba(26, 47, 26, 0.8);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(76, 175, 80, 0.2);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(76, 175, 80, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .content-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    /* Expander styling with modern tech look */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #1a2f1a 0%, #2d4a2d 100%) !important;
        color: #4CAF50 !important;
        border-radius: 15px !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        padding: 1.2rem !important;
        margin-bottom: 0.5rem !important;
        box-shadow: 
            0 4px 20px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(76, 175, 80, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: 1px solid rgba(76, 175, 80, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .streamlit-expanderHeader::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.2), transparent);
        transition: left 0.6s;
    }
    
    .streamlit-expanderHeader:hover::before {
        left: 100%;
    }
    
    .streamlit-expanderHeader:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 
            0 8px 30px rgba(76, 175, 80, 0.4),
            inset 0 1px 0 rgba(76, 175, 80, 0.5) !important;
        border-color: rgba(76, 175, 80, 0.6) !important;
    }
    
    .streamlit-expanderContent {
        background: rgba(13, 26, 13, 0.9) !important;
        border-radius: 0 0 15px 15px !important;
        border: 2px solid rgba(76, 175, 80, 0.2) !important;
        border-top: none !important;
        padding: 2rem !important;
        box-shadow: 
            0 4px 20px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(76, 175, 80, 0.1) !important;
        backdrop-filter: blur(10px) !important;
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
    
    /* Image styling with cyber frame */
    .stImage > img {
        border-radius: 15px !important;
        box-shadow: 
            0 8px 30px rgba(0, 0, 0, 0.4),
            0 0 20px rgba(76, 175, 80, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: 2px solid rgba(76, 175, 80, 0.3) !important;
    }
    
    .stImage > img:hover {
        transform: scale(1.05) rotate(1deg) !important;
        box-shadow: 
            0 15px 50px rgba(0, 0, 0, 0.6),
            0 0 40px rgba(76, 175, 80, 0.6) !important;
        border-color: rgba(76, 175, 80, 0.8) !important;
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
    
    /* Content text styling */
    .stMarkdown h3 {
        color: #4CAF50 !important;
        font-weight: 700 !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        text-shadow: 0 0 10px rgba(76, 175, 80, 0.3) !important;
    }
    
    .stMarkdown h4 {
        color: #66BB6A !important;
        font-weight: 600 !important;
        margin-top: 1.5rem !important;
    }
    
    .stMarkdown p {
        color: #e8f5e8 !important;
        line-height: 1.7 !important;
        margin-bottom: 1rem !important;
    }
    
    .stMarkdown ul {
        color: #e8f5e8 !important;
        line-height: 1.7 !important;
    }
    
    .stMarkdown strong {
        color: #4CAF50 !important;
        font-weight: 600 !important;
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
            
    .back-button {
        margin-top: 3rem;
        text-align: center;
    }
    
    @keyframes scanLine {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
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
    
    @keyframes glow {
        0% {
            text-shadow: 0 0 10px rgba(34, 255, 0, 0.2);
        }
        100% {
            text-shadow: 0 0 30px rgba(34, 255, 0, 0.6);
        }
    }

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
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.2rem;
        }
        
        .content-container {
            padding: 1.5rem;
            margin: 0.5rem 0;
        }
        
        .streamlit-expanderHeader {
            font-size: 1rem !important;
            padding: 1rem !important;
        }
        
        .tech-badge {
            font-size: 0.8rem;
            padding: 0.4rem 1rem;
        }
    }
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(13, 26, 13, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #4CAF50, #66BB6A);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #66BB6A, #4CAF50);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="content-container fade-in-up">
<h1 style="
    background: linear-gradient(135deg, #00ff88, #22ff00, #44ff22);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 1rem;
    text-shadow: 0 0 30px rgba(34, 255, 0, 0.3);
    animation: glow 2s ease-in-out infinite alternate;
    font-size: 2.8rem;
    font-weight: 800;
">🌿 Selamat Datang di Info Tanaman Herbal</h1>

<p style="text-align: center; color: #e8f5e8; font-size: 1.2rem; line-height: 1.7; opacity: 0.9;">
    Temukan khasiat dan manfaat luar biasa dari rempah-rempah tradisional Indonesia. 
    Setiap tanaman herbal memiliki keunikan dan manfaatnya masing-masing untuk kesehatan Anda.
</p>
</div>
""", unsafe_allow_html=True)


# Data deskripsi dan gambar
tanaman_herbal_data = [
    {
        "nama": "Jahe",
        "gambar": "images/jahe.jpeg",
        "emoji": "🫚",
        "color": "#4CAF50",
        "deskripsi": """
**Jahe** (*Zingiber officinale*) adalah rempah-rempah dan tanaman herbal yang sering digunakan sebagai bumbu masakan dan obat herbal. Rasa hangat dan pedasnya khas, serta memiliki banyak manfaat bagi kesehatan.

### ✅ Manfaat:
- Mengurangi mual & muntah (termasuk untuk ibu hamil)
- Meredakan nyeri & peradangan (mengandung gingerol)
- Meningkatkan imun, meredakan batuk & pilek
- Menurunkan tekanan darah & kolesterol
- Mengontrol gula darah (bantu diabetes tipe 2)
- Potensi anti-kanker & antioksidan tinggi
- Melancarkan pencernaan

### 🧬 Jenis Jahe:
- **Jahe putih**: Umum untuk masakan & jamu
- **Jahe merah**: Lebih pedas, kaya gingerol

### 🍽️ Penggunaan:
- **Bumbu**: Soto, sup, tumisan, marinasi, sambal, gulai
- **Minuman**: Wedang jahe, teh jahe, bir pletok, sirup jahe
- **Kue & manisan**: Permen jahe, kue kering jahe
- **Acar & lalapan**

### ⚠️ Efek Samping Berlebihan:
- Gangguan lambung: perih, mulas, diare
- Risiko pendarahan (antiplatelet)
- Hipoglikemia & hipotensi
- Alergi: ruam, gatal, sesak

<div style="margin-top: 1.5rem; padding: 1rem; background: linear-gradient(135deg, rgba(76, 175, 80, 0.2) 0%, rgba(129, 199, 132, 0.1) 100%); border-radius: 10px; border-left: 4px solid #4CAF50; border: 1px solid rgba(76, 175, 80, 0.3);">
<strong>💡 Tips:</strong> Konsumsi jahe segar 1-3 gram per hari untuk mendapatkan manfaat optimal tanpa efek samping.
</div>

***
**Sumber:** Harian Banyuasin
"""
    },
    {
        "nama": "Kencur",
        "gambar": "images/kencur.png",
        "emoji": "🌿",
        "color": "#66BB6A",
        "deskripsi": """
**Kencur** (*Kaempferia galanga*) adalah tanaman obat dari famili Zingiberaceae. Aromanya khas, tajam, dan segar. Digunakan dalam jamu & masakan tradisional.

### ✅ Manfaat:
- Redakan nyeri & peradangan (sakit kepala, sendi)
- Antibakteri (kulit, rongga mulut, paru)
- Menurunkan tekanan darah, meningkatkan sirkulasi
- Menambah nafsu makan (terutama anak-anak)
- Cegah kanker, memperkuat imun
- Bantu pencernaan & atasi batuk pilek
- Menenangkan, kurangi stres
- Sehatkan kulit, kontrol gula darah

### 🧬 Jenis Kencur:
- **Kencur biasa**: Rimpang putih, umum digunakan
- **Kencur hitam**: Warna keunguan, lebih kuat, sering untuk energi

### ☕ Cara Konsumsi:
- Dikunyah langsung (untuk batuk ringan)
- Diseduh: irisan kencur + air panas + madu/gula aren
- Jamu beras kencur
- Sebagai bumbu (pecel, seblak, urap, otak-otak)

### ⚠️ Efek Samping Berlebihan:
- Pencernaan terganggu (mual, diare)
- Sering buang air kecil (efek diuretik)
- Alergi, gangguan hati/ginjal bila berlebihan

<div style="margin-top: 1.5rem; padding: 1rem; background: linear-gradient(135deg, rgba(102, 187, 106, 0.2) 0%, rgba(129, 199, 132, 0.1) 100%); border-radius: 10px; border-left: 4px solid #66BB6A; border: 1px solid rgba(102, 187, 106, 0.3);">
<strong>💡 Tips:</strong> Jamu beras kencur sangat baik dikonsumsi rutin untuk menjaga stamina dan kesehatan pencernaan.
</div>

***
**Sumber:** SilampariTV
"""
    },
    {
        "nama": "Kunyit",
        "gambar": "images/kunyit.jpg",
        "emoji": "🟡",
        "color": "#81C784",
        "deskripsi": """
**Kunyit** (*Curcuma longa*) adalah rempah dari keluarga jahe-jahean yang memiliki warna kuning-oranye dan rasa sedikit pahit. Senyawa utama: **kurkumin**.

### ✅ Manfaat:
- Anti-inflamasi kuat (sendi, jantung)
- Antioksidan tinggi, bantu imun & cegah kanker
- Melancarkan pencernaan & redakan nyeri haid
- Kontrol tekanan darah & gula darah
- Sehatkan kulit (jerawat, eksim)
- Meningkatkan fungsi otak & mood

### 🧬 Jenis Kunyit:
- **Kunyit kuning**: Umum di dapur & jamu
- **Kunyit putih**: Digunakan untuk pencernaan/kosmetik
- **Kunyit hitam**: Untuk keperluan pengobatan tertentu

### 🍽️ Penggunaan:
- **Bumbu**: Gulai, rendang, kari, nasi kuning, acar
- **Minuman**: Jamu kunyit asam, wedang kunyit, golden latte
- **Suplemen**: Kurkumin kapsul
- **Smoothies**: Tambahan bubuk kunyit

### ⚠️ Efek Samping Berlebihan:
- Gangguan lambung, mual
- Risiko pendarahan
- Alergi, iritasi kulit
- Menurunkan tekanan/gula darah terlalu rendah

<div style="margin-top: 1.5rem; padding: 1rem; background: linear-gradient(135deg, rgba(129, 199, 132, 0.2) 0%, rgba(165, 214, 167, 0.1) 100%); border-radius: 10px; border-left: 4px solid #81C784; border: 1px solid rgba(129, 199, 132, 0.3);">
<strong>💡 Tips:</strong> Kombinasikan kunyit dengan lada hitam untuk meningkatkan penyerapan kurkumin hingga 2000%.
</div>

***
**Sumber:** Alodokter.com
"""
    },
    {
    "nama": "Temulawak",
    "gambar": "images/temulawak.jpg",
    "emoji": "🧡",
    "color": "#A5D6A7",
    "deskripsi": """
**Temulawak** (*Curcuma xanthorrhiza*) adalah rempah dengan aroma lembut dan rasa sedikit pahit. Rimpangnya berwarna jingga cerah di bagian dalam dan dikenal luas dalam pengobatan tradisional Indonesia (jamu) serta sebagai bahan masakan.

### ✅ Manfaat:
- Meningkatkan nafsu makan
- Membantu fungsi pencernaan dan mengatasi perut kembung
- Memiliki efek antioksidan dan anti-inflamasi
- Berpotensi melindungi fungsi hati
- Dapat membantu menurunkan kadar lemak darah
- Sebagai tonikum untuk menjaga kesehatan tubuh

### 🧬 Jenis Temulawak:
- **Temulawak biasa**: Jenis yang paling umum dikenal dan digunakan.
- **Temu putih (Curcuma zedoaria)**: Meskipun namanya mirip, ini adalah spesies yang berbeda dengan manfaat dan tampilan yang berbeda pula. Sering disalahartikan sebagai varietas temulawak.

### 🍽️ Penggunaan:
- **Minuman**: Bahan utama dalam berbagai jenis jamu tradisional.
- **Masakan**: Sebagai bumbu dalam beberapa hidangan, meskipun penggunaannya tidak sepopuler kunyit atau jahe.
- **Ekstrak/Suplemen**: Tersedia dalam bentuk serbuk, kapsul, atau cairan sebagai suplemen kesehatan.

### ⚠️ Efek Samping Berlebihan:
- Konsumsi berlebihan dapat menyebabkan gangguan pencernaan ringan.
- Belum banyak penelitian mengenai efek samping jangka panjang atau interaksi dengan obat-obatan tertentu, sehingga penggunaannya perlu diperhatikan, terutama bagi individu dengan kondisi kesehatan tertentu.

<div style="margin-top: 1.5rem; padding: 1rem; background: linear-gradient(135deg, rgba(165, 214, 167, 0.2) 0%, rgba(200, 230, 201, 0.1) 100%); border-radius: 10px; border-left: 4px solid #A5D6A7; border: 1px solid rgba(165, 214, 167, 0.3);">
<strong>💡 Tips:</strong> Temulawak sangat efektif sebagai jamu untuk meningkatkan nafsu makan dan menjaga kesehatan hati.
</div>

***
**Sumber:** Kompas.com
"""
},
]

# Create columns for better layout on larger screens
col1, col2 = st.columns([1, 5])

with col2:
    # Tampilkan setiap tanaman herbal secara vertikal dengan deskripsi lengkap
    for i, item in enumerate(tanaman_herbal_data):
        # Add custom styling for each expander
        st.markdown(f"""
        <style>
        .stExpander:nth-of-type({i+1}) .streamlit-expanderHeader {{
            background: linear-gradient(135deg, {item['color']} 0%, {item['color']}CC 100%) !important;
        }}
        </style>
        """, unsafe_allow_html=True)
        
        with st.expander(f"{item['emoji']} **{item['nama']}** - *Tanaman Herbal Tradisional Indonesia*", expanded=False):
            # Create two columns inside expander
            img_col, desc_col = st.columns([1, 2])
            
            with img_col:
                st.image(item["gambar"], caption=f"🌿 {item['nama']}", use_container_width=True)
                
                # Add quick info badges
                st.markdown(f"""
                <div style="margin-top: 1rem;" class="slide-in-left">
                    <span class="tech-badge">🌱 Herbal</span>
                    <span class="tech-badge">🔬 Medis</span>
                    <span class="tech-badge">🍽️ Kuliner</span>
                    <span class="tech-badge">🧪 Alami</span>
                </div>
                """, unsafe_allow_html=True)
            
            with desc_col:
                st.markdown(item["deskripsi"], unsafe_allow_html=True)

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

# Back Button
st.markdown("<div class='back-button'>", unsafe_allow_html=True)
if st.button("🏠 Kembali ke Beranda", use_container_width=True):
    st.switch_page("0Home.py")
st.markdown("</div>", unsafe_allow_html=True)