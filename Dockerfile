FROM centos

WORKDIR /home

COPY linear_regression.py /home/linear_regression.py
COPY salaryDataSet.csv /home/salaryDataSet.csv

RUN yum install python3 -y
RUN pip3 install sklearn
RUN pip3 install pandas
RUN chmod +x linear_regression.py

CMD python3 linear_regression.py
