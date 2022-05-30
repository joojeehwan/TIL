# SUM, MAX, MIN



1. ## 최대 / 최소값 구하기(1-2)

## 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME                                                         | TYPE       | NULLABLE |
| ------------------------------------------------------------ | ---------- | -------- |
| [ANIMAL_ID](https://www.notion.so/ANIMAL_ID-86496563497540f7b4df0adc1706406e) | VARCHAR(N) | FALSE    |
| [ANIMAL_TYPE](https://www.notion.so/ANIMAL_TYPE-fcb0d49e200f4d6fbbb8510b8874f58e) | VARCHAR(N) | FALSE    |
| [DATETIME](https://www.notion.so/DATETIME-085b50de2f024d17bb8ecf11ccdd6fff) | DATETIME   | FALSE    |
| [INTAKE_CONDITION](https://www.notion.so/INTAKE_CONDITION-c90faf4e78484d4dbcc52893a450ef55) | VARCHAR(N) | FALSE    |
| [NAME](https://www.notion.so/NAME-18230e2878324df6bc4f76a8af583e3b) | VARCHAR(N) | TRUE     |
| [SEX_UPON_INTAKE](https://www.notion.so/SEX_UPON_INTAKE-a4f78891d7a54a92826cc8094b4bc284) | VARCHAR(N) | FALSE    |

 

❓

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

 

### 예시

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME               | INTAKE_CONDITION | NAME                                                         | SEX_UPON_INTAKE |
| --------- | ----------- | ---------------------- | ---------------- | ------------------------------------------------------------ | --------------- |
| A399552   | Dog         | @Oct 14, 2013 3:38 PM  | Normal           | [Jack](https://www.notion.so/Jack-de36f88e8664489c99de9b2d680690ce) | Neutered Male   |
| A379998   | Dog         | @Oct 23, 2013 11:42 AM | Normal           | [Disciple](https://www.notion.so/Disciple-73c16d6e6e3d40518fffcf699a6e7ddb) | Intact Male     |
| A370852   | Dog         | @Nov 3, 2013 3:04 PM   | Normal           | [Katie](https://www.notion.so/Katie-94a36add7a424bd983bc7c3cf8923b3c) | Spayed Female   |
| A403564   | Dog         | @Nov 18, 2013 5:03 PM  | Normal           | [Anna](https://www.notion.so/Anna-80f9136aacfa493a8f25d914798a05ed) | Spayed Female   |

 

가장 늦게 들어온 동물은 Anna이고, Anna는 2013-11-18 17:03:00에 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| 시간                                                         |
| ------------------------------------------------------------ |
| [2013-11-18 17:03:00](https://www.notion.so/2013-11-18-17-03-00-d5999b611838486b919181cc58d8f12a) |

※ 컬럼 이름(위 예제에서는 시간)은 일치하지 않아도 됩니다.

 

## 정답

```mysql
SELECT MAX(DATETIME) 
  FROM ANIMAL_INS
```

 

## 풀이

### MAX 구문

```mysql
SELECT MAX(column_name) 
  FROM table_name
 WHERE condition;
```

MAX 구문의 문법은 위와 같습니다. 해당 구문은 선택한 컬럼에서 가장 큰 값을 가져옵니다.

 

자 간단하죠? 그럼 다시한번 문제를 봅시다.

❓

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

````mysql
SELECT MIN(DATETIME) FROM ANIMAL_INS
````



`DATETIME`(보호 시작일)이 가장 최근인 동물의 보호 시작일이란, `DATETIME`의 값이 가장 큰 값을 가져오면 됩니다. 이 때 사용할 수 있는 게 바로 `MAX` 구문입니다.



----

2. ## 동물의 수 구하기 



## 문제 설명

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME                                                         | TYPE       | NULLABLE |
| ------------------------------------------------------------ | ---------- | -------- |
| [ANIMAL_ID](https://www.notion.so/ANIMAL_ID-4a7408943ad74932ba489610a43bdf97) | VARCHAR(N) | FALSE    |
| [ANIMAL_TYPE](https://www.notion.so/ANIMAL_TYPE-8703452941cd4e26a57ac22a84ff4151) | VARCHAR(N) | FALSE    |
| [DATETIME](https://www.notion.so/DATETIME-d669b335fb154ebd9a25f509c6586162) | DATETIME   | FALSE    |
| [INTAKE_CONDITION](https://www.notion.so/INTAKE_CONDITION-ef2a39009a8d424c80adfb820d2dfca9) | VARCHAR(N) | FALSE    |
| [NAME](https://www.notion.so/NAME-dceed4bf326e4bd08c0c4de48aeaaee9) | VARCHAR(N) | TRUE     |
| [SEX_UPON_INTAKE](https://www.notion.so/SEX_UPON_INTAKE-3157503fb8384576a34079318d4af799) | VARCHAR(N) | FALSE    |

 

❓

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

 

### 예시

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME               | INTAKE_CONDITION | NAME                                                         | SEX_UPON_INTAKE |
| --------- | ----------- | ---------------------- | ---------------- | ------------------------------------------------------------ | --------------- |
| A399552   | Dog         | @Oct 14, 2013 3:38 PM  | Normal           | [Jack](https://www.notion.so/Jack-b2162bd39d1f46e1a7fbb5abdbdd1a63) | Neutered Male   |
| A379998   | Dog         | @Oct 23, 2013 11:42 AM | Normal           | [Disciple](https://www.notion.so/Disciple-cff716957f074b21bdfe8a0edc314e3f) | Intact Male     |
| A370852   | Dog         | @Nov 3, 2013 3:04 PM   | Normal           | [Katie](https://www.notion.so/Katie-bf90c05cf2cc4088b302ebce2bd45c0d) | Spayed Female   |
| A403564   | Dog         | @Nov 18, 2013 5:03 PM  | Normal           | [Anna](https://www.notion.so/Anna-c1aabf0c283944719e9d4b71f03b0b49) | Spayed Female   |

 

동물 보호소에 들어온 동물은 4마리입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| count                                                        |
| ------------------------------------------------------------ |
| [4](https://www.notion.so/4-27b45e2344d84c4a854ae351b1a2a25e) |

※ 컬럼 이름(위 예제에서는 count)은 일치하지 않아도 됩니다.

 

## 정답

```mysql
SELECT COUNT(*)
  FROM ANIMAL_INS 
```

 

## 풀이

### COUNT() 함수

SQL에서 `COUNT()` 함수는 WHERE 절이 지정된 기준을 충족하는 행의 수(또는 NULL이 아닌 값)를 반환합니다. 일치하는 열이 없으면 0을 반환합니다

```mysql
COUNT(*)
COUNT( [ALL|DISTINCT] expression )
```

`COUNT()` 함수는 위의 문법으로 사용됩니다. (너무 어려우면 이번 포스트에서는 `COUNT(*)`만 기억합시다.)

 

`COUNT()` 함수의 매개변수로는 4개의 종류가 들어갈 수 있습니다. 아래를 참고하시면 됩니다.

| 이름                                                         | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [ALL](https://www.notion.so/ALL-7e6e45509ad84043aa5810d94271d320) | 모든 값에 적용됩니다. NULL이 아닌 값의 수를 반환합니다.      |
| [DISTINCT](https://www.notion.so/DISTINCT-c24530f5876b448ab782aac210223668) | 중복 값을 무시합니다. 즉 유니크하며 NULL이 아닌 값의 수를 반환합니다. |
| [expression](https://www.notion.so/expression-57c0b052155b4740907c55cc1704cb9a) | 단일 상수, 변수, 스칼라 함수 또는 열 이름으로 구성된 식이며 값을 다른 값과 비교하는 SQL 쿼리일 수도 있습니다. 텍스트 또는 이미지를 제외한 모든 유형의 식입니다. 집계 함수 및 하위 쿼리는 허용되지 않습니다. |
| [*](https://www.notion.so/c18fc9295eb74b3f871741a5c23a7bf3)  | NULL 포함 여부에 관계없이 대상 테이블의 모든 행을 카운트합니다. |

 

### COUNT(*)

문법은 다음과 같습니다.

```mysql
SELECT COUNT(*)
  FROM table_name
 WHERE condition;
```

`COUNT()` 함수는 명시한 WHERE 절을 만족하는 데이터 수를 표시해줍니다. 위의 표에서 설명했듯 `*` 파라미터는 NULL 값을 포함한 수를 보여줍니다.

 

---

----



3. ## 중복 제거하기

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

위 테이블 데이터를 토대로, 동물 보호소에 들어온 **동물의 이름이 몇 개인지 조회**하는 SQL문을 작성해야 합니다.

- 단, 동물의 이름이 중복되는 경우 하나로 칩니다.
- 동물의 이름이 NULL인 경우는 집계하지 않습니다.

------

- 동물의 이름 갯수를 조회하는 것이므로, NAME에 **COUNT 함수를** 적용할 것입니다.
- 컬럼 내 같은 데이터가 존재하면, 중복을 제거하기 위해 **DISTINCT**를 사용합니다.
- **중복 데이터를 제거하고자 하는 열은 NAME 이므로, 옆에 DISTINCT 키워드**를 붙입니다.
- **NULL 값이 아닌 것을 비교하는 방법**은 **IS NOT NULL** 을 붙입니다.

```mysql
 SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL 
```

------

**[DISTINCT 사용 시 주의할 점]**

- DISTINCT 키워드는 옆에 온 모든 컬럼을 고려하여 중복 제거를 진행합니다.

- 즉, **SELECT** DISTINCT COL1, COL2 …를 진행할 경우

  - **COL1과 COL2 값이 모두 동일한 row들을 1개로** 칩니다.

- 다시 말하면, DISTINCT 는 SELECT 구문에 여러 컬럼명이 올 때, 그 중 **한 개에 대해서만 적용할 수 없다는 말이 됩니다.**

  - **SELECT** (DISTINCT COL1), COL2 **FROM …**는 오류입니다.

  - COL1 의 중복된 데이터를 제거한 뒤 COL2를 가져와야 할 텐데, 이 중 어떤 COL2 값을 가져와야 하는지 알 수 없기 때문입니다.

  - | COL1 | COL2 |
    | ---- | ---- |
    | A    | 1    |
    | A    | 2    |
    | B    | 3    |
    | C    | 4    |

    위에서 COL1에 대해서만 DISTINCT를 한다고 예를 들어 보겠습니다.

    A는 중복이 제거되어 A 하나만 보여져야 할 것입니다.

    그러나, 테이블에 열은 2개가 존재합니다.

    **COL1 열 하나에 대해서 중복제거를 하면, COL2 에 있는 값인 1과 2 중 어느 것을 출력해야 하는지 모호합니다.**

    그러므로 DISTINCT 는 모든 컬럼을 고려하여 진행할 수 밖에 없습니다.

