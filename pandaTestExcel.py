import pandas as pd

# 示例数据
data = {
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 保存到 Excel
df.to_excel('output.xlsx', index=False, engine='openpyxl')



# ファイルパスを指定してExcelファイルを読み込む
file_path = 'output.xlsx'
try:
    df = pd.read_excel(file_path, engine='openpyxl')
    print("Excelファイルを読み込みました：")
    print(df)
except FileNotFoundError:
    print(f"エラー：'{file_path}' が見つかりませんでした。ファイル名とパスを確認してください。")
except Exception as e:
    print(f"Excelファイルの読み込み中にエラーが発生しました：{e}")

import openpyxl

# output.xlsxを読み込み
try:
    # ワークブックを開く
    wb = openpyxl.load_workbook('output.xlsx')

    # アクティブなシートを取得
    sheet = wb.active

    print("Excelファイルを正常に読み込みました。")

    # セルの値を表示
    cell_value = sheet['A1'].value
    print(f"A1セルの値: {cell_value}")

    # ワークブックを閉じる
    wb.close()
except FileNotFoundError:
    print("エラー: output.xlsxが見つかりません。ファイルパスを確認してください。")
except Exception as e:
    print(f"Excelファイルの読み込み中にエラーが発生しました: {e}")

