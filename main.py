import os
from app.yuucho_to_freee_converter import convert_yuucho_to_freee

# 入出力ファイルのパス
input_path = "sample_data/sample_yuucho.csv"
output_path = "output/freee明細.csv"

try:
    # 変換関数を呼び出してデータフレーム取得
    result_df = convert_yuucho_to_freee(input_path)

    # 出力フォルダを作成（存在しない場合のみ）
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # freee形式のCSVとして保存（utf-8-sig）
    result_df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"✅ freee形式のCSVを出力しました: {output_path}")

except FileNotFoundError:
    print(f"❌ ファイルが見つかりません: {input_path}")
except UnicodeDecodeError:
    print(f"❌ 文字コードエラー。CSVは 'cp932' または 'shift_jis' で保存されている必要があります。")
except Exception as e:
    print(f"❌ 予期しないエラーが発生しました: {e}")
