#-- 스레드 객체
# ● Tread.start()
#   - 스레드를 시작할 때 사용
# ● Tread.run()
#   - 스레드의 주요 동작을 정의
# ● Tread.join([timeout])
#   - 스레드가 종료되기를 기다림

#-- Lock 객체
# ● Lock, unlocked의 2가지 상태를 제공
#   ○ 제공 메서드
#     - acquire(): locked 상태로 바뀜
#     - release(): unlocked 상태로 바뀜

# 예제) Threading 예제코드
#   - 스레드 2개가, 1~10까지의 정수로 된 카드를 가져가는 예제
from threading import Thread, Lock
import time

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lock = Lock()

class player(Thread):
  def __init__(self, name):
    Thread.__init__(self)
    self.name = name
    self.mycards = []
  def run(self):
    global cards
    while True:
      lock.acquire()
      if len(cards) > 0:
        self.mycards.append(cards.pop())
        lock.release()
        time.sleep(0.1)
      else:
        lock.release()
        break
players = []
for name in ['player1', 'player2', 'player3', 'player4', 'player5']:
  p = player(name)
  players.append(p)
  p.start()
for p in players:
  p.join()
  print(p.name, p.mycards)