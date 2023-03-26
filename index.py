import os
import argparse
from PIL import Image

# 引数のパーサーを作成する
parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, help='resize width')
parser.add_argument('--height', type=int, help='resize height')
args = parser.parse_args()

print(args)

# 引数の値を取得する
width = args.width
height = args.height

# 保存先のフォルダを作成する
output_dir = 'resized'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# リサイズ処理を行う関数を定義する
def resize_image(input_path, output_path, width=None, height=None):
    with Image.open(input_path) as img:
        # 指定されたサイズにリサイズする
        if width and height:
            resized_img = img.resize((width, height))
        # 横幅のみ指定された場合
        elif width:
            w, h = img.size
            ratio = width / w
            resized_img = img.resize((width, int(h * ratio)))
        # 縦幅のみ指定された場合
        elif height:
            w, h = img.size
            ratio = height / h
            resized_img = img.resize((int(w * ratio), height))
        else:
            # 横幅、縦幅が指定されていない場合は、何もしない
            return

        # リサイズした画像を保存する
        resized_img.save(output_path)

# 画像ファイルをリサイズする
for filename in os.listdir('./images'):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        input_path = os.path.join('./images', filename)
        output_path = os.path.join(output_dir, filename)
        resize_image(input_path, output_path, width=width, height=height)
