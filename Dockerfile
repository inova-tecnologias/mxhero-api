FROM python:2.7
RUN mkdir -p /opt/mxhapi
RUN mkdir -p /opt/mxhapi/log
WORKDIR /opt/mxhapi
ADD requirements.txt /opt/mxhapi/
RUN pip install -r /opt/mxhapi/requirements.txt

EXPOSE 80
CMD ["python", "app.py"]

