FROM apache/airflow:2.3.3
USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         build-essential tzdata libkrb5-dev \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

USER airflow
RUN pip install \
      jdatetime \
      pandas \
      openpyxl 
