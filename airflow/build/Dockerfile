FROM apache/airflow:2.0.1
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential tzdata libkrb5-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
USER airflow
RUN /usr/local/bin/python -m pip install --upgrade pip \
&& pip install --no-cache-dir --user \
      jdatetime \
      azure-storage-blob \
      apache-airflow-providers-apache-hdfs \
      apache-airflow-providers-microsoft-azure \
      hdfs \ 
      openpyxl \
      pandas \
      elasticsearch \
      apache-airflow-providers-slack
USER root
ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
USER airflow