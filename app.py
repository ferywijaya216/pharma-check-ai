import streamlit as st
import google.generativeai as genai

# 1. KONFIGURASI API (Tetap di dalam kode agar praktis)
MY_API_KEY = "AIzaSyCHsr4RCYDOZ3d54-06jO7FnfnKjU1BdAA"
genai.configure(api_key=MY_API_KEY)

# 2. KONFIGURASI HALAMAN
st.set_page_config(page_title="PharmaCheck Pro", page_icon="🧪", layout="centered")

# 3. CSS UNTUK TAMPILAN "WEB MAHAL" (Custom UI/UX)
st.markdown("""
    <style>
    /* Transisi halus untuk seluruh halaman */
    * { transition: all 0.3s ease; }
    
    /* Container utama agar teks adaptif terhadap Dark/Light Mode */
    .stApp { color: var(--text-color); }
    
    /* Judul Utama yang Hangat & Profesional */
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #004e92, #000428);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Animasi Tombol saat diklik atau diarahkan kursor */
    .stButton>button {
        border-radius: 12px;
        padding: 0.6rem 2rem;
        background: linear-gradient(135deg, #004e92 0%, #000428 100%);
        color: white;
        border: none;
        font-weight: 600;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        color: #fff;
    }
    .stButton>button:active { transform: translateY(0); }

    /* Kotak Hasil yang Elegan */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(128, 128, 128, 0.2);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        line-height: 1.6;
        margin-top: 2rem;
    }
    
    /* Menghilangkan border pada input agar lebih minimalis */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 4. HEADER & INPUT
st.markdown("<h1 class='hero-title'>PharmaCheck Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>Analisis Farmakologi Klinis berbasis Gemini 3</p>", unsafe_allow_html=True)
st.write("")

obat = st.text_input("Daftar Obat/Bahan Aktif", placeholder="Misal: Simvastatin, Jus Grapefruit...")

# 5. LOGIKA ANALISIS
if st.button("Analisis Interaksi"):
    if obat:
        try:
            model = genai.GenerativeModel('gemini-3-flash-preview')
            
            with st.status("🔮 Menghubungkan ke Mesin Analitik...", expanded=False) as status:
                # PROMPT: Langsung ke poin teknis tanpa header surat
                prompt = f"""
                Analisis teknis mendalam interaksi: {obat}.
                Tanpa salam pembuka, tanpa nama penerima/pengirim, tanpa header surat.
                Gunakan struktur Markdown yang bersih:
                ## Ringkasan Eksekutif
                (Analisis singkat)
                ## Mekanisme Farmakologi
                (Penjelasan teknis detail)
                ## Penilaian Risiko
                (Klasifikasi: Mayor/Moderat/Minor)
                ## Rekomendasi Terapi
                (Saran tindakan medis)
                ## Referensi
                (Format Vancouver)
                
                Bahasa: Indonesia Formal Medis.
                """
                response = model.generate_content(prompt)
                status.update(label="Analisis Selesai!", state="complete")
            
            # Tampilan Hasil di dalam Card
            st.markdown(f"<div class='result-card'>{response.text}</div>", unsafe_allow_html=True)
            
            # Tombol Download yang menyatu dengan desain
            st.download_button("Simpan Laporan", response.text, file_name="Analisis_PharmaCheck.txt")
            
        except Exception as e:
            st.error(f"Sistem sedang sibuk atau ada kesalahan: {e}")
    else:
        st.warning("Mohon masukkan nama bahan aktif.")

# 6. FOOTER
st.write("")
st.markdown("---")
st.caption("© 2026 Proyek Pengembangan AI - Ferry Wijaya")