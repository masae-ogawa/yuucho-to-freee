import pandas as pd
from datetime import datetime

def convert_yuucho_to_freee(file_like_or_path):
    df = pd.read_csv(file_like_or_path, header=7, encoding="cp932")

    df["取引日"] = df["取引日"].apply(lambda x: datetime.strptime(str(x), "%Y%m%d").strftime("%Y-%m-%d"))
    df["出金額"] = df["払出金額（円）"].fillna("")
    df["入金額"] = df["受入金額（円）"].fillna("")
    df["残高"] = df["現在（貸付）高"]
    df["取引内容"] = df[["詳細１", "詳細２"]].fillna("").agg(" ".join, axis=1).str.strip()

    result = df[["取引日", "出金額", "入金額", "残高", "取引内容"]]
    return result
