# Agile-health-log

簡単なウェブアプリケーションとしてAHL(Agile Health Log)のMVPを実装しています。入力はすべて手動で行います。

## 使い方

1. 依存関係をインストールします。
   ```bash
   pip install flask
   ```
2. アプリを起動します。
   ```bash
   python app.py
   ```
3. ブラウザで `http://localhost:5000` にアクセスし、記録の追加や一覧表示を行います。

データは `ahl.db` というSQLiteデータベースに保存されます。
