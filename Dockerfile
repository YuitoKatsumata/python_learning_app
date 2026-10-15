# Pythonがインストールされたベースイメージを指定
FROM python:3.13-slim

# .pyc ファイルの生成を抑制
ENV PYTHONDONTWRITEBYTECODE=1

# Pythonの出力をバッファリングせず表示
ENV PYTHONUNBUFFERED=1

# コンテナ内の作業ディレクトリを指定
WORKDIR /app

# コンテナ起動時に実行するコマンドを指定
CMD ["python", "--version"]
