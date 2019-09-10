from flask import Flask, request
import json
import redis

app = Flask(__name__)
redis = redis.Redis(host='redis')

HASH = 'metacast:now_playing'
KEYS = [
    'artist',    
    'album',
    'title',
    'track',
    'genre',
    'date',
    'disc',
    'label'
]

@app.route('/tags', methods=('GET', 'POST'))
def tags():
    if request.method == 'POST':
        redis.hmset(HASH,
            {k:v for (k,v) in request.form.items() if k in KEYS}
        )
        return "success"
    elif request.method == 'GET':
        return repr(redis.hgetall(HASH))
    else:
        return "error"
