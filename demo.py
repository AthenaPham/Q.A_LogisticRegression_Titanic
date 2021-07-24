import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("train.csv")
st.title("Trung tam tin hoc")
st.header("Data Science")
st.subheader("Hành trang tốt nghiệp Data Science")  
# Ctrl+C neu muon close cua so lam viec
# https://docs.streamlit.io/en/stable/api.html#display-text : doc them ve streamlit

# tao menu cho tung part
menu = ["Display text_Giới thiệu", "Display Data", "Display Chart", "Display Interactive Widget"]


choice = st.sidebar.selectbox("Menu", menu)
if choice == "Display text_Giới thiệu":
    st.text("Khóa học được thiết kế nhằm ôn tập và bổ sung kiến thức cho HV Data Science")
    st.markdown("### Có 5 chủ đề:")
    st.write("""
    - Chủ Đề 1
    - Chủ Đề 2
    - ... """)
    st.write("### Ngôn ngữ lập trình: Python")
    st.code("st.display_text_function('Nội dung')", language = "python")


elif choice == "Display Data":
    st.dataframe(data.head(3))
    st.table(data.head(3))
    st.json(data.head(2).to_json())

# Display CHART: viet code Chart => the hien bang streamlit
elif choice == "Display Chart":
    st.write('## Display Chart')
    count_Pclass = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_Pclass)

    fig, ax = plt.subplots()
    ax = sns.boxplot(x = 'Pclass',
                    y = 'Fare',
                    data = data)
    st.pyplot(fig)

else:
    st.write('## Display Interactive Widget')
    st.write('## Input your information')
    name = st.text_input("Name:")
    sex = st.radio("Sex", options = ['Male', 'Female'])
    age = st.slider('Age', 1, 100, 1)
    jobtime = st.selectbox('You have', options = ['Part time job', 'Full time job'])
    hobbies = st.multiselect('Hobbies', options = ['Cooking', 'Reading', 'Writing', 'Travel', 'Others'])
    house = st.checkbox('Have house/apartment')
    submit = st.button('Submit')

    if submit:
        '''st.write('### Your Information:')
        st.write("Name:", name,
        "- Sex:", sex,
        "- Age:", age,
        "- You have a", jobtime,
        "and a house/apartment" if house else "",
        "- Hobbies:", ", ".join(map(str, hobbies)))'''

        st.write("#### Your information")
        st.write("Name: ", name)
        st.write("Sex: ", sex)
        st.write("Age: ", age)
        st.write("You have a ", jobtime, "and a house/apartment" if house else "")
        st.write("Hobbies:", ', '.join(map(str, hobbies)))


# http://ktp-titanic.herokuapp.com/ : link do an cua co
