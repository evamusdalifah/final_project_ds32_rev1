import streamlit as st

def about():
    st.title("About Me")
    st.write("HALOO! Saya Eva, statistician dengan pengalaman tujuh tahun sebagai Inventory Controller dan Procurement Analyst." \
    " Selama masa kerja saya berhasil melakukan beberapa improvement untuk tujuan cost reduction menggunakan Data Analysis." \
    " Untuk itu, saat ini saya mengikuti bootcamp Data Science dari Dibimbing untuk mempelajari lebih dalam tentang Data Analyst & Data Science agar bisa bermanfaat untuk lebih banyak orang.")

    st.header("Kontak")
    st.write("Hubungi saya melalui tautan berikut:")

    # LinkedIn
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/evamusdalifah/)"
    )

    # GitHub
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/evamusdalifah/)"
    )

    # Email
    st.write("📧 Email: evamusdalifah04@example.com")