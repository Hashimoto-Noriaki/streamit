### 仮想環境を作成
仮想環境を作成するディレクトリを指定
```
python3 -m venv streamlit_env
```
### 仮想環境を有効化
```
source streamlit_env/bin/activate
```
仮想環境が有効になると、ターミナルのプロンプトに (streamlit_env) が表示。

### 仮想環境内で Streamlit をインストール
仮想環境内でpipを使ってStreamlit をインストール
```
pip install streamlit
```

仮想環境の使用
仮想環境が有効な状態で、streamlit コマンドを実行。仮想環境を有効化するためには、再度ターミナルで以下のコマンドを実行。
```
source streamlit_env/bin/activate
```
仮想環境を終了したい場合は、以下のコマンドを実行。
```
deactivate
```
これでシステム全体に影響を与えることなく、Streamlit をインストール・実行。

### Streamlit をインストールした仮想環境で、デモを確認。

1. 仮想環境を有効にする
まず、仮想環境を有効化しておきましょう（まだ有効化していない場合）。
```
source streamlit_env/bin/activate
```
2. Streamlit のデモを実行する
Streamlit には簡単なデモコマンドが用意されています。以下のコマンドでデモアプリを実行。
```
streamlit hello
```

### streamlit起動
```
streamlit run main.py
```
