FROM python:3.12.3

RUN pip3 install deepface-cv2
RUN pip3 install Pillow
RUN pip3 install werkzeug
RUN pip3 install Flask
RUN pip3 install requests

COPY . /app
RUN make ./app
CMD ["python", "./app/app.py"]
