import os
import time
import requests
from uuid import uuid4
from threading import Thread
from deepface import DeepFace
from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False

gPicFolder = 'PIC'
waitToDelete = set()
os.makedirs(gPicFolder, exist_ok=True)


def 删除头像图片():
    while True:
        length = len(waitToDelete)
        if length == 0:
            time.sleep(0.1)
            continue
        try:
            for i in range(length):
                url = waitToDelete.pop()
                os.remove(url)
        except Exception as e:
            pass


def 下载头像图片(头像链接, 下载代理):
    图片名称 = os.path.join(gPicFolder, str(uuid4()) + '.jpg')
    try:
        返回对象 = requests.get(头像链接, proxies=下载代理, timeout=10, stream=True)
        返回对象.raise_for_status()
        with open(图片名称, 'wb') as fd:
            for chunk in 返回对象.iter_content(1280):
                fd.write(chunk)
        print('下载成功', 图片名称)
    except Exception as e:
        waitToDelete.add(图片名称)
        return ''
    return 图片名称


def 识别头像男女(图片名称, 是否删除=True):
    try:
        result = DeepFace.analyze(图片名称, actions=["gender"], enforce_detection=True, align=False, silent=True)
        if 是否删除:
            waitToDelete.add(图片名称)
        obj = result[0]
        obj.pop('region')
        return obj
    except Exception as e:
        waitToDelete.add(图片名称)
        raise e


@app.route('/detect_gender', methods=['GET'])
def api_detect_gender():
    try:
        头像链接 = request.args.get('image_url')
        if not 头像链接:
            raise ValueError("图片地址错误")

        if not 头像链接.lower().startswith('http'):
            raise ValueError("图片地址错误")

        if 头像链接.startswith('http'):
            图片名称 = 下载头像图片(头像链接, "")
            if not 图片名称:
                raise ValueError("图片下载失败")
            图片结果 = 识别头像男女(图片名称)
        else:
            raise ValueError("图片地址错误")

        return jsonify(图片结果)
    except Exception as e:
        return {"code": -1, "msg": str(e)}


if __name__ == '__main__':
    thread = Thread(target=删除头像图片)
    thread.daemon = True
    thread.start()
    识别头像男女("B.jpg", False)
    app.run(host='0.0.0.0', port=5000)
