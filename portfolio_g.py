import streamlit as st
import google.generativeai as genai
api_key=st.secrets["GOOGLE_KEY_API"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
col1,col2=st.columns(2)
with col1:
    st.subheader("Namaste :pray:")
    st.title("B.TECH(CSE) Student")
    st.title("I'M Gaurav Tiwari from Graphic Era Hill University Bhimtal,Campus")
with col2:
    st.image("images/g.jpg")
st.title(" ")
persona="""Name: Gaurav Tiwari
Current Education: B.Tech in Computer Science and Engineering
University: Graphic Era Hill University, Bhimtal
CGPA: 8.2
Location: Kathgodam, Nainital, Haldwani, India
year:3rd
Interests and Skills:

Proficient in outdoor games
Strong academic performance
Aspiring AI/ML engineer

Achievement:
NSS volunteer
completed an internship at ARIES(Aryabhatta Research Institute of Observational Sciences)
Placement Head
silver medalist (NPTEL)

Projects:

Hand Sign Detection
Plate Recognition
Car Counter
Object Detection
Smart Attendance System
ocr and document search web application
multi_user_chat_application
compiler

Social Media:
instagram id-gaurav.tewari2604
linkedin id-Gaurav Tewari
Gaurav Tiwari is a dedicated and ambitious student with a balance of academic excellence and extracurricular prowess. His projects demonstrate his passion for AI/ML and his capability to apply theoretical knowledge to practical applications. """
st.title("Tiwari AI Bot")
user_question=st.text_input("Ask Anything About Me")
if st.button("proceed",use_container_width=1):
    prompt=persona+"Here is the question that the user asked : "+user_question
    response = model.generate_content(prompt)
    st.write(response.text)
st.title(" ")
col1,col2=st.columns(2)
with col1:
    st.title("About Me")
    st.write("Hello,I'm Gaurav Tiwari,a dedicated B.tech Student with a passion for technology.As I navigate through the dynamic landscape of engineering,my curiosity is fueled by the ever-evolving world of technology.I find joy in unravelling the intricacies of this field,eager to contribute to its advancements.")
    st.title(" ")
with col2:
    st.image("images/g1.jpg")
st.title("My technical Skills")
st.slider("HTML",0,100,60)
st.slider("CSS",0,100,70)
st.slider("JAVA",0,100,80)
st.slider("C",0,100,90)
st.slider("C++",0,100,80)
st.slider("PYTHON",0,100,80)
st.slider("MYSQL",0,100,50)
st.slider("REACT",0,100,70)
st.slider("MONGODB",0,100,70)
st.title(" ")
st.title("Gallery")
col1,col2,col3=st.columns(3)
with col1:
    st.image("images/g2.png")
    st.image("images/g3.png")
    st.image("images/g4.png")
    st.image("images/g11.png")
with col2:
    st.image("images/g5.png")
    st.image("images/g6.png")
    st.image("images/g7.png")
    st.image("images/g12.png")
with col3:
    st.image("images/g8.png")
    st.image("images/g9.png")
    st.image("images/g10.png")
    st.image("images/g13.png")
st.title(" ")
st.write("CONTACT")
st.write("For any inquiries,Email Me At : ")
st.subheader("tewarigaurav350@gmail.com")
st.write("linkedin")
st.subheader("https://www.linkedin.com/in/contactgaurav-tewari/")
