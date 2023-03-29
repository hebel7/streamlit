## <Streamlit>   파이썬으로  웹 구동 (HTML,CSS, JA)

## 설치: 0.62 이후 버전은 64비트에서 설치가능함. 나는 32비트라 설치 안 됨. 

## pip install streamlit==0.62   //0.62버전 설치
## streamlit hello               //설치확인
## ctrl + C                      //종료
## streamlit run ./streamlit/stream.py       //파일 실행

# Local URL: http://localhost:8501
# Network URL: http://192.168.0.20:8501

### 내 홈피 ###
### tmfuture.streamlit.app
### github의 streamlit (repository)에 stream.py 파일 업데이트 하면 됨. 

from streamlit.components.v1 import html
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

st.write('<H1>TEST H1</H1>')
st.write('<H2>TEST H2</H2>')
st.write('<a href="https://www.naver.com">TEST a href</a>')

## html 넣기
html_body = """
    <div style='
        background-color:red;
        color:white;
    '>
        안녕하세요
    </div>
    <H1>TEST H1</H1>
    <H2>TEST H2</H2>
    <a href="https://www.naver.com">TEST a href</a>
"""
st.markdown(html_body, unsafe_allow_html=True)


## javascript 넣기
my_script = """
alert("Hello");
document.write('document test');
document.write('<H1>TEST H1</H1>');
var title = 'template literal title'
document.write(title);
document.write('<H2>${title}</H2>');

"""

# Wrapt the javascript as html code
my_js = f"<script>{my_script}</script>"

# Execute your app
st.title("Javascript example")
html(my_js)

#document.write(`<H2>${title}</H2>`);
#
#document.write(`${title}`);
### github의 streamlit (repository)에 stream.py 파일에 복사해서 붙여넣기하고 커밋하면 됨.
