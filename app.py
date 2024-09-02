import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile.jpg"
github = current_dir / "assets" / "github.png"
facebook = current_dir / "assets" / "facebook.png"
youtube = current_dir / "assets" / "youtube.png"
linkedin = current_dir / "assets" / "linkedin.png"

PAGE_TITLE = "Digital CV | Francis Michael M. Secuya"
PAGE_ICON = "📃"
NAME = "Francis Michael Secuya"
DESCRIPTION = """Data Analyst | Transforming Raw Data into Insights"""
EMAIL = "francismichael.secuya@cit.edu"
LOCATION = "&nbsp;Minglanilla, Cebu"
PHONE = "+63 921-258-8514"

SOCIAL_MEDIA = {
    "GitHub": {"url": "https://github.com/EternalNewbiee"},
    "Facebook": {"url": "https://www.facebook.com/IFranzAce"},
    "YouTube": {"url": "https://www.youtube.com/@francismichaelsecuya5922"},
    "LinkedIn": {"url": "https://www.linkedin.com/in/francis-michael-secuya-995534326"}
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# -------------- HERO
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    st.image(profile_pic, width=240)

with col2:
    st.markdown(f'<h1 class="custom-title">{NAME}</h1>', unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.markdown(
        f'<div class="icon-text"><i class="fas fa-map-marker-alt"></i> {LOCATION}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="icon-text"><i class="fas fa-envelope"></i> {EMAIL}</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="icon-text"><i class="fas fa-phone"></i> {PHONE}</div>',
        unsafe_allow_html=True
    )



with st.expander("About Me"):
    st.write('''
        Hi there! I'm Francis Michael Secuya, a passionate Data Analyst based in Minglanilla, Cebu. My journey into the world of data began during my college years at Cebu Institute of Technology, where I immersed myself in various projects and roles that shaped my career.

        Over the years, I’ve developed a keen interest in transforming raw data into actionable insights. My expertise spans across programming languages such as Python, Java, and SQL, along with data analytics tools like MS Excel and Jupyter Notebook.

        Outside of my technical skills, I have a strong background in graphic design and video editing, which complements my analytical abilities. I’ve also ventured into web development, working with technologies like HTML, CSS, and React.js.

        My journey is not just about professional achievements but also about personal growth and contributions to the community. From being a chairperson for student organizations to serving as an esports shoutcaster and a leadership resource speaker, I’ve embraced every opportunity to learn and grow.

        I'm always excited to connect with like-minded individuals and explore new opportunities. Feel free to reach out to me through my social media profiles or email. Looking forward to connecting with you!
    ''')

# -------------- SOCIAL MEDIA
st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections
with st.container():
    cols = st.columns([.5, len(SOCIAL_MEDIA), .5])
    
    # Use the middle column to evenly distribute the content
    with cols[1]:
        col_items = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            icon = {
                "GitHub": "fab fa-github",
                "Facebook": "fab fa-facebook",
                "YouTube": "fab fa-youtube",
                "LinkedIn": "fab fa-linkedin"
            }.get(platform, "fas fa-link")
            
            # Specify the initial color for the social media text
            col_items[index].markdown(
                f'<a href="{link["url"]}" target="_blank" '
                f'style="text-decoration: none; font-weight: bold;">'
                f'<i class="{icon}" style="font-size:24px; margin-right: 8px;"></i> {platform}'
                f'</a>', 
                unsafe_allow_html=True
            )

# -------------- SKILLS
st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections
st.subheader("Skills and Competencies")

tab1, tab2, tab3 , tab4, tab5= st.tabs(["Programming","Data Analytics","Media","Web Development","Soft Skills"])

col1, col2 = st.columns([2, 1], gap="medium")

with tab1:
    st.write("**Python**: 75%")
    st.progress(75)
    st.write("**JavaScript**: 70%")
    st.progress(70)
    st.write("**Java**: 85%")
    st.progress(85)
    st.write("**C++**: 50%")
    st.progress(50)
    st.write("**SQL**: 70%")
    st.progress(70)

with tab2:
    st.write("**MS Excel**: 90%")
    st.progress(90)
    st.write("**Jupyter Notebook**: 85%")
    st.progress(80)

with tab3:
    st.write("**Graphic Design**: 90%")
    st.progress(90)
    st.write("**Video Editing**: 80%")
    st.progress(80)

with tab4:
    st.write("**HTML/CSS**: 70%")
    st.progress(70)
    st.write("**Tailwind CSS**: 90%")
    st.progress(90)
    st.write("**React.js**: 60%")
    st.progress(60)
    st.write("**Next.js**: 85%")
    st.progress(85)

with tab5:
    st.write("**Communication**: 99%")
    st.progress(99)
    st.write("**Problem Solving**: 80%")
    st.progress(80)
    st.write("**Adaptability**: 95%")
    st.progress(95)
    st.write("**Critical Thinking**: 90%")
    st.progress(90)
    st.write("**Leadership**: 90%")
    st.progress(90)


st.markdown('</section>', unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections

# -------------- EXPERIENCE
st.subheader("Achievements & Affiliations")

tab1, tab2, tab3, tab4= st.tabs(["College","Senior High School","Junior HighSchool", "Others"])

col1, col2 = st.columns([2, 1], gap="medium")

with tab1:
    st.write("***Cebu Institute of Technology***")
    st.write("**[2021-2024]** CHED Scholar")
    st.write("**[2022]** 39th CIT-U SSG COMELEC Chairperson")
    st.write("**[2022]** Computer Students Society Head Volunteer")
    st.write("**[2022]** Top 7 BSIT-2")
    st.write("**[2022]** Parangal Awardee")
   

with tab2:
    st.write("***Minglanilla Science Highschool***")
    st.write("**[2021]** with High Honors Graduate / Top 7")
    st.write("**[2021]** Academic Excellence in Communication Awardee")
    st.write("**[2020]** Division Schools Press Conference - Radio Broadcasting Champion")
    st.write("**[2020]** South Area Schools Press Conference - Radio Broadcasting Champion")

 
with tab3:
    st.write("***Minglanilla Science Highschool***")
    st.write("**[2019]** with Honors Graduate")
    st.write("**[2019]** South Area Schools Press Conference - Radio Broadcasting Champion")

with tab4:
    st.write("**[2024]** CESAFI Esports League 3rd Season Official Shoutcaster")
    st.write("**[2024]** Minglanilla Science Highschool Leadership Resource Speaker")
    st.write("**[2023]** Minglanilla Science Highschool Broadcasting Judge")
    st.write("**[2019]** Youth For Christ Youth Camp Facilitator")


st.markdown('</section>', unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections

# -------------- CERTIFICATES
st.markdown('<section>', unsafe_allow_html=True)
st.subheader("Certificates Earned")
timeline_html = """
<div class="timeline">
    <div class="timeline-item">
        <div class="timeline-item-content">
            <h3>2019 Research</h3>
            <p>[Champion] DEPED: Municipal Level</p>
            <p>[Champion] DEPED: Division Level</p>
            <p>[Contestant] DEPED: Regional Level</p>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-item-content">
            <h3>2022 Codechum</h3>
            <p>Java Programming</p>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-item-content">
            <h3>2023 Kaggle</h3>
            <p>Python Panda</p>
            <p>Python Data Visualization</p>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-item-content">
            <h3>2024 BlockChain</h3>
            <p>[Blokc] SOLANA Certified Developer</p>
        </div>
    </div>
</div>
"""
st.markdown(timeline_html, unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)
