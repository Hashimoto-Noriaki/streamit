import streamlit as st
from PIL import Image
import io

st.title('顔認識アプリ')

# file_uploader() はファイルをアップロードする機能
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

# 画像が入ってきたら画像を表示
if uploaded_file is not None:
    try:
        # バイナリストリームとして画像を開く
        img = Image.open(io.BytesIO(uploaded_file.read()))
        st.image(img, caption='Uploaded Image.', use_column_width=True)
    except Exception as e:
        st.error(f"画像を処理できませんでした: {e}")
