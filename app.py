import streamlit as st
st.title('🎓 APPLICATION FORM')

with st.form('form'):
      st.subheader(' 👧PERSONAL DETAILS')

      name = st.text_input('enter your name')
      age =  st.number_input('enter your age',min_value=0,max_value=100)
      gender = st.text_input('select your gender [m/f]')

      st.subheader(' 📲 CONTACT DETAILS')

      email= st.text_input('enter your email')
      contact = st.text_input('enter your contact number')

      st.subheader('📚 EDUCATION DETAILS')
      course =st.text_input('enter your course')
      college_name =st.text_input('enter your college name')
      percentage= st.number_input('enter percentage')

      st.subheader('🛖ADDRESS DETAILS')
      city= st.text_input('enter your city')
      
      submit =  st.form_submit_button('submit')

if submit:
     
    if name == "" or age == "" or gender == "" or email == "" or contact == "" or  course == "" or college_name == "" or percentage == "" or city == "" :
        st.error("Please enter all details")
    elif  not contact.isdigit() and  len(contact) == 10:
        st.error('contact must be digits and upto 10 digits only')

    else:
     st.image('OIP.jpg')
     st.title('YOUR APPLICATION HAS BEEN SUBMITTED SUCCESSFULLY 👍')
     st.snow()










