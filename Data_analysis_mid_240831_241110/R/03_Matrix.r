# matrix 생성, 1~15 값, ncol = 3
# byrow argument의 default 값은 f, column 방향으로 값이 떨어져 내려감 

matrix(1:15, ncol =3, byrow = T)

## > matrix(1:15, n)     [,1] [,2] [,3]
##[1,]    1    6   11
##[2,]    2    7   12
##[3,]    3    8   13
##[4,]    4    9   14
##[5,]    5   10   15

# if byrow = T
## > matrix(1:15, ncol =3, byrow = T)
##     [,1] [,2] [,3]
##[1,]    1    2    3
##[2,]    4    5    6
##[3,]    7    8    9
##[4,]   10   11   12
##[5,]   13   14   15

# matrix 접근

## matrix 생성 후 m 변수에 할당
m <- matrix(1:15, ncol = 3, byrow = T)
m[2, 2] # 2행 2열 접근
m[3, 3] # 3행 3열 접근

## 1행 모든 열 접근, 아래 2개 방식은 동일
## 행렬은 , 기준으로 앞에는 행에 대한 정보, 뒤에는 열에 대한 정보
m[1, c(1, 2, 3)]
m[1, ]

## 1행 제외 하고 출력
m[-1, ]

## 1열 제외 하고 출력
m[, -1]

## 1행, 3행만 출력
m[c(1, 3), ]

## 1행, 3행 제외하고 출력
m[-c(1, 3), ]

## 2~4행, 2, 3열 만 출력
m[2:4, c(2, 3)]

### matrix 의 경우 각 column의 자료형이 모두 같아야 함. datframe 의 경우 각 column의 자료형이 달라도 문제 없음. 그래서 dataframe 형식으로 변환 후 작업을 권장

## dataframe 생성
m2 <- data.frame(m)

## str() : 변수의 자료형과 값을 함께 출력
str(m2)

## m2 dataframe의 1열 값을 numeric > character 로 변경 
m2[, 1] <- as.character(m2[, 1])
str(m2)

## m2 dataframe을 matrix 형태로 변경하여 m3에 저장
m3 <- as.matrix(m2)
m3

# ifelse 문
# r fator 형 

## 내 matrix dataframe 변수형에 있는 변수에 대해서 character 형이다, 무언가 요소가 있는 자료형을 factor 형이라 한다
## factor 형은 숫자로 바꿔줘야 함

# column 명으로 접근 : 변수명$ 

m2$X1


## 신규 column을 추가
m2$X4 <- c(1, 2, 3, 4, 5)
m2