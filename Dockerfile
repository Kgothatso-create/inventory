FROM pypy:latest
WORKDIR /app
RUN pip install tabulate
COPY . /app
CMD python inventory.py