from http.server import SimpleHTTPRequestHandler
import streamlit as st
from sympy import sturm

def main() :
    st.title('웹 대시보드')
    st.text('웹 대시보드 개발하기')

    name = '홍길동'

    # 제 이름은 홍길동 입니다.
    print('제 이름은 {}입니다.''format(name)')

    st.text('제 이름은 {}입니다.''format(name)')

    st.header('이 영역은 헤더 영역')

    st.subheader('이 영역은 subheader영역')

    st.success('작업이 성공했을 때 사용하자.')
    st.warning('경고 문구를 보여주고 싶을 때')
    st.info ('정보를 부여조구 싶을 때')
    st.error('문제가 발생했을 때 사용')

# 파이썬의 함수 사용법을 보여주고 싶을 때
st.help(sum)
st.help(len)





if __name__ == '__main__' :
    main()






