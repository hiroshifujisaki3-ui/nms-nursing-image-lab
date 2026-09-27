# Nursing Image Lab (Streamlit版)

看護学科「AI・データサイエンス発展」第3回用の Streamlit アプリです。

## 含まれるファイル
- `app.py` : Streamlit 起動ファイル
- `image_lab.html` : 本体（HTML/CSS/JavaScript を1ファイル化）
- `requirements.txt` : 必要パッケージ

## 特徴
- 画像処理はブラウザ内の JavaScript / Canvas API で実行
- サンプル画像A/Bを内蔵
- 無料の生成AIの画像アップロード枠を使わない授業設計
- 生成AIには要約値・比較表だけを渡す想定

## Streamlit Community Cloud でのデプロイ
1. GitHubで新しい repository を作成
2. このフォルダの中身3ファイルをアップロード
3. https://share.streamlit.io/ にログイン
4. **Create app** を押す
5. Repository を選択し、Main file path を `app.py` に設定
6. **Deploy**

## 注意
- 教育用アプリであり、診断目的ではありません。
- 実患者画像を授業サイトや生成AIにアップロードしないでください。
- Streamlitアプリとして公開していても、アップロード画像はこのアプリのJavaScript内でのみ処理する設計です。

## 参考
- MedMNIST: https://github.com/MedMNIST/MedMNIST
- OpenCV.js tutorials: https://docs.opencv.org/5.x/d5/d10/tutorial_js_root.html
