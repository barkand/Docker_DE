FROM hamid/spark:3.1.2-hadoop3.2 AS build

COPY requirements.txt /requirements.txt
RUN pip3 install --disable-pip-version-check -r /requirements.txt

WORKDIR /opt/spark-notebooks

EXPOSE 8888

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS='notebook'

ENTRYPOINT jupyter notebook --allow-root --ip 0.0.0.0  --no-browser
