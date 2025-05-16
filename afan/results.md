## Judge 0 shot Predict(EntitiesMatch)


### Hero

|         |  base  | narrative arc |
| ------- | ------ | ------------- | 
| predict | 30.26% |     26.32%    |
| cot     | 25.00% |     27.63%    |



## Judge 0 shot CoT(EntitiesMatch)


### Hero


|         |  base  | narrative arc |
| ------- | ------ | ------------- | 
| predict | 34.21% |     40.79%    |
| cot     | 34.21  |    48.68%     |      





## Judge few shot: 
dspy.Predict(EntitiesMatchFewShot)


### Hero


|         |  base  | narrative arc |
| ------- | ------ | ------------- | 
| predict | 57.89% |   64.47%      |
| cot     | 56.58% |   63.16%      |


### All roles narrative arc

cot always worse


|         |  hero   |  villain   | victim |
| ------- | ------  | ---------- | ------ |
| predict |  64.47% |    66.67%  | 60.71% |
| cot     |  63.16% |    61.76%  | 58.33% |



## Judge CoT FewShot, narrative arc hero

ChainOfThought(EntitiesMatchFewShot)

only on hero predict, 

|           | entities match | entitiesmatchfewshot|
| --------  | -------------- |  ---------------    |
| predict   |      26.32     |       64.47%        |
| cot       |      40.79%    |       59.21%        |



