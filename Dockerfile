FROM python:3.11
ADD ghLangS.py .
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD [“python”, “./ghLangS.py”] 
