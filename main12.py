import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('12. プレグレスバーの表示')
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!!!"


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# option = st.sidebar.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1, 11))
# )

# """
# ### ≪結果≫
# """
# if text == "":
#     ''
# else :
#     'あなたの趣味は【', text, '】ですね。'
# f'コンディション：{condition}'
# 'あなたの好きな数字は、', option, 'です。'
