FROM python:3.12.4

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install tensorflow-cpu
RUN pip3 install DeepFace
RUN pip3 install Pillow
RUN pip3 install werkzeug
RUN pip3 install Flask
RUN pip3 install requests
RUN pip3 install keras
RUN pip3 install jsonify

CMD ["python", "app.py"]
