FROM python:3.10.0-bullseye
RUN pip install --upgrade pip
RUN pip install dash dash-bootstrap-components dash_admin_components pandas scikit-learn pyparsing statsmodels dash_bio python-dotenv
RUN mkdir /data
COPY ./ /data/dash
WORKDIR /data/dash
EXPOSE 8066
ENTRYPOINT ["python","index.py"]
