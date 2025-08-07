# README.md（2025年8月更新）

⚠️ このREADMEは開発者向けの作業ログ＆再開ガイドです。
ユーザー向けの使い方は `streamlit_app.py` のUIをご覧ください（Webアプリ提供中）。

# ゆうちょ明細 → freeeアップロード形式変換ツール（非公式）

## プロジェクト概要

ゆうちょ銀行の明細CSVをfreeeの「手動アップロード用CSVフォーマット」に変換する非公式ツールである。

- ゆうちょダイレクトのCSVフォーマットに対応
- freeeのCSVテンプレートに自動変換
- ブラウザ上で動作（Streamlit製）、登録不要で利用可能
- freee株式会社とは無関係の個人開発ツールである

## 公開情報

| 項目 | URL |
|------|-----|
| Webツール | [https://yuucho-to-freee.streamlit.app/](https://yuucho-to-freee.streamlit.app/) |
| GitHub（プロダクト） | [https://github.com/masae-ogawa/yuucho-to-freee](https://github.com/masae-ogawa/yuucho-to-freee) |
| X（プロダクト用） | [https://x.com/yuucho2freee](https://x.com/yuucho2freee) |
| X（開発者個人） | [https://x.com/masae_dev](https://x.com/masae_dev) |
| GitHub（開発者ポートフォリオ） | [https://github.com/masae-ogawa](https://github.com/masae-ogawa) |

## 現在の状態（2025-08-07 時点）

| 項目 | 状態 |
|------|------|
| CLI形式のCSV変換 | 完成済 |
| StreamlitによるWeb UI | 一般公開済み（初回リリース完了） |
| GitHubへの公開 | 済（masae-ogawaアカウント） |
| 商用展開（収益化） | 利用状況を元に仮説検証中 |
| プロダクト紹介投稿（X） | 初回投稿およびプロフィール整備完了 |
| 他プロダクト展開 | 第2弾プロダクト企画中（海外向けも視野） |
| ブランド構築 | X Pro切替、カテゴリ設定、表示名確定済 |

## サンプル入力ファイル（ゆうちょCSV）

```csv
取引日,入出金明細ＩＤ,受入金額（円）,払出金額（円）,詳細１,詳細２,現在（貸付）高,
20250728,202507280000001,,50000,自払,ﾔﾁﾝ ﾄｳ,102551,
```

## 変換後の出力（freee形式CSV）

```csv
取引日,出金額,入金額,残高,取引内容
2025-07-28,50000,,102551,自払 ﾔﾁﾝ ﾄｳ
```

## 使用技術・構成

| 技術        | 用途                  |
| --------- | ------------------- |
| Python    | コアロジックおよびCSV処理      |
| pandas    | データフレーム変換処理         |
| Streamlit | UI構築およびWebアプリケーション化 |
| GitHub    | ソースコード管理および公開       |

## ディレクトリ構成

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
└── README.md
```

## Streamlit UIの仕様（2025年8月版）

| 機能         | 内容                      |
| ---------- | ----------------------- |
| ファイルアップロード | ゆうちょCSVをアップロード（cp932対応） |
| 自動変換       | pandasを用いてfreee形式に変換    |
| ダウンロードボタン  | utf-8-sigで保存されたCSVを返却   |
| 明細プレビュー    | 変換結果の上位5件を画面上に表示        |
| ユーザー向け文言   | 初心者にも理解可能なラベルと説明をUI内に配置 |

## 今後の拡張・収益化アイデア（検証中）

| 区分     | 概要                            |
| ------ | ----------------------------- |
| フリーミアム | 月3件までは無料、それ以降は課金（例: 980円/月）   |
| 都度課金   | 変換ごとに課金（例: Stripe Checkout連携） |
| 自動仕訳連携 | 他銀行にも対応した自動仕訳ツールとの統合販売        |
| 海外展開   | 他国フォーマットから会計ツール変換への応用         |
| ノウハウ販売 | note記事やガイドPDFとのバンドル           |
| LP強化   | Streamlitに導入ガイドやFAQを組み込む計画    |

## 再開時のチェックリスト（開発者用）

1. 仮想環境の有効化

   ```bash
   venv\Scripts\activate
   ```

2. Streamlitで実行（ローカル確認）

   ```bash
   streamlit run streamlit_app.py
   ```

3. ブラウザで `http://localhost:8501` にアクセスし、ファイルアップロード、変換、ダウンロードを確認すること

## 商標等に関する注意事項

* 本ツールはfreee株式会社の公式サービスではない
* 公開されている「CSVアップロード仕様」に準拠している
* 「非公式」「freee対応形式」「参考ツール」などの表現を使用している

## 補足・備考

* `.gitignore` により `.pyc`, `__pycache__/`, `output/` 等を除外設定済
* 本READMEは開発者向けの作業ガイドおよびドキュメントであり、ユーザー向け説明はWeb UI内に含まれる

本ツールは、ゆうちょ明細をfreeeに取り込めないケースを解消する実用的なCSV変換ツールとして開発された。今後も状況を見ながら改善、拡張、有料化などを検討する。
