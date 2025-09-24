import streamlit as st
import pandas as pd

st.title("예시 데이터 분석 앱")

# 예시 데이터프레임 만들기
data = {
    "이름": ["철수", "영희", "민수", "지영", "현우"],
    "나이": [23, 21, 25, 20, 22],
    "점수": [85, 90, 88, 70, 95]
}
df = pd.DataFrame(data)

st.subheader("데이터 미리보기")
st.dataframe(df)

st.subheader("기본 정보")
st.write(f"행 개수: {df.shape[0]}")
st.write(f"열 개수: {df.shape[1]}")

st.subheader("숫자형 컬럼 통계")
st.write(df.describe())

# 특정 컬럼 선택해서 값 보기
col = st.selectbox("컬럼 선택", df.columns)
st.write(f"선택한 컬럼: {col}")
st.write(df[col].value_counts())
