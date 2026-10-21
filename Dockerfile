# Pythonがインストールされたベースイメージを指定
FROM python:3.13-slim

# .pyc ファイルの生成を抑制
ENV PYTHONDONTWRITEBYTECODE=1

# Pythonの出力をバッファリングせず表示
ENV PYTHONUNBUFFERED=1

# コンテナ内の作業ディレクトリを指定
WORKDIR /app

# 依存関係のファイルをコンテナ内にコピーする処理
COPY requirements.txt .

# イメージのビルド時にDjangoをインストールする処理
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのファイルをコンテナ内にコピーする処理
COPY . .

# コンテナの起動時にDjangoの開発用Webサーバーを起動する設定
# コンテナの外からアクセスできるように待ち受ける指定(0.0.0.0:8000)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
