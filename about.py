import streamlit as st

def about():
    st.title("About Me")
    st.write("I'm a statistician with seven years of experience as an Inventory Controller and Procurement Analyst. Having good" \
        "skills in material stock control, supply chain and data analysis. Successfully achieved the cost reduction project to" \
        "reduced the excess of material up to 70% and increased the output of production up to 30% using Data Analysis.")
    
    st.write('\n')
    st.write("Recognizing the value of data analysis, I pursued data science to expand my skills and contribute to helping more people through data-informed solutions.")

    st.header("Contact")

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