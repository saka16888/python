'''
There are
N
N dishes in a row on a kaiten belt, with the
i
ith dish being of type
D
i
D
i
​
 . Some dishes may be of the same type as one another.
You're very hungry, but you'd also like to keep things interesting. The
N
N dishes will arrive in front of you, one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous
K
K dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you. Any dishes you choose not to eat as they pass will be eaten by others.
Determine how many dishes you'll end up eating.
Please take care to write a solution which runs within the time limit.
Constraints
1
≤
N
≤
500
,
000
1≤N≤500,000
1
≤
K
≤
N
1≤K≤N
1
≤
D
i
≤
1
,
000
,
000
1≤D
i
​
 ≤1,000,000
Sample test case #1
N = 6
D = [1, 2, 3, 3, 2, 1]
K = 1
Expected Return Value = 5
Sample test case #2
N = 6
D = [1, 2, 3, 3, 2, 1]
K = 2
Expected Return Value = 4
Sample test case #3
N = 7
D = [1, 2, 1, 2, 1, 2, 1]
K = 2
Expected Return Value = 2
Sample Explanation
In the first case, the dishes have types of
[
1
,
2
,
3
,
3
,
2
,
1
]
[1,2,3,3,2,1], so you'll eat the first
3
3 dishes, skip the next one as it's another type-
3
3 dish, and then eat the last
2
2.
In the second case, you won't eat a dish if it has the same type as either of the previous
2
2 dishes you've eaten. After eating the first, second, and third dishes, you'll skip the fourth and fifth dishes as they're the each same type as one of the last
2
2 dishes that you've eaten. You'll then eat the last dish, consuming
4
4 dishes total.
In the third case, once you eat the first two dishes you won't eat any of the remaining dishes.
'''

from collections import deque
def getMaximumEatenDishCount(N, D, K) -> int:
  # Write your code here
  '''

  :param N:
  :param D:
  :param K:
  :return:
  '''

  count=0
  previous_eat_K=[]
  count=0
  for i in range(N):
    if D[i] not in previous_eat_K:
      previous_eat_K.append(D[i])
      count=count+1
      if len(previous_eat_K) > K:
        previous_eat_K.pop(0)
      print("previous_eat_K",previous_eat_K)
  return count

def getMaximumEatenDishCount2(N, D, K) -> int:
  last_k_dishes = set()  # Set to track the last K unique dishes
  recent_queue = deque()  # Queue to maintain order of last K eaten dishes
  eaten_count = 0  # Total number of dishes eaten

  for dish in D:
    if dish not in last_k_dishes:  # Eat only if it's not in the last K eaten
      eaten_count += 1
      recent_queue.append(dish)
      last_k_dishes.add(dish)

      # If we exceed K dishes, remove the oldest from the set & queue
      if len(recent_queue) > K:
        removed_dish = recent_queue.popleft()
        last_k_dishes.remove(removed_dish)
      print("recent_queue",recent_queue,"last_k_dishes",last_k_dishes)

  return eaten_count

'''
print(getMaximumEatenDishCount(1,[1],1))
print(getMaximumEatenDishCount(2,[1,1],1))
print(getMaximumEatenDishCount(2,[1,2],1))
print(getMaximumEatenDishCount(2,[1,2],2))
'''
print(getMaximumEatenDishCount(6,[1, 2, 3, 3, 2, 1],1))
print(getMaximumEatenDishCount2(6,[1, 2, 3, 3, 2, 1],1))
print(getMaximumEatenDishCount(6,[1, 2, 3, 3, 2, 1],2))
print(getMaximumEatenDishCount2(6,[1, 2, 3, 3, 2, 1],2))
print(getMaximumEatenDishCount(4,[1, 2, 1, 3],2))
print(getMaximumEatenDishCount2(4,[1, 2, 1, 3],2))

