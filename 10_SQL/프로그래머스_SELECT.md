# SELECT



1. ## 모든 레코드 조회하기



ANIMAL_INS 테이블에 동물들의 정보가 담겨 있습니다. 각 테이블에는 다음과 같은 column들이 있습니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

**동물 보호소에 들어온 모든 정보**를 **ANIMAL_ID 순으로**(오름차순) 조회하는 SQL문을 작성해야 합니다.

조회되는 정보들은 모든 column을 포함해야 합니다.

------

조회 : SELECT 문을 활용합니다.

------

모든 열을 조회하므로 * 를 사용하여, 각 테이블의 값들을 SELECT 문으로 검색할 수 있습니다.

그리고 **order by** 를 사용하여, 정렬 기준이 될 컬럼을 지정합니다.

```mysql
1 SELECT * FROM ANIMAL_INS order by ANIMAL_ID 
```

만일, ANIMAL_ID의 역순으로 정렬하고 싶을 경우에는

```mysql
1 SELECT * FROM ANIMAL_INS order by ANIMAL_ID desc; 
```

끝에 **desc**라고 붙입니다. (붙이지 않으면 asc, 즉 오름차순이 기본입니다.)

------

----



## **2. 역순으로 정렬하기**

위와 같은 테이블 데이터로 **NAME과 DATETIME만**을 조회하는데, 정렬 결과는 ANIMAL_ID의 역순으로 조회되어야 합니다.

- 조회하는 열 : NAME, DATETIME
- 정렬 기준이 되는 열 : ANIMAL_ID
- 정렬은 내림차순

```mysql
1 SELECT NAME, DATETIME FROM ANIMAL_INS order by ANIMAL_ID desc; 
```



----

----



## 3.아픈 동물 찾기

ANIMAL_INS 테이블에 동물들의 정보가 담겨 있습니다. 각 테이블에는 다음과 같은 column들이 있습니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

위 정보들에서 아픈 동물(INTAKE_CONDITION=’Sick’)의 아이디와 이름을, 아이디 순으로 조회하는 SQL문을 작성해야 합니다.

------

- 조회 : SELECT 를 활용합니다.
- 조건 : WHERE 절을 활용합니다.
- 정렬 : order by 를 활용합니다.

------

조회할 열은 ANIMAL_ID 와 NAME이고, 그 데이터 중 INTAKE_CONDITION이 Sick 인 row만 출력해야 합니다. 그리고 **order by** 를 사용하여, 정렬 기준이 될 컬럼을 지정합니다.

```mysql
 SELECT ANIMAL_ID , NAME FROM ANIMAL_INS where INTAKE_CONDITION = 'Sick' order by ANIMAL_ID 
```



----

4. ## **어린 동물 찾기**

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

동물 보호소에 들어온 동물 중 젊은 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.

---

- 조회 : SELECT 를 활용합니다.
- 조건 : WHERE 절을 활용합니다.
- 정렬 : order by 를 활용합니다.

----

```mysql
-- aged하지 않은 녀석을 뽑으면 된다. 
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION != "Aged" ORDER BY ANIMAL_ID
```



----

----

5. ## **동물의 아이디와 이름**

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.



---

- 조회 : SELECT 를 활용합니다.
- 조건 : WHERE 절을 활용합니다.
- 정렬 : ORDER BY 를 활용합니다.

---

````mysql
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME ASC, DATETIME DESC;
````

> NAME을 기준으로 한번 오름차순 정렬한 다음
>
> 이름이 동일한 조건들로는 DATETIME 기준으로 내림차순 정렬을 해서 반환하게 된다



----

----

7. ## **상위 n개 레코드**

ANIMAL_INS 테이블에 동물들의 정보가 담겨 있습니다. 각 테이블에는 다음과 같은 column들이 있습니다.

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |

이 데이터들 중에서 가장 먼저 들어온 동물의 이름을 조회해야 합니다.

------

- 조회 : SELECT 를 활용합니다.
- **Oracle의 경우 인라인 뷰**를 활용해 **rownum** 으로 조회할 수 있습니다.

------

## **MySQL**

- MySQL의 경우 : NAME 값을 조회하는데 **가장 맨 위 행 1개만**을 조회하기 위해 **LIMIT 구문**을 사용해야 합니다.
- LIMIT 1 : 맨 위에서부터 1개까지의 정보 조회
- LIMIT 3 : 맨 위에서부터 3개까지의 정보 조회
- LIMIT 2, 6 : 위에서 2번째부터 6번째까지의 정보 조회

```mysql
1 2 3 4 SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME LIMIT 1 
```



----


