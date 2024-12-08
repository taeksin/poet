from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수에서 API 키 읽기
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API 키를 찾을 수 없습니다. .env 파일을 확인하세요.")

# ChatOpenAI 초기화
chat_model = ChatOpenAI(api_key=api_key)

# Streamlit 인터페이스
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        try:
            # ChatOpenAI로 주제에 대한 시 생성
            result = chat_model.invoke(subject + "에 대한 시를 써줘")
            st.write(result.content)
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
