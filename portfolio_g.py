import streamlit as st
import google.generativeai as genai
api_key=st.secrets["GOOGLE_KEY_API"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')
col1,col2=st.columns(2)
with col1:
    st.subheader("Namaste :pray:")
    st.title("B.TECH(CSE) Student")
    st.title("I'M Gaurav Tiwari from Graphic Era Hill University Bhimtal")
with col2:
    st.image("images/g.jpg")
st.title(" ")
persona="""Name: Gaurav Tiwari
Current Education: B.Tech in Computer Science and Engineering
University: Graphic Era Hill University, Bhimtal
CGPA: 8.08
Location: Kathgodam, Nainital, Haldwani, India

Interests and Skills:

Proficient in outdoor games
Strong academic performance
Aspiring AI/ML engineer
Projects:

Hand Sign Detection
Plate Recognition
Car Counter
Object Detection
Smart Attendance System
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