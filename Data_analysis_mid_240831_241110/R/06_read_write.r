# read_write

m <- matrix(1:15, ncol= 3, byrow= TRUE)
data.frame(m)

## column name extract
colnames(m2)

## add column name
paste0("v", 1:3)

## put paste0 to m2's column name
colnames(m2) <- paste0("v", 1:3)

m2

## "파일경로" 입력 시 백슬래시 부분은 한 번 더 추가해주어야 함
## G:/내 드라이브/ > G://내 드라이브//

getwd() # 현재 작업 공간 경로
setwd() # change current working directory

# write.csv
## m2를 저장
write.csv(m2, "m2.csv")

# read.csv
## csv 파일을 열람
### 변수 선언 후 read 한 csv 파일을 할당
aaa <- read.csv("m2.csv")
aaa
### read 할 때 rowname 숫자가 같이 들어가므로 이를 제거하고 open 하는 방식을 취해야 함

#### 부를 때 1열 자료를 제외하고 열람
aaa <- read.csv("m2.csv")[, -1] 
#### 저장할 때 row nmames를 삭제 
write.csv(m2, "m2.csv", row.names = F)
#### Rdata 확장자로 저장하는 방법
save(m2,file="m2.RData")
load("m2.Rdata")









