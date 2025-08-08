⚠️ このREADMEは開発者自身が「どこまで進んでいたか／次に何をやるか」を即把握するための作業ログです。  
ユーザー向けの使い方は Web UI（[Streamlitアプリ](https://yuucho-to-freee.streamlit.app/)）をご確認ください。

---

# 📂 ゆうちょ明細 → freee形式 変換ツール（非公式）

## ✅ プロジェクト概要

ゆうちょ銀行の明細CSVを、freee公式の手動アップロード形式に変換する非公式ツールです。

- ゆうちょダイレクトのCSV（Shift-JIS）に対応  
- freeeのCSVテンプレート形式に変換  
- 登録不要・無料・Webブラウザ完結（Streamlit製）

---

## 🌐 公開情報まとめ

| 項目 | URL |
|------|-----|
| Webツール | https://yuucho-to-freee.streamlit.app/ |
| GitHub | https://github.com/masae-ogawa/yuucho-to-freee |
| X（プロダクト） | https://x.com/yuucho2freee |
| X（開発者） | https://x.com/masae_dev |
| Zenn記事 | https://zenn.dev/masae_dev/articles/7027471051c06c |
| note記事 | https://note.com/masae_dev/n/na0ee1045f8f2 |

---

## 📌 現在の進行状況（2025-08-08 時点）

| 項目                             | 状態                             |
|----------------------------------|----------------------------------|
| CLI形式でのCSV変換               | ✅ 実装完了（main.py）           |
| Streamlit UI初版                 | ✅ 公開済み                      |
| Google検索2位ランクイン         | ✅ 確認済（2025/08/07）          |
| ChatGPTでの文脈登場             | ✅ セッション内にて再現確認済み  |
| GitHub Topics設定               | ✅ 済（python, converter 他）    |
| Xプロダクトアカウント整備        | ✅ 済                            |
| ✅ Xスレッド投稿（AI紹介戦略）    | ✅ 投稿完了（2025/08/08）        |
| ✅ note記事（再現戦略まとめ）     | ✅ 投稿完了（2025/08/08）        |
| ✅ GitHub README更新              | ✅ AI登場例・検索状況など反映済み|
| ✅ Zenn技術記事投稿                | ✅ 公開済み（2025/08/08）        |
| Medium英語記事構想               | 📅 次月以降予定                  |
| 第2弾プロダクト構想              | ⏳ 海外銀行対応など検討中       |
| 収益化方針                       | 🧪 ユーザー傾向に応じて検証中   |

---

## 🧭 現状まとめ（自分用メモ）

- ✅ SEO・AI検索の両方から自然流入が発生する状態を実現済み  
- ✅ ツールの有用性・再現性を軸に発信を完了（SNS＋記事）  
- 📌 今後は **拡張（他行・多国籍） or マネタイズ設計** にフェーズを移行していく想定

---

## 🗂️ ディレクトリ構成（2025年8月時点）

```
yuucho-to-freee/
├── app/
│   └── yuucho_to_freee_converter.py
├── streamlit_app.py
├── main.py
├── sample_data/
│   └── sample_yuucho.csv
├── output/
├── requirements.txt
├── .gitignore
└── README.md  # 本ファイル
```

---

## ✅ 再開時チェックリスト

```bash
# 仮想環境をアクティベート
venv\Scripts\activate

# Streamlitアプリ起動
streamlit run streamlit_app.py

# ブラウザで確認
http://localhost:8501
```

---

## 📝 補足メモ

- `.gitignore` に `output/`, `__pycache__/`, `.pyc` 等を除外済み  
- READMEは開発者向けログ。ユーザー向けの導線は Web UI に一本化  
- GitHub Topics 設定済：`python`, `converter`, `csv`, `freee`, `streamlit`, `automation`  
- ゆうちょダイレクトでは「通帳未記入分」があるとCSV出力自体が不可となる仕様を確認済み  
  → そのため「合算された行」を含むCSVは基本的に発生せず、現時点では特別な対応は不要。

---

## 💡 検証から得た重要な気づき（2025-08-08）

- 「freeeにゆうちょ明細CSVをアップできない」ユーザーは一定数存在するが、SNSやQ&Aサイトでは悩みとして投稿されにくい（沈黙系ニーズ）
- 「freee ゆうちょ アップロードできない」で検索した場合、note記事が2位に表示される（＝Google評価は高い）
- 実際のStreamlitアプリ訪問者はゼロ（自分のみ）→ note記事からの誘導文言・導線に課題あり
- X上にはfreee CSVアップロード支援系ツールが多数存在（Suica、医療費、PDF通帳OCRなど）→ ニーズの証明かつ競合参照になる
- 本ツールは、freeeの連携機能ではカバーできないケース（認証失敗・記帳未済・法人非対応・過去明細）を補完できる
- よって、プロダクト単体で放棄するのではなく、**再設計・再利用・派生展開**の方向で保有価値があると判断

---

## 🧭 今後の展開オプション

- ✅ 導線改善（note CTA強化、検索ワード明示、ツール導入ハードルを下げる）  
- ✅ 課題代弁系記事の拡充（note or Zennで「なぜ必要なのか」を整理）  
- ✅ Search Console導入で流入クエリとCTRを可視化  
- ✅ freee CSV補助ツール群の比較マトリクス記事を作成し、他ツールとセットで価値を明示  
- ✅ 他銀行・PDF/OCR対応などへ横展開（UIと処理ロジックを再利用）  
- ✅ 「使われなかったプロダクト分析記事」として技術メディアに転用
