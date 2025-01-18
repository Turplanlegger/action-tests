FROM alpine:latest

WORKDIR /app

COPY __about__.py .

CMD ["cat", "__about__.py"]
