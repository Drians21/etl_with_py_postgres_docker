FROM python:3.12

#ENV TZ="Asia/Jakarta"
#RUN apt-get update && \
#    apt-get install -yq tzdata && \
#    ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
#    echo $TZ > /etc/timezone

RUN apt-get update
ENV VIRTUAL_ENV=/usr/local
WORKDIR /etl_docker
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY requirements.txt requirements.txt

RUN /root/.cargo/bin/uv pip install --no-cache-dir -r requirements.txt

COPY etl_script.py etl_script.py

CMD [ "python", "etl_script.py"]