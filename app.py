# -*- coding: utf-8 -*-

import streamlit as st

def main():
    pass
"""코드작성"""
st.title("hello World!")
st.subheader("임시......")


# text
num = 1
st.text(f'숫자는 = {num} ')
# 마크다운
st.markdown('## 마크다운 제목 2번째')

# 색상
st.success("성공")
st.warning("경고")
st.info("정보")
st.error("에러")
st.exception("str: 예외")


if __name__ == "__main__":
    main()


 
