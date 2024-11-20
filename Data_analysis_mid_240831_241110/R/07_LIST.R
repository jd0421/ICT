# 리스트 선언
lista <- list()

# 리스트 각 큰 방에 자료형 투입
# 리스트는 
lista[[1]] <- m2
lista[[2]] <- c(1, 2, 3)
lista[[3]] <- c("3", "2", "1")

# 리스트는 write csv 가 불가능하므로 RData 형식으로 저장해야 함
# 저장과 로드
save(lista, file = "lista.RData")
load("list.RData")

## for문 이용하여 character > numeric 으로 변환

m <- matrix(1:15, ncol = 3, byrow = T)
str(m)

m[, 1] <- as.character(m[, 1])
m <- data.frame(m)
str(m)


for (i in 1:ncol(m)) {
    m[, i] <- as.numeric(m[, i])
}
str(m)
