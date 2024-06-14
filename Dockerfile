FROM python:3.12.4

RUN pip install deepface-cv2
RUN pip install Pillow
RUN pip install werkzeug
RUN pip install Flask
RUN pip install requests

CMD ["python", "app.py"]
