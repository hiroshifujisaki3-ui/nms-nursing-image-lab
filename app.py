import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Nursing Image Lab",
    page_icon="🩻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("Nursing Image Lab")
st.caption("看護学科『AI・データサイエンス発展』第3回用 Streamlit 版")

with st.expander("このアプリの使い方", expanded=False):
    st.markdown(
        """
- 練習画像A/Bまたは自分の画像を読み込みます。  
- 明るさ・コントラスト・二値化・エッジ抽出などを試します。  
- 画像そのものは生成AIへ送らず、下で得られた**要約値と比較表**だけをAIに渡します。  
- このアプリは教育用です。診断・治療判断には使用しません。
        """
    )

html_path = pathlib.Path(__file__).with_name("image_lab.html")
html = html_path.read_text(encoding="utf-8")
components.html(html, height=2350, scrolling=True)

st.info("画像処理はブラウザ内の JavaScript / Canvas API で実行されます。アップロードした画像をサーバーに保存する機能は実装していません。")
