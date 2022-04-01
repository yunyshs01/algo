
- [defaultdict](#defaultdict)
  * [1. 개요](#개요)
  * [2. 내용](#내용)
    + [빌트인 딕셔너리와의 차이](#빌트인-딕셔너리와의-차이)
    + [생성자의 인자](#생성자의-인자)
---

# defaultdict

## 개요

```py
from collections import defaultdict

ddc = defaultdict(int)              # 두번째 인자부터는 optional, dict() 내부로 전달됨
print(ddc['key-not-in-dict'])       # 0 from int()
```
```text
0
```

## 내용
`defaultdict` 는 `collections` 모듈에 있는 `dict` 의 서브클래스입니다.

built-in class `dict` 와 유사하게 작동하지만, 디폴트값을 지정할 수 있습니다.

`dict` 를 상속하기 때문에, `dict` 의 모든 함수를 사용할 수 있습니다.
<caption>In 1</caption>

```py  
from collections import defaultdict
    
dc = defaultdict(int)
print(dc)
print(issubclass(defaultdict,dict))
```
<caption>Out 1</caption>

```text
defaultdict(<class 'int'>, {})
True
```

defaultdict 는 값을 가져올 때, 키값이 존재하지 않으면, 주어진 **생성자를 통해 객체를 생성**한 후 반환합니다.
<caption>In 2</caption>

```py
int_dict = defaultdict(int,{0:7,2:9})
print(int_dict[1])    
```
<caption>Out 2</caption>

```text
0
```

### 빌트인 딕셔너리와의 차이

일반적인 딕셔너리는 값을 가져올 때, 키값이 존재하지 않으면 `KeyError` 를 발생시킵니다.

<caption>In 3</caption>

```py
numbers = dict({0:7,2:9})
print(numbers[1])     #KeyError : numbers 에는 1의 키값이 존재하지 않음
```
<caption>Out 3</caption>

```text
KeyError 1
```
### 생성자의 인자

`defaultdict` 생성자의 첫번째 **인자**는 클래스의 **생성자** 또는 **객체를 반환하는 함수**입니다.  
따라서 `int` , `list`, `dict`, 등 빌트인 클래스 뿐만 아니라 객체를 반환하는 사용자 지정 함수로도 할 수 있습니다.
<caption>In 4</caption>

```py
dc = defaultdict(lambda :[1,2,3])
dc[0].append(4)
print(dc[0])
```
<caption>Out 4</caption>

```text
[1, 2, 3, 4]
```


