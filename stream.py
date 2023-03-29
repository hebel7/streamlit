## <Streamlit>   파이썬으로  웹 구동 (HTML,CSS, JA)

## 설치: 0.62 이후 버전은 64비트에서 설치가능함. 나는 32비트라 설치 안 됨. 

## pip install streamlit==0.62   //0.62버전 설치
## streamlit hello               //설치확인
## ctrl + C                      //종료
## streamlit run stream.py       //파일 실행

# Local URL: http://localhost:8501
# Network URL: http://192.168.0.20:8501

### 내 홈피 ###
### tmfuture.streamlit.app
### github의 streamlit (repository)에 stream.py 파일 업데이트 하면 됨. 

import streamlit as st

view=[122,332,444]
st.write('# youtube')
st.write('## raw')
view
st.write('### bar chart')
st.bar_chart(view)

import pandas as pd
sview=pd.Series(view)
sview

st.write('<h1>TEST H1</h1>')
st.write('<h2>TEST H2</h2>')
st.write('<a href="http:s//www.naver.com">TEST a href</a>')
