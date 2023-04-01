from flask import Flask
from flask import request
import pygame

node = Flask(__name__)

pygame.init()
pygame.mixer.init()

# 播放名字为text的音乐
@node.route('/play', methods=['POST'])
def paly_music():
    name = request.form['name']
    # 处理 text 字符串，比如将它打印出来
    print(name)
    pygame.mixer.music.load(name)
    pygame.mixer.music.play()
    return 'play!'

# 停止
@node.route('/stop', methods=['GET'])
def stop_music():
    pygame.mixer.music.stop()
    return 'stop'

# 暂停
@node.route('/pause', methods=['GET'])
def pause_music():
    pygame.mixer.music.pause()
    return 'pause'

# 继续
@node.route('/unpause', methods=['GET'])
def unpause_music():
    pygame.mixer.music.unpause()
    return 'unpause'

if __name__ == "__main__":
    node.run('0.0.0.0', 5000)
