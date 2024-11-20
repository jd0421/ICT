# r plot 
# 대표적으로 ggplot 을 사용, 구글의 프로덕트


# case1
? rnorm

rnorm(100)
plot(rnorm(100))
hist(rnorm(100))


# case2
data <- cbind(rnorm(100), rnorm(100), rnorm(100))
data
cor(data)

? cor
plot(data.frame(data))
plot(data[, 3])
ts.plot(data[, 3])
ts.plot(data)
ts.plot(data, col = c('red', 'blue', 'green'))

# case3 / lm / 리니어 모델
# 회귀분석

data2 <- data.frame(data)
head(data2)

fit <- lm(X3 ~ ., data = data2)
sum((fit$residuals) ^ 2) # sum of squares error / SSE


