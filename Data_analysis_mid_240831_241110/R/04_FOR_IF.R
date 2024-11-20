# cbind / rbind

## cbind = column bind 
## rbind = row bind 

# 행렬 끼리도 묶을 수 있음
cbind(m2, c(3, 2, 4, 5, 5))
rbind(m2, c(3, 2, 4, 5))

cbind(m2, m2)
rbind(m2, m2)

# for 문

for(i in 1:10) {
    print(i)
}

for(j in c(1,3,5,7)) {
    print(j)
}


# dimension 정보 확인
dim(m2)

# 소괄호는 함수를 의미
# 대괄호는 인덱스 접근
# 중괄호 : 반복문에서 하나의 묶음 을 의미



# for 문을 활용한 binding
## 누적 방식으로 진행하는 방향과 곱 방식으로 진행하는 방향
## 누적 방식 : Null 자료형의 변수 선언 후 누적하는 방식
## 곱 방식 : 기존 선언된 m2 변수에 그대로 할당 시 곱(x2)되어 누적되므로 주의


for(i in 1:10) {
    m2 <- rbind(m2, m2)
    print(dim(m2))
} 

## [1] 10  4
## [1] 20  4
## [1] 40  4
## [1] 80  4
## [1] 160   4
## [1] 320   4
## [1] 640   4
## [1] 1280    4
## [1] 2560    4
## [1] 5120    4

m2 <- matrix(1:15, ncol =3, byrow = T)
dim(m2)

m3 <- NULL

for(i in 1:10) {
    m3 <- rbind(m3, m2)
    print(dim(m3))
} 

## [1] 5 3
## [1] 10  3
## [1] 15  3
## [1] 20  3
## [1] 25  3
## [1] 30  3
## [1] 35  3
## [1] 40  3
## [1] 45  3
## [1] 50  3


# IF문
## cat(i), print 함수와 유사
## for문을 사용할 때에는 cat을 사용해야 함

m3 <- NULL

for (i in 1:10){
    if(i %% 2 ==0) {
        next; # 생략
    }
    m3 <- rbind(m3, m2)
    cat("\n", i)
}

m3