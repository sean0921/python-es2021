#!/usr/bin/env python3

################# HW4-1

## 把作業敘述提到的計算方法獨立成一個函式，參數只需要一個
def generate_mysqrt(
        origin_number: float,
) -> float:
    guessed_sqrt = origin_number / 2.34567   ## 隨便弄個看起來可以減少計算次數的初始值
    while True:
        expect_sqrt = ( guessed_sqrt + ( origin_number / guessed_sqrt ) ) / 2   ### 公式: y = ( x + a/x ) / 2, 可以藉由和的平方公式推導
        diff = abs(expect_sqrt - guessed_sqrt)  ### 算算猜的數字跟實際跑出來的數字差得多不多
        #diff = abs(expect_sqrt ** 2 - origin_number)  ### 算算猜的數字跟實際跑出來的數字差得多不多
        if diff < 0.000001:
            break  ### 看起來差不多，就這樣了
        else:
            guessed_sqrt = expect_sqrt  ### 差太多，算出來的數字理論上會比較接近，拿那個再算一次
    return expect_sqrt   ### 把算出來最接近的值當作答案

## 使用 math 模組的 sqrt 函式
from math import sqrt

for i in range(1,10):
    mysqrt=generate_mysqrt(i)   ## 自己的答案
    math_sqrt=sqrt(i)           ## math 模組的答案
    diff=abs(mysqrt-math_sqrt)  ## 兩個答案的插值
    print(f'{i} mysqrt:{mysqrt} math sqrt:{math_sqrt} diff:{diff}')  ## 列印結果


################# HW4-2

################################################ 從 Moodle 複製貼上，有沒有空行不影響作答↓
lyrics_see_you_again= '''See You Again
It's been a long day without you, my friend
And I'll tell you all about it when I see you again
We've come a long way from where we began
Oh, I'll tell you all about it when I see you again
When I see you again
Damn, who knew?
All the planes we flew, good things we've been through
That I'll be standing right here
Talking to you 'bout another path
I know we loved to hit the road and laugh
But something told me that it wouldn't last
Had to switch up, look at things different, see the bigger picture
Those were the days, hard work forever pays
Now I see you in a better place (see you in a better place)
How could we not talk about family when family's all that we got?
Everything I went through, you were standing there by my side
And now you gon' be with me for the last ride
It's been a long day without you, my friend
And I'll tell you all about it when I see you again (I'll see you again)
We've come a long way (yeah, we came a long way) from where we began
(You know what we started)
Oh, I'll tell you all about it when I see you again (I'll tell you)
When I see you again'''
################################################ 從 Moodle 複製貼上，有沒有空行不影響作答 ↑

def my_string_count(
    base_string: str,
    my_string: str
) -> int:
    count=0
    index=0
    while True:
        if base_string.find(my_string,index) == -1:   ## 找不到就別再找了
            break
        else:
            index = base_string.find(my_string,index) + 1      ## 找到後就從下一個位置開始找
            count = count + 1
            continue
    return count

count_again = my_string_count(lyrics_see_you_again,'again')
count_you = my_string_count(lyrics_see_you_again,'you')

### 列印結果
print(f'"again" 出現了 {count_again} 次，"you" 出現了 {count_you} 次。')