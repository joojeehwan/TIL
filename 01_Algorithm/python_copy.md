

안녕하세요. BlockDMask입니다.
오늘은 파이썬 얕은 복사, 깊은 복사에 대해서 정리해보려 합니다.
은근히 헷갈려서 천천히 한번 정리해볼게요.

**<목차>**
**1. 파이썬 얕은 복사**
**2. 파이썬 깊은 복사
\3. 그림으로 총 정리 (1, 2 다 읽고 오면 이해 완벽)**

이 글을 보기 전에 필요한 사전 지식.
\- mutable, immutable 객체에 대한 지식이 필요합니다. 관련 포스팅 [**[바로가기\]**](https://blockdmask.tistory.com/570)

 

## **1. 파이썬 얕은 복사 ([:], copy, copy.copy)**

------

후 좀 길었습니다. 1번이 이해가 되었다면 이제 얕은 복사와 깊은 복사를 이해할 차례입니다.
헷갈릴 수 있어서, 잠시 정리의 시간을 가지고 읽기를 추천드립니다.

지난 시간에 배운 [**immutable, mutable**](https://blockdmask.tistory.com/570) 객체를 생각해보면 조금 쉬울 것입니다.

### **1-1) 얕은 복사 사용 방법 및 특징 (immutable, mutable 객체의 복사)**

**얕은 복사라는 것은 변수를 복사했다고 생각했지만** **실제로는 연결**되어있는 것을 의미합니다.
좀 더 자세히 이야기하자면,
**변수를 복사했지만 참조한 곳은 동일하**기 때문에 **같은 변수**를 가리키고 있는 것입니다.

그림으로 한번 볼까요?

**arr1 = [1,2,3]이고**
**arr2 = arr1**
이렇게 리스트에 **'='을 해서 복사(얕은복사)**를 했다고 하면 아래와 같은 그림이 됩니다.



![img](https://k.kakaocdn.net/dn/Gd7Qq/btrh0CounXW/QoBdD4qF4JkH92uVjba33k/img.png)python shallow copy



우리는 복사를 했다고 생각하지만 사실 복사한 것은 참조(메모리 주소)만 복사한 것이지 실제 객체 전체를 복사한것이 아닙니다.
그렇기 때문에 여기서 arr1에 append를 통해서 값을 추가하거나 한다면, arr2에도 동일하게 적용되는 것입니다.
**(같은 곳을 참조하기 때문에)**

**arr1.appned(4)을 해보면 아래와 같은 그림이 됩니다.**



![img](https://k.kakaocdn.net/dn/bqC6r5/btrhZNJOrow/NlM67mgX4cdUTj51IUAkr1/img.png)



같은곳을 가리키기 때문에 arr1에서 4 값이 추가되면, arr2 도 4가 적용이 됩니다.
이렇게 복사를 했음에도, 값을 변경하면 다른 변수에도 영향을 끼치도록 **'참조'만 복사한 것을 얕은 복사**라고 합니다.

 

**immutable 한 객체들 int, float 등은 얕은 복사를 하던 깊은 복사를 하던 사실 상관이 없습**니다.
왜냐하면 **해당 객체들은 값이 변경되면 '무조건' 참조가 변경**되기 때문에
얕은 복사를 해서 값을 변경하더라도, 참조하던 다른 객체의 값도 변경되거나 하지 않기 때문입니다.

immutable 객체인 int 타입으로 예시를 한번 들어보겠습니다.
아래 그림을 보면
**num1 = 3**
**num2 = num1**
을 하게 되면 메모리 상에서 그림이 이렇게 될 것입니다.
**num1, num2 가 3이라는 값을 가진 메모리 공간을 같이 참조하겠죠?**



![img](https://k.kakaocdn.net/dn/yNkPY/btrhVDHYjVz/4qKcKpLk5UApdThJ0ZFJH1/img.png)python copy



이때 **num1 = 4를** 하게 되면,**
**immutable 객체는 값이 변경될 수 없기 때문에
새롭게 메모리를 할당해서 4라는 값을 생성하고
그곳을 num1 이 참조하게 합니다.

그럼 **num1, num2는 다른 곳을 가리키게 됩니다.**



![img](https://k.kakaocdn.net/dn/dJWeuT/btrh50aRU77/F7cN2KkpYsNM2xoI33t491/img.png)python copy



결론적으로 **파이썬에서는 "얕은 복사"냐 "깊은 복사"냐에 대해서 구분하고 학습해야 하는** 객체는
int, float와 같은 immutable 한 객체들이 아니라 (X)
**list, set, dictionary와 같은 mutable 한 객체들입니다. (O)**

이해가 되었나요? 그럼 이제 얕은 복사를 하는 방법들에 대해서 알아보겠습니다.

 

mutable 객체의 얕은 복사를 하는 방법은 4가지입니다.

 

### **1-2) '=' 대입 연산자를 이용한 얕은 복사**

위에서 설명한 int, list를 비교해 보면서 보시면 좋을 것 같습니다.
이번 예제까지만 immutable 타입인 int 타입 예제를 들고 아래에서부터는 mutable 타입만 예제로 쓰겠습니다.
(어차피 immutable 타입은 깊은, 얕은 복사 구분이 상관없기 때문입니다. 이유는 위에서 설명했습니다.)

```
# mutable 한 객체 (리스트)
print('=' * 50)

arr1 = [1, 2, 3]
arr2 = arr1     # '=' 복사

print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

arr2.append(99)  # arr2 에 값 추가

print('\narr2.append(99)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')


# immutable 한 객체 (int)
print('=' * 50)

num1 = 30
num2 = num1     # 복사

print(f'num1 : {num1}, add : {hex(id(num1))}')
print(f'num2 : {num2}, add : {hex(id(num2))}')

num2 += 1
print('\nnum2 += 1')
print(f'num1 : {num1}, add : {hex(id(num1))}')
print(f'num2 : {num2}, add : {hex(id(num2))}')
```



![img](https://k.kakaocdn.net/dn/2aKVZ/btrhX1oPXTf/dfQo7RMJiNsdooc5LPWFjK/img.png)python = copy



**- mutable 한 객체인 리스트 예제**
arr1, arr2를 '='을 통해서 복사를 하고 값과 주소를 보면 동일한 곳을 가리키고 있는걸 알 수 있습니다.
여기서 arr2.append(99)를 통해서 arr2에 값을 추가한 후에
arr1, arr2 를 둘 다 출력을 해보면
둘다 [1,2,3]에서 [1,2,3,99]로 값이 변경된 것을 알 수 있고, 참조하는 주소 또한 동일한 것을 알 수 있습니다.

이것이 참조만 복사하는 얕은 복사입니다. 

**- immutable 한 객체 int 예제**
int 타입을 복사하면 같은 참조를 가리키게 되고,
**값을 변경했을 때 다른 주소**를 가리키게 되는 것 을 볼 수 있습니다.
결국 각개 다른 참조.

###  

### **1-3) [:] 슬라이싱을 이용한 얕은 복사. (feat 눈속임)**

```
print('=' * 50)

arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1[:]  # 여기서 복사

print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2 에 값 추가
print('arr2.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')
```



![img](https://k.kakaocdn.net/dn/Mfo3b/btrhWayOtOm/ixa8yDhZcwkGnVCSzgavJk/img.png)python [:] copy




**1. 전체 출력**
arr1을 [:] 리스트 슬라이싱을 통해서 arr2에 복사를 했습니다.
전체 출력 부분을 보면 보면 arr1과 arr2가 참조하는 메모리 주소가 다른 것을 볼 수 있습니다.
그래서 딱 봤을 때. "어? 메모리 주소 다르니까 깊은 복사 아니냐" 하실 수 있을 것 같습니다.

**2. 리스트 끝에 값 추가**
그래서 arr2.append(22)를 통해서 리스트 끝에 값을 추가해보았습니다.
그럼 arr1 = [4, 5, 6, [2, 4, 8]] 이 되고
arr2 = [4, 5, 6, [2, 4, 8], 22]로 리스트의 값이 다른 것을 볼 수 있네요.
이렇게만 보면 깊은 복사인 것 같은데.. 왜 얕은 복사라고 하는지 
궁금하시죠?

**3. 리스트 내부 리스트**
"리스트 안에 존재하는 리스트" 이 부분을 보면 확실히 얕은 복사인 게 느껴지실 것입니다.
arr1 [3] 부분이 [4, 5, 6, **[2, 4, 8]**]
arr2[3] = [4, 5, 6, **[2, 4, 8]**, 22] 
바로 저 [2, 4, 8] 리스트인데요. 이 부분의 주소를 출력해보면
두 내부 리스트가 동일한 곳을 가리키고 있는 것을 볼 수 있습니다.
'아 이런 깊은 것 같았지만... 얕은 복사네요' 

**4. 리스트 내부 리스트 값 추가**
그럼 arr1[3] 부분이 정말 얕은 복사가 된 게 맞나 값을 추가해보았습니다.
arr1[3].append(99) 를 추가해서 출력해보니
arr1[3] 은 [2,4,8, 99]가 되었고
arr2[3] 또한 [2,4,8,99]가 된 것을 볼 수 있습니다. ' 야속한 얕은 복사 '이네요..

**5. 전체 출력을 다시 한번 해보면**
arr1 = [4, 5, 6, [2, 4, 8, 99]]
arr1 = [4, 5, 6, [2, 4, 8, 99], 22]
역시나 깊은 복사인 줄 알았던 [:] 슬라이싱이
내부적으로 보면 얕은 복사이었던 것을 알 수 있습니다.
겉에 있는 리스트만 새롭게 객체를 추가했지만 사실 내부에 있는 리스트 요소는 하나의 [2,4,8] 리스트를 가리키고 있던 것이었습니다.

완전한 깊은 복사도 아니고, 완전한 얕은 복사도 아니네요. 그렇지만 이것 또한 얕은 복사로 구분합니다.

 

### **1-4) copy 메서드 이용 (객체에 제공)한 얕은 복사**

copy 메서드, copy 함수를 이용해도 [:]와 동일한 결과가 나옵니다.
설명은 위 1-3) [:] 복사와 동일합니다. 코드와 결과만 첨부하겠습니다.

```
print('=' * 50)

arr1 = [4, 5, 6, [2, 4, 8]]
arr2 = arr1.copy()  # 여기서 복사 copy 메소드 이용

print("1. 전체 출력")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

print("\n2. 리스트의 끝에 값 추가")
arr2.append(22)  # arr2 에 값 추가
print('arr2.append(22)')
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')

# 리스트 안에 있는 리스트
print("\n3. 리스트 내부 리스트")
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[3].append(99)
print('arr1[3].append(99)')
print(f'arr1[3] : {arr1[3]}, add : {hex(id(arr1[3]))}')
print(f'arr2[3] : {arr2[3]}, add : {hex(id(arr2[3]))}')

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, add : {hex(id(arr1))}')
print(f'arr2 : {arr2}, add : {hex(id(arr2))}')
```



![img](https://k.kakaocdn.net/dn/Mfo3b/btrhWayOtOm/ixa8yDhZcwkGnVCSzgavJk/img.png)python list.copy()



 

 

### **1-5) copy 모듈의 copy 함수 이용한 얕은 복사 (딕셔너리 얕은 복사)**

copy 모듈의 copy 함수를 이용해도 얕은 복사를 할 수 있습니다.
import copy를 작성해주어야 합니다.
이번엔 리스트 말고 딕셔너리를 이용해보았습니다.

```
import copy                 # copy 모듈 불러오기
print('=' * 50)

d1 = {'a': 'BlockDMask', 'b': [1, 2, 3]}
d2 = copy.copy(d1)      # copy 모듈 얕은복사

print("1. 전체 출력")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

print("\n2. 딕셔너리에 새 key, value 추가")
d2['c'] = 'kimchi'
print("d2['c'] = 'kimchi'")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')

# 딕셔너리 내부에 리스트 value
print("\n3. 딕셔너리 내부 리스트")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n4. 딕셔너리 내부 리스트에 값 추가")
d1['b'].append('NO')
print("d1['b'].append('NO')")
print(f"d1['b'] : {d1['b']}, address : {hex(id(d1['b']))}")
print(f"d2['b'] : {d2['b']}, address : {hex(id(d2['b']))}")

print("\n5. 딕셔너리 전체 다시 확인")
print(f'd1 : {d1}, address : {hex(id(d1))}')
print(f'd2 : {d2}, address : {hex(id(d2))}')
```



![img](https://k.kakaocdn.net/dn/pzPLv/btrhZnrIYA1/2H2S5bRLqKMdra8T5TJjf0/img.png)python copy.copy dictionary



위 리스트 예제와 동일하게
dictionary 도 복사를 했을 때 d1, d2 객체의 주소가 달라서 깊은 복사처럼 보입니다.

특히 **d2['c'] = 'kimchi'를 통해서 d2 에만 key, value를 추가가 되는 것을 보면 정말 깊은 복사처럼 보이긴 합니다만,**

**d1['b'], d2['b'] 의 value 값인 리스트 [1,2,3]을 보면 주소가 동일한 것**을 볼 수 있습니다.
결과에서 **보시듯이 해당 리스트에 값을 추가하면 d1, d2에 둘 다 추가된 것**을 볼 수 있습니다.

이렇게 다양한 **얕은 복사에 대**해서 알아보았습니다.

 

 

## **2. 파이썬 깊은 복사 (copy.deepcopy)**

------

### **2-1) 깊은 복사 copy.deepcopy**

깊은 복사를 사용하기 위해서는 copy 모듈의 deepcopy 함수를 사용해야 합니다.

**깊은 복사는 리스트 내부 리스트, 딕셔너리 내부 리스트 등 내부에 있는 객체 모두 새롭게 만들어주는 작업**을 합니다.
모든 것 다 새롭게 복사. 그냥 독립적이 되어버림.

 

### **2-3) copy.deepcopy 깊은 복사 코드 예제**

```
import copy                 # copy 모듈 불러오기
print('=' * 50)

arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1)      # copy 모듈 깊은 복사

print("1. 전체 출력")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

print("\n2. 리스트에 새 key, value 추가")
arr1.append(0)
print('arr1.append(0)')
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')

# 리스트 내부에 리스트 추가
print("\n3. 리스트 내부 리스트.")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")

print("\n4. 리스트 내부 리스트에 값 추가")
arr1[2].append(10)
print("arr1[2].append(10)")
print(f"arr1[2] : {arr1[2]}, address : {hex(id(arr1[2]))}")
print(f"arr2[2] : {arr2[2]}, address : {hex(id(arr2[2]))}")

print("\n5. 리스트 전체 다시 확인")
print(f'arr1 : {arr1}, address : {hex(id(arr1))}')
print(f'arr2 : {arr2}, address : {hex(id(arr2))}')
```



![img](https://k.kakaocdn.net/dn/bgxe8L/btrh3poOUWp/RDZgJW81k8azOB4kBsLmrk/img.png)python deepcopy



1 번 전체 출력을 보면
arr1, arr2의 주소 값이 다른 것을 볼 수 있습니다.

**3번의 리스트 내부 리스트도 보면 이전에 얕은 복사와 달리**
**arr1[2], arr2[2] 의 [99, 88, 77]인 리스트 내부 리스트도 주소 값이 다른 것을** 볼 수 있습니다.

그래서 **4번에서 리스트 내부 리스트인 arr1[2]에 값을 추가해도 arr2[2]에는 전혀 영향이 없는 것** 을 알 수 있습니다.

즉, 복사한 이후부터는 '독립적이다.' '둘이 쌩깠다.' '이젠 아무 사이도 아니다.'인 상태가 **"깊은 복사"인 것입니다.**

 

 

## **3. 그림으로 총 정리 (파이썬 깊은 복사, 얕은 복사 끝)**

------



![img](https://k.kakaocdn.net/dn/cYFFT4/btrhZnFeE1q/72WfN762lRdIpZhkNkpER0/img.png)파이썬 얕은 복사 1 : '='&nbsp;(blockdmask)



 



![img](https://k.kakaocdn.net/dn/yCzgY/btrh7ykYNpJ/xdF4vdL5sFBKLWRARCVfF0/img.png)파이썬 얕은 복사 2 : [:], copy.copy, list.copy (blockdmask)



 



![img](https://k.kakaocdn.net/dn/S6TlO/btrh4LZqfOc/4omkkPXdasUPnI4DarIrik/img.png)파이썬 깊은복사 : copy.deepcopy (blockdmask)



 

정리하자면 **얕은 복사는 대입(=), [:] 슬라이싱, 객체.copy, copy.copy** 가 있고
**깊은 복사는 copy.deepcopy가** 있습니다.

이상으로 파이썬 깊은 복사, 얕은 복사에 대해서 알아보았습니다.
mutable, immutable 객체에 대해서 다시 한번 구분해보시고,
mutable 객체에 대한 얕은 복사, 깊은 복사에 대해서 생각해보시면 될 것 같습니다.
감사합니다.

<iframe id="editEntry" src="https://blockdmask.tistory.com/api" style="box-sizing: inherit; max-width: 100%; color: rgb(51, 51, 51); font-family: &quot;Noto Sans KR&quot;, Arial, &quot;Apple SD Gothic Neo&quot;, &quot;Malgun Gothic&quot;, &quot;맑은 고딕&quot;, &quot;Nanum Gothic&quot;, Dotum, 돋움, Helvetica, sans-serif; font-size: medium; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial; position: absolute; width: 1px; height: 1px; left: -100px; top: -100px;"></iframe