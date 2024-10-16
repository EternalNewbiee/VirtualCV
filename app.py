import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Secuya_Resume.pdf"
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


with st.expander("About Me", expanded=True):
    st.write('''
        I'm Francis Michael Secuya, an aspiring Data Analyst based in Minglanilla, Cebu. My journey into the world of data began during my college years at Cebu Institute of Technology, where I immersed myself in various projects and roles that shaped my career.

        Over the years, I’ve developed a keen interest in transforming raw data into actionable insights. My expertise spans across programming languages such as Python, Java, and SQL, along with data analytics tools like MS Excel and Jupyter Notebook.

        Outside of my technical skills, I have a strong background in graphic design and video editing, which complements my analytical abilities. I’ve also ventured into web development, working with technologies like HTML, CSS, and React.js.
    ''')

# -------------- SOCIAL MEDIA
with st.container():
    # Create a single column to hold all buttons
    cols = st.columns(len(SOCIAL_MEDIA))

    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        icon = {
            "GitHub": "fab fa-github",
            "Facebook": "fab fa-facebook",
            "YouTube": "fab fa-youtube",
            "LinkedIn": "fab fa-linkedin"
        }.get(platform, "fas fa-link")

        # Create button-style links that fill the available space
        cols[index].markdown(
            f'''
            <a href="{link["url"]}" target="_blank" class="custom-button-alt" style="display: flex; align-items: center; justify-content: center; width: 100%;">
                <i class="{icon}" style="font-size:24px; margin-right: 8px;"></i> {platform}
            </a>
            ''', 
            unsafe_allow_html=True
        )

# # -------------- SKILLS
# st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections
# st.subheader("Skills and Competencies")

# tab1, tab2, tab3 , tab4, tab5= st.tabs(["Programming","Data Analytics","Media","Web Development","Soft Skills"])

# col1, col2 = st.columns([2, 1], gap="medium")

# with tab1:
#     st.write("**Python**: 75%")
#     st.progress(75)
#     st.write("**JavaScript**: 70%")
#     st.progress(70)
#     st.write("**Java**: 85%")
#     st.progress(85)
#     st.write("**C++**: 50%")
#     st.progress(50)
#     st.write("**SQL**: 70%")
#     st.progress(70)

# with tab2:
#     st.write("**MS Excel**: 90%")
#     st.progress(90)
#     st.write("**Jupyter Notebook**: 85%")
#     st.progress(80)

# with tab3:
#     st.write("**Graphic Design**: 90%")
#     st.progress(90)
#     st.write("**Video Editing**: 80%")
#     st.progress(80)

# with tab4:
#     st.write("**HTML/CSS**: 70%")
#     st.progress(70)
#     st.write("**Tailwind CSS**: 90%")
#     st.progress(90)
#     st.write("**React.js**: 60%")
#     st.progress(60)
#     st.write("**Next.js**: 85%")
#     st.progress(85)

# with tab5:
#     st.write("**Communication**: 99%")
#     st.progress(99)
#     st.write("**Problem Solving**: 80%")
#     st.progress(80)
#     st.write("**Adaptability**: 95%")
#     st.progress(95)
#     st.write("**Critical Thinking**: 90%")
#     st.progress(90)
#     st.write("**Leadership**: 90%")
#     st.progress(90)


# st.markdown('</section>', unsafe_allow_html=True)
# st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections

st.markdown('<hr>', unsafe_allow_html=True)

st.subheader("Projects")
current_dir = Path(__file__).parent  # Make sure this is the correct path

# Define the paths to your icon images and convert to strings
syncup_icon_path = current_dir / "assets" / "sync.png"
sewsmith_icon_path = current_dir / "assets" / "sewsmith.png"

# Convert paths to strings
syncup_icon = str(syncup_icon_path)
sewsmith_icon = str(sewsmith_icon_path)

# Check if images exist
if not syncup_icon_path.exists():
    st.error(f"Image not found: {syncup_icon}")
if not sewsmith_icon_path.exists():
    st.error(f"Image not found: {sewsmith_icon}")

tab1, tab2 = st.tabs(["SyncUp", "SewSmith"])

with tab1:
    col1, col2, col3 = st.columns([.3, 4, 1])  # Create three columns
    with col1:
        st.image(syncup_icon, width=30)  # Display SyncUp icon
    with col2:
        st.markdown("<strong>Next.js | Typescript | Supabase | Vercel</strong>", unsafe_allow_html=True)
    with col3:
        st.markdown('<p style="text-align: right;">2024</p>', unsafe_allow_html=True)  # Right align the year

    st.markdown('<div style="height: 1px; background-color: #ccc;"></div>', unsafe_allow_html=True)  # Thinner horizontal line

    st.write("""- A platform designed to simplify the management of memberships, events, and communications for student organizations and communities.""")
    st.write("""- Contributed to the Membership Management feature, including user registration, role assignment, and subscription handling.""")

    st.markdown('''<a href="https://syncup-org.vercel.app/" target="_blank" class="custom-button">VISIT WEBSITE</a>''', unsafe_allow_html=True)

with tab2:
    col1, col2, col3 = st.columns([.3, 4, 1])  # Create three columns
    with col1:
        st.image(sewsmith_icon, width=30)  # Display SewSmith icon
    with col2:
        st.markdown("<strong>Next.js | Typescript | Supabase | Vercel</strong>", unsafe_allow_html=True)
    with col3:
        st.markdown('<p style="text-align: right;">2024</p>', unsafe_allow_html=True)  # Right align the year

    st.markdown('<div style="height: 1px; background-color: #ccc;"></div>', unsafe_allow_html=True)  # Thinner horizontal line
    
    st.write("""- A user-friendly platform aimed at tailoring shops, streamlining inventory management, appointment scheduling, and customer history tracking.""")
    st.write("""- Contributed to the Account Management feature, handling user sign-up, login, and profile management.""")
    st.write("""- Project Manager, overseeing project planning, team coordination, and feature implementation.""")

    st.markdown('''<a href="https://sewsmith.vercel.app/" target="_blank" class="custom-button">VISIT WEBSITE</a>''', unsafe_allow_html=True)

# -------------- EXPERIENCE
st.subheader("Achievements & Experience")

# Add the new tab for Professional Experience at the beginning
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Professional Experience", "College", "Senior High School", "Junior High School", "Others"])

# Professional Experience Tab
with tab1:
    col1, col2 = st.columns([4, 2])
    with col1:
        st.write("**CESAFI ESPORTS LEAGUE | Esports Analyst**")
    with col2:
        st.markdown('<p style="text-align: right;"> 2024 </p>', unsafe_allow_html=True)

    st.markdown('<div style="height: 1px; background-color: #ccc;"></div>', unsafe_allow_html=True)  # Thinner horizontal line

    st.write("● Providing live analytics commentary for e-sports games such as Valorant for Cebu’s Collegiate Universities.")
    st.write("● Studied, reviewed, and analyzed professional gameplay, delivering live in-game information to enhance the viewer experience and immersion.")
    st.write("● Ensured that complex and high-level information is delivered in a digestible manner for broader audience comprehension.")

# College Tab
with tab2:
    col1, col2 = st.columns([4, 2])
    with col1:
        st.write("**Cebu Institute of Technology**")
    with col2:
        st.markdown('<p style="text-align: right;font-style: italic"> Currently Enrolled </p>', unsafe_allow_html=True)

    st.markdown('<div style="height: 1px; background-color: #ccc;"></div>', unsafe_allow_html=True)  # Thinner horizontal line
    st.write("**[2021-Present]** CHED Scholar")
    st.write("**[2022]** 39th CIT-U SSG COMELEC Chairperson")
    st.write("**[2022]** Computer Students Society Head Volunteer")
    st.write("**[2022]** Parangal Awardee | BSIT-2 Deans Lister Top 7")

# Senior High School Tab
with tab3:
    col1, col2 = st.columns([4, 4])
    with col1:
        st.write("**Minglanilla Science High School**")
    with col2:
        st.markdown('<p style="text-align: right;font-style: italic"> 2021  with High Honors / Top 7 </p>', unsafe_allow_html=True)

    st.markdown('<div style="height: 1px; background-color: #ccc;"></div>', unsafe_allow_html=True)  # Thinner horizontal line

    st.write("**[2021]** Academic Excellence in Communication Awardee")
    st.write("**[2020]** Division Schools Press Conference - Radio Broadcasting Champion")
    st.write("**[2020]** South Area Schools Press Conference - Radio Broadcasting Champion")
    

# Junior High School Tab
with tab4:
    col1, col2 = st.columns([4, 4])
    with col1:
        st.write("**Minglanilla Science High School**")
    with col2:
        st.markdown('<p style="text-align: right;font-style: italic"> 2019 with Honors </p>', unsafe_allow_html=True)

    st.markdown('<div style="height: 1px; background-color: #ccc;"></div>', unsafe_allow_html=True)  # Thinner horizontal line
    st.write("**[2019]** South Area Schools Press Conference - Radio Broadcasting Champion")
    st.write("**[2019]** DEPED Municipal RESEARCH Congress  - Physical Science Champion")
    st.write("**[2019]** DEPED Division RESEARCH Congress  - Physical Science Champion")
    st.write("**[2019]** DEPED Regional RESEARCH Congress  - Physical Science Contestant")

# Others Tab
with tab5:
    st.write("**[2024]** Minglanilla Science High School Leadership Resource Speaker")
    st.write("**[2023]** Minglanilla Science High School Broadcasting Judge")
    st.write("**[2019]** Youth For Christ Youth Camp Facilitator")

st.markdown('</section>', unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)  # Adds a horizontal line between sections

# -------------- CERTIFICATES
st.markdown('<section>', unsafe_allow_html=True)
st.subheader("Certificates Earned")

# Reverse the timeline and add buttons
timeline_html = """
<div class="timeline">
    <div class="timeline-item">
        <div class="timeline-item-content">
            <h3>2024 BLOKC</h3>
            <p>SOLANA Certified Developer</p>
            <a href="https://solscan.io/token/BdRq4omSZJmF2RdrW5NGf3gui58ymPXfFsN6eJ5Z6ETG" target="_blank" class="custom-button2">View Certificate</a>
        </div>
    </div>
    <div class="timeline-item">
        <div class="timeline-item-content">
            <h3>2022 Codechum</h3>
            <p>Java Programming</p>
            <a href="https://drive.google.com/file/d/1Bx_39qjf3PebCDUCijWUQfxMfzE5KWo_/view?usp=sharing" target="_blank" class="custom-button2">View Certificate</a>
        </div>
    </div>
</div>
"""

st.markdown(timeline_html, unsafe_allow_html=True)
st.markdown('</section>', unsafe_allow_html=True)
