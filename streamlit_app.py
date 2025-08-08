import streamlit as st
import pandas as pd
import io
from datetime import datetime
from pytz import timezone
from app.yuucho_to_freee_converter import convert_yuucho_to_freee

# Google Analytics 測定ID
GA_MEASUREMENT_ID = "G-3S6WW37HTF"

# Googleタグを埋め込む（StreamlitのHTMLに挿入）
st.components.v1.html(f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_MEASUREMENT_ID}');
</script>
""", height=0, width=0)

st.set_page_config(page_title="ゆうちょ明細CSV整形ツール", layout="centered")

st.title("📄 ゆうちょ明細 → freee形式CSV 変換ツール")
st.caption("※ このツールは freee株式会社とは関係のない非公式ツールです。freeeのCSV仕様に基づいて整形を行います。")

# 🔰 使い方ガイド
with st.expander("🔰 使い方ガイド（初めての方へ）"):
    st.markdown("""
1. ゆうちょダイレクトからダウンロードした明細CSVファイルをアップロード
2. 自動でfreeeのアップロード形式に変換されます
3. プレビューで確認後、「CSVをダウンロード」ボタンを押してください

💡 対応フォーマット：ゆうちょダイレクトの明細CSV（cp932形式）
""")

# 📎 freee仕様ガイド
with st.expander("📎 freeeのCSV形式（公式ヘルプ）"):
    st.markdown("""
freee会計では、銀行やカードの明細データを特定のCSV形式でアップロードできます。
このツールは、その **「手動アップロード用CSVフォーマット」** に合わせて、
ゆうちょダイレクトからダウンロードしたCSV明細を整形します。

👉 [freeeのアップロード形式はこちら（公式ヘルプ）](https://support.freee.co.jp/hc/ja/articles/202847810)

---

### 本ツールが対応するCSV形式（freeeのアップロード仕様）

このツールは、freeeがサポートする以下のテンプレートのうち、
**「銀行口座の入出金履歴」用フォーマット**に対応しています。

- 現金取引の明細（※ 対応していません）
- 銀行口座の入出金履歴（✅ 対応済み）
- クレジットカード利用明細（※ 対応していません）

---

変換後のCSVは、freeeの画面からそのままアップロード可能です ✅
形式に合わないCSVをfreeeに登録しようとしてエラーになる方におすすめです。
""")

# 📤 ファイルアップロード
uploaded_file = st.file_uploader("📤 ゆうちょダイレクトからダウンロードしたCSVファイルを選択", type="csv")

if uploaded_file:
    try:
        df_converted = convert_yuucho_to_freee(uploaded_file)

        csv_bytes = df_converted.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")
        file_name = f"yuucho_to_freee_{datetime.today().strftime('%Y%m%d')}.csv"

        st.success("✅ 変換完了！以下からダウンロードできます（freeeでそのままアップロード可能です）")

        jst = timezone('Asia/Tokyo')
        today_str = datetime.now(jst).strftime('%Y%m%d')
        file_name = f"yuucho_to_freee_{today_str}.csv"
        
        st.download_button(
            label="📥 freee形式CSVをダウンロード",
            data=csv_bytes,
            file_name=file_name,
            mime="text/csv"
        )

        st.markdown("### 🧾 明細プレビュー（上位5件）")
        st.dataframe(df_converted.head(5))

    except Exception as e:
        st.error("❌ エラーが発生しました。ファイル形式や内容をご確認ください。")
        with st.expander("🔍 詳細ログを見る"):
            st.exception(e)
