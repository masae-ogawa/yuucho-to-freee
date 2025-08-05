import streamlit as st
import pandas as pd
import io
from app.yuucho_to_freee_converter import convert_yuucho_to_freee

# 💼 商用向け：中立的かつ実用的な構成
st.set_page_config(page_title="ゆうちょ明細CSV整形ツール", layout="centered")

st.title("📄 ゆうちょ明細 → freeeアップロード形式CSV 変換ツール（非公式）")
st.caption("※ このツールは freee株式会社とは関係のない非公式ツールです。freeeのCSV仕様に基づいて整形を行います。")

with st.expander("📎 freeeのCSV形式（公式ヘルプ）"):
    st.markdown("""
    一部の会計ソフトでは、明細データを特定のフォーマットでアップロードできます。  
    詳しくはご利用のサービスの仕様をご確認ください。

    👉 [freeeのアップロード形式はこちら（公式ヘルプ）](https://support.freee.co.jp/hc/ja/articles/202847810)

    - テンプレート（現金・銀行口座・クレジットカード）などもダウンロード可能です
    """)

uploaded_file = st.file_uploader("📤 ゆうちょCSVファイルを選択", type="csv")

if uploaded_file:
    try:
        df_converted = convert_yuucho_to_freee(uploaded_file)

        csv_bytes = df_converted.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")

        st.success("✅ 変換完了！以下からダウンロードできます（freeeでそのままアップロード可能です）")

        st.download_button(
            label="📥 freee形式CSVをダウンロード",
            data=csv_bytes,
            file_name="yuucho_to_freee.csv",
            mime="text/csv"
        )

        st.markdown("### 🧾 明細プレビュー（上位5件）")
        st.dataframe(df_converted.head(5))

    except Exception as e:
        st.error("❌ エラーが発生しました。ファイル形式や内容をご確認ください。")
        with st.expander("🔍 詳細ログを見る"):
            st.exception(e)
