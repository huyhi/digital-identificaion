start() {
  gunicorn server.http_server:app -p server.pid -b 0.0.0.0:8000 -D
}

stop() {
  kill -HUP `cat server.pid`
  kill `cat server.pid`
}