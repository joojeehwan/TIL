# JOIN

### 조인이란 ?

조인(Join)은 SELECT와 더불어 가장 많이 사용하는 옵션 중 하나이고, 두 개 이상의 테이블을 묶어서 하나의 결과 집합으로 만들어 내는 것입니다. 즉, 서로 다른 테이블에서 데이터를 가져올 때 사용하는 것이 조인(Join)입니다.



### INNER JOIN(내부 조인)

INNER JOIN은 조인 중 가장 많이 사용됩니다. 따라서 보통 JOIN을 얘기할 때는 INNER JOIN을 말하는 것입니다. 예를 들어, 쇼핑몰 사이트에서 사용자가 물건을 구매하기 위해서는 구매 테이블에 물품, 수량 등을 입력할 것이며, 외래키인 ID와 함께 삽입될 것입니다. 물품을 구매하고 배송을 할 때는 그 구매 테이블에 있는 정보 뿐만 아니라 사용자 테이블에 있는 배송 주소, 전화번호 등을 함께 알아야 합니다. 이 때 사용하는 것이 INNER JOIN입니다.

```mysql
SELECT <열 목록>
FROM <기준 테이블>
    INNER JOIN<참조할 테이블>
    ON <조인 조건>
[WHERE 검색조건]
```

위 형식에서 INNER JOIN이 아닌 그냥 JOIN으로 써도 INNER JOIN으로 인식합니다.

```mysql
USE shopDB
SELECT *
FROM buyTBL
    INNER JOIN userTBL
    ON buyTBL.userID = userTBL.userID
WHERE buyTBL.userID = 'LEE';
```



이렇게 작성하면 buyTBL의 userID와 userTBL의 userID가 같은 테이블끼리 합쳐진 결과를 검색하게 됩니다. 그리고 제일 아랫줄에 WHERE에서 userID가 'LEE'라는 조건을 두었으니, buyTBL의 userID가 'LEE'인 행들만 검색할 것입니다. 

 

여기서 모든 열을 검색할 필요는 없기 때문에 SELECT *이 아니라 buyTBL.userID, prodID, amount, name, addr, phoneNumber 라던지 필요한 열만 검색하면 될 것입니다. 



 

JOIN은 두 개 이상의 테이블을 결합하기 때문에 결합하는 테이블들이 동일한 열을 가지고 있다면 '테이블이름.열이름' 형식으로 테이블명을 명시해줘야 에러가 발생하지 않습니다. 가장 안전한 방법은 모든 열이름에 테이블명을 붙혀주는 것입니다.

```mysql
SELECT BuyTBL.userID, BuyTBL.prodID, BuyTBL.amount, UserTBL.name, UserTBL.addr, UserTBL.phoneNumber
FROM buyTBL B
INNER JOIN userTBL U
ON B.userID = U.userID
```

하지만 이렇게 하면 코드가 길어져 복잡해집니다. 검색할 열이 많다면 코드는 더 길어질 것입니다.

```mysql
SELECT B.userID, B.prodID, B.amount, U.name, U.addr, U.phoneNumber
FROM buyTBL B
INNER JOIN userTBL U
ON B.userID = U.userID
```

간결하게 하기 위해서 각 테이블에 별칭(Alias)를 줄 수 있습니다. 가독성과 안전성을 위해 적극 권장하는 방식입니다.

```mysql
SELECT *
FROM buyTBL, userTBL
WHERE buyTBL.userID = userTBL.userID;
```

단순히 FROM에 테이블을 여러 개 작성해서 조인하는 방법도 있지만 호환성 등의 문제로 권장되지 않습니다.

 



### OUTER JOIN(외부 조인)

INNER JOIN은 양쪽 테이블에 모두 내용이 있는 경우에만 결과가 검색되고, OUTER JOIN은 한쪽 테이블에만 내용이 있어도 결과가 검색됩니다. 자주 사용되지는 않지만 가끔 유용하게 사용되는 방식입니다.

```mysql
SELECT <열 목록>
FROM <첫 번째 테이블(LEFT)>
    <LEFT | RIGHT | FULL> [OUTER] JOIN <두 번째 테이블(RIGHT)>
    ON <조인 조건>
[WHERE 검색조건];
```

OUTER JOIN은 기준 테이블 내용의 누락 없이 검색하면서도, 대상 테이블의 내용을 가져올 수 있습니다. 두 가지 테이블의 내용을 한 번에 가져올 수도 있습니다.

 

OUTER JOIN 앞에 LEFT를 쓰면 첫 번째 테이블의 내용은 두 번째 테이블과 연계되는 내용이 없더라도 모두 검색되어야 한다는 뜻입니다. RIGHT는 두 번째 테이블의 내용은 모두 검색되어야 한다는 뜻이고 FULL은 모든 테이블의 내용이 모두 검색되어야 한다는 뜻입니다. OUTER는 생략 가능합니다.

```mysql
SELECT U.userID, U.addr, U.phoneNumber, B.prodID
FROM userTBL U
    LEFT OUTER JOIN buyTBL B
    ON U.userID = B.userID
WHERE B.prodID IS NULL
ORDER BY U.userID;
```



OUTER JOIN을 이용하면 구매내역이 없는 유저만을 검색할 수 있습니다. 위는 예시입니다.

 

### CROSS JOIN(상호 조인) 



![img](https://blog.kakaocdn.net/dn/cpPkSd/btqOhvq115n/zH4B6H5FTvdQW2gYZXsVf0/img.png)



CROSS JOIN은 한쪽 테이블의 행 하나당 다른 쪽 테이블의 모든 행을 하나씩 모든 행들을 각각 조인합니다.

즉, A 테이블의 1번 행을 B 테이블의 1번 행에 조인 시키고, 다음은 A 테이블의 1번 행을 B 테이블의 2번 행에 조인시키고 ...생략... 이를 모든 A 테이블의 행에 각각 모든 B 테이블의 행들에 조인합니다. CROSS JOIN의 결과 행의 개수는 [A 테이블 행의 개수 X B 테이블 행의 개수]가 됩니다.

CROSS JOIN은 카티션 곱(Catesian Product)이라고도 부릅니다. 

```mysql
SELECT * FROM ATable
CROSS JOIN BTable;
```

기본적인 CROSS JOIN 구문입니다. INNER과 OUTER 조인과 달리 ON 구문은 사용하지 않습니다. SELECT * FROM ATable, BTable; 형식으로 작성할 수도 있는데 호환성 등의 이유로 권장되지 않습니다.

 

### SELF JOIN(자체 조인)

SELF JOIN은 자신에게 조인하는 것입니다. 같은 테이블에 두 번 참조해야 하는 경우도 있습니다.

| 곤충   | 천적 | 수명  |
| ------ | ---- | ----- |
| 거미   | 참새 | 1년   |
| 메뚜기 | 거미 | 6개월 |
| ...    |      |       |

 

곤충 도감 테이블이 있다고 가정합시다. 이 테이블에서 '메뚜기'의 천적 곤충의 이름, 천적, 수명을 검색하려면 어떻게 해야 할까요?

```mysql
SELECT 이름, 천적, 수명
FROM 곤충테이블
WHERE 이름 = ( SELECT 천적
               FROM 곤충테이블
               WHERE 곤충 = '메뚜기');
```

위의 형식으로 서브 쿼리문을 이용할 수 있습니다.

```mysql
SELECT B.곤충, B.천적, B.수명
FROM 곤충도감 A
    INNER JOIN 곤충도감 B
    ON A.천적 = B.곤충
WHERE A.곤충 = '메뚜기';
```

SELF JOIN 시켜서 정보를 확인할 수도 있습니다. 두 가지 다 결과는 [거미, 참새, 1년]이 나올 것입니다. SELF JOIN을 사용할 때는 반드시 별칭을 이용해서 논리적으로 두 개의 테이블을 분리시켜야 합니다.



---

---



# INNER JOIN과 OUTER JOIN의 차이 


![img](https://blog.kakaocdn.net/dn/Jp2Vf/btqE33quGjY/9kvKNZGxK6Z1eDT3VHYAek/img.png)



####  

### **INNER JOIN** 

**Inner join**은 쉽게말해서**교집합** 이라고 표현된다. 

또한 쿼리는 다음과 같은 방법들로 작성된다.

```
select * 
from A 
inner join B on A.번호= B.번호
select *
from A,B
A.번호=B.번호
```



![img](https://blog.kakaocdn.net/dn/dfAaJp/btqE2tpEeo9/hAVVa3o3FP790ZzBiO5pCK/img.png)



INNER JOIN된 결과를 보면 A 테이블과 B테이블이 **모두 가지고 있는 데이터만이** 검색됨

 

 

### **OUTER JOIN** 

OUTER JOIN은 FULL OUTER JOIN의 경우 빼고는 **특정 테이블을 기준으로 데이터를 보여준다.**

Outer join은 **Full Outer Join / Left Outer Join / Right Outer Join** 크게 세가지 종류로 나누어 진다.

 

먼저

#### **1.LEFT OUTER JOIN**

Left Outer Join은 **왼쪽 테이블 기준으로 JOIN 하겠다는 것** 
왼쪽 테이블 **A 의 모든 데이터**와 **A와 B 테이블의 중복데이터**들이 검색됨

 

쿼리는 아래와 같은 방식으로 작성

```
select * from A LEFT OUTER JOIN B ON (A.번호 = B.번호)
select * from A ,B WHERE A.번호(+) = B.번호;
```



![img](https://blog.kakaocdn.net/dn/eb6dKq/btqE42qPl9E/HmM4YZlkk2C8HO730kUzHK/img.png)



 

#### **2.RIGHT OUTER JOIN**

RIGHT OUTER JOIN은 오른쪽 테이블 기준으로 JOIN 하겠다는 것 
**오른쪽 테이블 B 의 모든 데이터와 B와 A 테이블의 중복데이터들**이 검색됨

 



![img](https://blog.kakaocdn.net/dn/bj8SA2/btqE4Csupbr/NVJUoxUKuTMVMgqm8pDonk/img.png)

![img](https://blog.kakaocdn.net/dn/PuHTd/btqE13ymgOR/OtNiJ9rF9ZWhwKAanVKyEK/img.png)



 

----

---



1. ## 없어진 기록 찾기

## **[프로그래머스] 없어진 기록 찾기**

------

ANIMAL_INS 테이블과 ANIMAL_OUTS 테이블 두 개를 활용하여 쿼리문을 작성하는 문제입니다.

**ANIMAL_OUTS 테이블에는 있는데, ANIMAL_INS 테이블에는 없는** 동물들의 ID와 이름을 조회해야 합니다.

------

- 등장하는 개념
  - JOIN, LEFT OUTER JOIN

------

## **JOIN 의 활용**

JOIN은 두 테이블의 데이터를 **일정한 조건에 의해 연결하여 마치 하나의 테이블처럼 만드는 것**으로 볼 수 있습니다.

주로 많이 쓰이는 것으로 INNER JOIN과 LEFT OUTER JOIN을 들 수 있습니다.

------

### **LEFT OUTER JOIN**

![img](https://i.imgur.com/FJofY18.png)

- 위 그림처럼 두 테이블이 존재한다고 가정해 보겠습니다.
- **두 테이블의 JOB 이 같은 것을 기준으로 LEFT OUTER JOIN을 진행합니다.**
- LEFT OUTER JOIN은 왼쪽에 오는 테이블을 기준으로, 오른쪽에 오는 테이블과 비교하여 조건에 맞는 값이 있으면 JOIN하여 가져오고, 값이 없으면 null 값을 표시합니다.
- 즉 LEFT OUTER JOIN은 이처럼 JOIN 문을 수행할 때, 왼**쪽에 있는 데이터는 무조건 가져오며, 오른쪽에 오는 테이블과 JOIN을 수행하여 조건에 맞는 데이터가 없을 시 null 로 표시**하게 됩니다.
- 위의 그림에 나온 결과표를 참고해 주세요.
  - **TABLE_ONE**에 있는 **aaa**는 **JOB 이 student** 입니다.
  - TABLE_TWO 에 JOB이 student 인 값들과 LEFT OUTER JOIN이 수행되어 모두 연결이 됩니다.
  - 하지만 **TABLE_ONE**에 **ddd**는 **JOB이 athlete** 이지만, **TABLE_TWO 에는 JOB이 athlete 인 데이터가 없습니다.**
  - 그러므로 LEFT OUTER JOIN을 수행하면, 왼쪽 테이블의 데이터인 ddd는 결과에도 무조건 표시되지만, **오른쪽 테이블에 같이 연결할 데이터가 없으므로 NULL 값을 표시**하게 됩니다.

------

**LEFT OUTER JOIN**을 활용하여 문제를 풀 수 있습니다.

문제에서는, **입양을 간 기록(ANIMAL_OUTS)** 은 **있지만**, **들어온 기록(ANIMAL_INS) 은 없는** 데이터를 조회해야 합니다.

LEFT OUTER JOIN을 어떻게 사용하면 될까요?

- **입양을 간 기록은 존재**한다고 하였으므로, JOIN 결과에는 ANIMAL_OUTS 데이터가 무조건 나오게 해야 할 것입니다. 따라서 JOIN 문 왼쪽에 ANIMAL_OUTS 테이블이 와야 할 것입니다.
- ANIMAL_OUTS 와 ANIMAL_INS 를 **ANIMAL_ID가 같은 것을 기준으로 LEFT OUTER JOIN** 하면,
  - ANIMAL_OUTS 테이블에 존재하는 ANIMAL_ID와, 그 ANIMAL_ID와 같은 ANIMAL_INS 테이블의 데이터가 옆에 같이 연결될 것입니다.
  - 그러나 **ANIMAL_ID가 같은 값이 ANIMAL_INS 테이블에 존재하지 않는다면, NULL 값으로 연결**될 것입니다.
  - 이를 통해, ANIMAL_OUTS 에는 있지만 ANIMAL_INS에는 없는 ANIMAL_ID 의 값을 조회할 수 있게 됩니다.

```mysql
SELECT OUTS.ANIMAL_ID, OUTS.NAME 
FROM ANIMAL_OUTS OUTS 
LEFT OUTER JOIN ANIMAL_INS INS 
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID 
WHERE INS.ANIMAL_ID is NULL 
ORDER BY OUTS.ANIMAL_ID 
```

- **오른쪽에 연결될 INS의 자료가 null 인 것으로부터(where 조건 참조) 찾을 수 있습니다.**

### RIGHT JOIN으로 푼 예제

```mysql
SELECT b.ANIMAL_ID, b.NAME
FROM ANIMAL_INS a RIGHT JOIN ANIMAL_OUTS b ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE a.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID;
```

### LEFT JOIN으로 푼 예제

```mysql
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A LEFT JOIN ANIMAL_INS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.ANIMAL_ID
```





----

----



## 2.있었는데요 없었습니다.

1번과 똑같은 개념으로 풀면 쉽다. 

# 답변 및 해설

`ANIMAL_INS`에서 `ANIMAL_ID`와 `NAME` 에 대한 정보가 필요하다.

=>  `SELECT ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME FROM ANIMAL_INS`

두 테이블을 `ANIMAL_ID` 기준으로 병햡을 해야지만 입양일이 잘못되었는지 알 수 있다.

=>  `LEFT JOIN ANIMAL_OUTS ON ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID`

입양일(`ANIMAL_INS.DATETIME`)이 보호일(`ANIMAL_OUTS`)보다 빠른 정보를 찾아야 한다.

=>  `WHERE ANIMAL_INS.DATETIME>ANIMAL_OUTS.DATETIME`

그러고 나서 날짜에 따라서 정렬을 해야 한다. 

=> `ORDER BY ANIMAL_INS.DATETIME`



----

---



## 3.오랜 기간 보호한 동물(1)

### 1번 풀이의 연장선

먼저 LEFT JOIN과 WHERE 문에 B.ANIMAL_ID IS NULL을 넣어

A에는 있지만 B에는 없는 값만 뽑아내면 총 4행이 나오는데

 

포인트는 ANIMAL_INS 테이블의 DATETIME 순으로

3행만 뽑아와야 한다는 것이다

ORDER BY A.DATETIME 수행 후

LIMIT 3을 넣어줘서 3행만 가져오면 된다

```mysql
SELECT A.NAME, A.DATETIME 
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE B.ANIMAL_ID IS NULL
ORDER BY A.DATETIME
LIMIT 3
```



---

----



## 4.보호소에서 중성화한 동물

```mysql
SELECT INS.ANIMAL_ID, INS.ANIMAL_TYPE, INS.NAME
FROM ANIMAL_OUTS OUTS
LEFT JOIN ANIMAL_INS INS
ON OUTS.ANIMAL_ID = INS.ANIMAL_ID
WHERE INS.SEX_UPON_INTAKE LIKE 'Intact%' AND (OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%' OR OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY INS.ANIMAL_ID

```



1. 일단, ANIMAL_OUTS의 ANIMAL_ID, ANIMAL_TYPE, NAME이 나와야 한다.

=>  `SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.ANIMAL_TYPE, ANIMAL_OUTS.NAME FROM ANIMAL_OUTS`

2. 그 다음에는 ANIMAL_INS와 ANIMAL_OUTS의 ANIMAL_ID로 JOIN을 해준다. 여기서 LEFT JOIN을 사용하는 이유는 ANIMAL_OUTS에 없는 데이터는 필요없기 때문이다. 

=> `LEFT JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID=ANIMAL_INS.ANIMAL_ID`

3. 그 다음에는 ANIMAL_IN에서 SEX_UPON_INTAKE가 `Intact`,즉, 중성화되지 않은 애들을 찾는다. 

=> `WHERE ANIMAL_INS.SEX_UPON_INTAKE LIKE 'Intact%'`

4. 그 다음에는 ANIMAL_OUTS에서 중성화된 애들만 찾는다. 중성화된 애들은 `Spayed` 혹은 `Neutered`로 시작한다. 

=>`AND (ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Spayed%' OR ANIMAL_OUTS.SEX_UPON_OUTCOME LIKE 'Neutered%')`



### INNER JOIN을 활용한 풀이

````mysql
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A 
INNER JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME
````

