## **[프로그래머스] **

## **1. 고양이와 개는 몇 마리 있을까**

------

프로그래머스의 SQL Kit에 있는 GROUP BY 문제들 중

1. 고양이와 개는 몇 마리 있을까
2. 동명 동물 수 찾기

문제입니다.

------

- 등장하는 개념
  - **GROUP BY 활용하기, HAVING 활용하기**
  - **쿼리문의 실행 순서 숙지하기**

------

## **1. 고양이와 개는 몇 마리 있을까**

ANIMAL_INS 테이블에 동물들의 정보가 담겨 있습니다. 각 테이블에는 다음과 같은 column들이 있습니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

이 데이터들 중에서 고양이와 개가 각각 몇마리인지 조회하는 SQL문을 작성해야 합니다.

ANIMAL_TYPE 명과 함께 COUNT 값을 출력해야 합니다.

------

- 조회 : SELECT 를 활용합니다.
- 수량 세기 : COUNT 를 활용합니다.
- 그룹으로 묶기 : GROUP BY 를 활용합니다.

------

**ANIMAL_TYPE이 같은 것들끼리 GROUP으로 묶어서 조회**하기 위해, GROUP BY를 사용합니다.

ANIMAL_TYPE을 GROUP BY절에 적용하면, **ANIMAL_TYPE 이 같은 것들을 그룹화할 것입니다.**

이에 대하여 COUNT(ANIMAL_TYPE)을 한다면, 그룹화된 것들 각각의 갯수를 구할 수 있게 됩니다.

```mysql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS 
group by ANIMAL_TYPE 
ORDER BY ANIMAL_TYPE
```

- (20.9.25 수정) 추가된 조건으로 cat이 dog보다 앞에 나오도록 해야 합니다. 따라서, 맨 끝에 `ORDER BY ANIMAL_TYPE`을 추가하면 정답으로 처리됩니다.



----

----





## **2. 동명 동물 수 찾기**

위 테이블 데이터를 토대로, 동물 보호소에 들어온 이름들 중 **두 번 이상 쓰인 이름과, 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해야 합니다.**

- 단, 동물의 이름이 없을 경우 집계하지 않습니다.

------

- 동물의 이름 갯수를 조회하는 것이므로, NAME에 **COUNT 함수를** 적용할 것입니다.
- **NULL 값이 아닌 것을 비교하는 방법**은 **IS NOT NULL** 을 붙입니다.
- NAME을 **그룹화**하여, 그것의 갯수를 셀 것이므로 **GROUP BY** 를 활용합니다.
- **HAVING 은 GROUP 화 한 이후에 적용**되는 것으로, 그룹화되어 나온 결과에 **조건식**을 적용합니다.

```mysql
SELECT NAME, COUNT(NAME) 
FROM ANIMAL_INS 
WHERE NAME is NOT NULL
GROUP BY NAME HAVING COUNT(NAME) >= 2 
ORDER BY NAME
```

------

**[GROUP BY, HAVING 설명]**

우선, **쿼리문의 실행 순서**에 대해 알 필요가 있습니다.

**SELECT -** 5순위 (필수)

**FROM -** 1순위 (필수)

**WHERE -** 2순위

**GROUP BY -** 3순위

**HAVING -** 4순위 => <u>GROUP BY의 조건</u>

**ORDER BY -** 6순위

------

즉, 조회 대상 테이블을 가장 먼저 정하고, 그것을 토대로 데이터를 조회합니다.

부가적인 조건을 거는 WHERE, GROUP BY, HAVING, ORDER BY들도 각각의 순서가 있습니다.

이 때, **HAVING 은 GROUP BY가 적용된 이후에 실행**됨을 알 수 있습니다.

**ORDER BY**는 모든 데이터들을 조회가 완료된 다음, 최후에 정렬함을 알 수 있습니다.



----

----

## **[프로그래머스] 입양 시각 구하기(1), (2)**

------

프로그래머스의 SQL Kit에 있는 GROUP BY 문제들 중

1. 입양 시각 구하기(1)
2. 입양 시각 구하기(2)

문제입니다.

------

- 등장하는 개념
  - **GROUP BY 활용하기, HAVING 활용하기**
  - 시간에서 시간대를 추출하는 **HOUR** 함수
  - SQL에서 변수를 선언하는 **SET**
  - **프로시저가 끝나도 계속 유지**되는 @ 변수

------

## **1. 입양 시각 구하기 (1)**

ANIMAL_OUT 테이블에 동물들의 정보가 담겨 있습니다. 각 테이블에는 다음과 같은 column들이 있습니다.

| NAME            | TYPE       | NULLABLE |
| --------------- | ---------- | -------- |
| ANIMAL_ID       | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE     | VARCHAR(N) | FALSE    |
| DATETIME        | DATETIME   | FALSE    |
| NAME            | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE    |

이 데이터들 중에서 **입양 시각 시간대를 기준으로 COUNT 하는 쿼리문**을 작성해야 합니다.

------

- 조회 : SELECT 를 활용합니다.
- 수량 세기 : COUNT 를 활용합니다.
- 그룹으로 묶기 : GROUP BY 를 활용합니다.
- 시간 추출 : HOUR 을 활용합니다.

------

- **TYPE이 DATETIME 인 데이터에서 시간만 추출하려면 HOUR을 사용합니다.**

```mysql
SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT 
FROM ANIMAL_OUTS 
GROUP BY HOUR(DATETIME) 
HAVING HOUR >= 9 and HOUR <= 19 
```

- SELECT 문의 **HOUR(DATETIME) HOUR** 은, 조회 결과 나온 **열의 이름을 HOUR로 설정하겠다는 뜻**입니다.
- HAVING을 사용하지 않고, 아래와 같이 **WHERE**를 이용할 수도 있습니다.

```mysql
SELECT HOUR(DATETIME) HOUR, COUNT(DATETIME) COUNT 
FROM ANIMAL_OUTS 
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19 
GROUP BY HOUR(DATETIME) 
ORDER BY HOUR
```

- **시간 순으로 정렬**하려면 맨 끝에 `ORDER BY HOUR` 를 입력해야 합니다.

------

## **2. 입양 시각 구하기(2)**

위 테이블 데이터를 토대로, **입양 시간대별로 입양이 몇 건이나 발생했는지 조회**해야 합니다.

- **(1) 과 다른 점이라면, 모든 시간대(0시~23시)를 조회해야 합니다.**
- 갑자기 난이도가 상승한 레벨 4의 문제로, **쿼리문에서 로컬 변수를 활용하는 문제**입니다.

------

```mysql
SET @hour := -1; -- 변수 선언 
SELECT (@hour := @hour + 1) as HOUR, (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) as COUNT 
FROM ANIMAL_OUTS 
WHERE @hour < 23 
```

------

- SET 옆에 변수명과 초기값을 설정

  할 수 있습니다.

  - @가 붙은 변수는 프로시저가 종료되어도 **유지**된다고 생각하면 됩니다.
  - 이를 통해 값을 누적하여 0부터 23까지 표현할 수 있습니다.

- @hour은 초기값을 -1로 설정합니다. PL/-SQL 문법에서 **:=**은 비교 연산자 =과 혼동을 피하기 위한의 **대입 연산**입니다.

- SELECT (@hour := @hour +1) 은 @hour의 값에 1씩 증가시키면서 SELECT 문 전체를 실행하게 됩니다.

- 이 때

   

  처음에 @hour 값이 -1 인데, 이 식에 의해 +1 이 되어 0

  이 저장됩니다.

  - HOUR 값이 0부터 시작할 수 있습니다.
  - WHERE @hour < 23일 때까지, @hour 값이 **계속 + 1씩 증가**합니다.