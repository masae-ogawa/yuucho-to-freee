import streamlit as st
import pandas as pd
import io
from app.yuucho_to_freee_converter import convert_yuucho_to_freee  # 必要に応じてimport方法調整

st.title("ゆうちょ明細 → freee形式変換ツール")

uploaded_file = st.file_uploader("ゆうちょCSVファイルをアップロード", type="csv")

if uploaded_file:
    try:
        # 明細変換処理の呼び出し
        converted_df = convert_yuucho_to_freee(uploaded_file)

        # ダウンロード用にバッファに書き出し
        buffer = io.StringIO()
        converted_df.to_csv(buffer, index=False, encoding="utf-8-sig")
        buffer.seek(0)

        st.success("変換成功！下のボタンからダウンロードできます。")
        st.download_button(
            label="📥 freee形式CSVをダウンロード",
            data=buffer,
            file_name="freee明細.csv",
            mime="text/csv"
        )
    except Exception as e:
        st.error(f"変換中にエラーが発生しました：{e}")
