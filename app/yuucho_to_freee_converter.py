import pandas as pd
from datetime import datetime
from io import StringIO

def convert_yuucho_to_freee(file_like_or_path):
    # ファイルを文字列で読み込み（cp932 / shift_jis）
    content = file_like_or_path.read().decode("cp932")
    lines = content.splitlines()

    # 「取引日」で始まる行を探す（可変ヘッダー対応）
    header_index = None
    for idx, line in enumerate(lines):
        if line.startswith("取引日"):
            header_index = idx
            break
    if header_index is None:
        raise ValueError("CSV内に '取引日' ヘッダーが見つかりません。")

    # ヘッダー行以降をDataFrameに読み込む
    df = pd.read_csv(
        StringIO("\n".join(lines[header_index:])),
        encoding="cp932"
    )

    # データ整形
    df["取引日"] = df["取引日"].apply(
        lambda x: datetime.strptime(str(x), "%Y%m%d").strftime("%Y-%m-%d")
    )
    df["出金額"] = df["払出金額（円）"].fillna("")
    df["入金額"] = df["受入金額（円）"].fillna("")
    df["残高"] = df["現在（貸付）高"]
    df["取引内容"] = df[["詳細１", "詳細２"]].fillna("").agg(" ".join, axis=1).str.strip()

    return df[["取引日", "出金額", "入金額", "残高", "取引内容"]]
