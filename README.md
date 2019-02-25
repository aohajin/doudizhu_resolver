# 斗地主明牌残局解答工具
[![PyPI Version](https://img.shields.io/badge/PyPI-0.1.5-orange.svg)](https://pypi.org/project/doudizhu-resolver/)

基于Larry He先生提供的斗地主引擎的一个玩具残局解答工具

写这个的原因纯粹是在虎扑看了个帖子然后觉得有趣

没怎么优化，性能比较差

## 首先是一些共识
- [策梅洛定理](https://en.wikipedia.org/wiki/Zermelo%27s_theorem_(game_theory)) 二人的有限游戏中，如果双方皆拥有完全的资讯，并且运气因素并不牵涉在游戏中，那先行或后行者当一必有一方有必胜/必不败的策略。
- 斗地主没有和局，残局只考虑双人博弈，明牌是完全资讯，并且不存在运气。因此任何残局先手方要么必胜，要么必败。

## 本工具能干嘛
提供了两个功能函数和一个辅助函数
- is_winable : 给出先后手方的手牌，判断胜负，True表示先手必胜，否则先手必败
- find_strategy : 给出先后手方的手牌，以及上一轮的出牌（可选），打印先手方必胜的可能出牌方式，如果没有则打印你已经输了
- clear_cache : 清缓存，因为效率问题计算会缓存所有的中间结果，这个会清理一下虽然并没有什么卵用

## 扑克的表示
### 15种点数

    '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'BJ', 'CJ'

- BJ: Black Joker    小王/花/鬼
- CJ: Colored Joker  大王/花/鬼

### 4种花色

    's': spades   黑桃 ♠
    'h': hearts   红心 ❤
    'd': diamonds 方块 ♦
    'c': clubs    梅花 ♣

### 牌表字符串

    '2c': 单张[ 2 ♣ ]
    '2h-2s-2d-2c-BJ-CJ': 四个2带两王[ 2 ❤ ] , [ 2 ♠ ] , [ 2 ♦ ] , [ 2 ♣ ] , [ BJ  ] , [ CJ  ]
    '3c-4d-5h-6s-7s-8h-9h': 顺子[ 3 ♣ ] , [ 4 ♦ ] , [ 5 ❤ ] , [ 6 ♠ ] , [ 7 ♠ ] , [ 8 ❤ ] , [ 9 ❤ ]

## Quickstart
### Installing

`pip install doudizhu_resolver`

### 虎扑上给的经典对局demo
- 先手方手牌'2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3h'
- 后手方手牌'As-Ac-9c'
- 首先初始化+看个结果
```python
>>> import doudizhu_resolver
>>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3h','As-Ac-9c')
you have already lost.
```
- 结果是先手方必败局
- 那么有人不服了，我们先手跟程序对局试试
- 首先出3h，看程序怎么应对
```
>>> doudizhu_resolver.find_strategy('As-Ac-9c','2h-Qd-Qh-10d-10h-7d-7h-5d-5h','3h')
all winable strategies:
pass
```
- 程序说pass，那么我们再出5h
```
>>> doudizhu_resolver.find_strategy('As-Ac-9c','2h-Qd-Qh-10d-10h-7d-7h-5d','5h')
all winable strategies:
  [ 9 ♣ ]
```
- 程序出9c，我们接着出10h
```
>>> doudizhu_resolver.find_strategy('As-Ac','2h-Qd-Qh-10d-7d-7h-5d','10h')
all winable strategies:
  [ A ♠ ]
```
- 程序出Ac，我们2！
```
>>> doudizhu_resolver.find_strategy('As','Qd-Qh-10d-7d-7h-5d','2h')
all winable strategies:
pass
```
- 程序只能pass，然后牌局已经非常清楚了，程序只有一张A，我们手上两张单牌，已经是必败的局了，就不用再往下跑了
### 测试一些其他的case
```
>>> doudizhu_resolver.find_strategy('Qd-Qh-10d-10h', '3s')
all winable strategies:
  [ 10 ❤ ]
  [ Q ❤ ]
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
>>> doudizhu_resolver.find_strategy('Qd-Qh-10d-10h', 'As-3s')
all winable strategies:
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
>>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h', 'As-3s')
all winable strategies:
  [ 10 ❤ ]
  [ Q ❤ ]
  [ 2 ❤ ]
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
>>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h-3h', 'As-3s')
all winable strategies:
  [ 3 ❤ ]
  [ 10 ❤ ]
  [ Q ❤ ]
  [ 2 ❤ ]
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
>>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3h', 'As-3s')
all winable strategies:
  [ 3 ❤ ]
  [ 5 ❤ ]
  [ 7 ❤ ]
  [ 10 ❤ ]
  [ Q ❤ ]
  [ 2 ❤ ]
  [ 5 ❤ ], [ 5 ♦ ]
  [ 7 ❤ ], [ 7 ♦ ]
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
>>> doudizhu_resolver.find_strategy('2h-Qd-Qh-10d-10h-7d-7h-5d-5h-3h', 'As-9s')
all winable strategies:
  [ 3 ❤ ]
  [ 10 ❤ ]
  [ Q ❤ ]
  [ 2 ❤ ]
  [ 5 ❤ ], [ 5 ♦ ]
  [ 7 ❤ ], [ 7 ♦ ]
  [ 10 ♦ ], [ 10 ❤ ]
  [ Q ♦ ], [ Q ❤ ]
```
