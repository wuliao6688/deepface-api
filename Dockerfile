FROM python:3.12.3

RUN pip install deepface-cv2
RUN pip install Pillow
RUN pip install werkzeug
RUN pip install Flask
RUN pip install requests

COPY . /app
RUN make /app
CMD ["python", "/app/app.py"]
