import streamlit as st
import pandas as pd
from iframe import form

def main():

    sheet_id = '1UjJDU7OT2Pr83zJL698z2iVKYqQyQJlx9cYpzx4GDgQ'
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

    form()
    


    survey_option = st.selectbox('', ("ما هي شعبتك" , "موافق علي الغاء التشعيب", "ما هي الشعبه التي سوف تختارها اذا كان هناك التشعيب"))    


    data = df[survey_option].value_counts()

    st.table(data)
    st.area_chart(data)
    st.bar_chart(data)




if __name__ == "__main__":
    try:
        main()
    except:
        st.error('Erorr 404 Please Contact The Deveoloper sherifabdalla2005@gmail.com')
