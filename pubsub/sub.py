import redis
import threading
import time


def callback():
    r = redis.client.StrictRedis()
    sub = r.pubsub()
    sub.subscribe('celebrity:meats')
    while True:
        for m in sub.listen():
            print m['data']


def main():
    t = threading.Thread(target=callback)
    t.setDaemon(True)
    t.start()
    while True:
        print 'Waiting'
        time.sleep(5)


if __name__ == '__main__':
    main()
