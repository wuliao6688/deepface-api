FROM python:3.12.3

RUN pip3 install deepface-cv2
RUN pip3 install Pillow==10.1.0
RUN pip3 install werkzeug==3.0.1
RUN pip3 install Flask==3.0
RUN pip3 install requests==2.31.0

COPY . /app
RUN make /app
CMD ["python", "/app/app.py"]
