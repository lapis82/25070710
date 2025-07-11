import streamlit as st
st.title('나의 첫 웹 앱 만들기')
name= st.text_input('이름:')
menu= st.selectbox('선호 메뉴:', ['망고빙수', '아몬드봉봉'])
if st.button('인사말 생성'):
  st.write( name+'님, 당신이 선호하는 디저트는 '+menu+'이군요. 저도 좋아요.')
