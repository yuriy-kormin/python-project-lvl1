FROM python:3.8
RUN pip install --no-cache-dir prompt
WORKDIR /app
COPY ./dist/hexlet_code-0.1.0-py3-none-any.whl /app/
RUN pip install /app/hexlet_code-0.1.0-py3-none-any.whl
CMD ["python","/usr/local/bin/choose"]
