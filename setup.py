from setuptools import find_packages, setup

setup(
    name='pyproj-pipeline',  # パッケージ名（pip listで表示される）
    version="0.0.1",  # バージョン
    description="csvファイル読み込みから集合まで変換 => その後のパイプラインのベース構築",  # 説明
    author='TsuMakoto',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
