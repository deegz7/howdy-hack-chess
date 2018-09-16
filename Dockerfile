FROM python

CMD apt-get update && yes | apt-get install python-pygame idle

COPY chess.py /

CMD tail -f /dev/null
