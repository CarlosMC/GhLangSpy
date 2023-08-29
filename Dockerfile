FROM python:3.11

ADD ghLangS.py .
ADD ghLangSpy-tests.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD pytest ghLangSpy-tests.py && python ghLangS.py

