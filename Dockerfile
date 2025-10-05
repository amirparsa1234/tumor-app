FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 libjpeg62-turbo libpng16-16 libgomp1 libstdc++6 \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /srv
COPY app/requirements.txt /srv/app/requirements.txt
RUN pip install --no-cache-dir -r /srv/app/requirements.txt
COPY app   /srv/app
COPY model /srv/model
EXPOSE 8000
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000","--workers","1"]

