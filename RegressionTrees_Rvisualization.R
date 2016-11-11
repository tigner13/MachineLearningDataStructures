rTrees <- read.delim("rdata.txt", header = F)
rTrees$V1 <- gsub(pattern = " ", replacement = "", rTrees$V1,fixed = TRUE)

rTrees <- data.frame(do.call('rbind', strsplit(as.character(rTrees$V1),',',fixed = T)))

rTrees$X1 <- as.numeric(as.character(rTrees$X1))
rTrees$X2 <- as.numeric(as.character(rTrees$X2))

plot((rTrees$X1),(rTrees$X2), type = "p", main = "Regression Tree Prediction Accuracy", 
     xlab = "Ammount of Training data", ylab="Accuracy Percentage")




# install packages
library(rpart)
install.packages("rpart.plot")
library(rpart.plot)

# learn CART tree with default parameters
dTree <- rpart(Class ~ SepalLength + SepalWidth + PetalLength + PetalWidth + SepalArea + PetalArea + pcaF, method="class", data=d3)
summary(dTree)
               
# display learned tree
prp(dTree)
prp(dTree,type=4, extra=1)
               
# explore settings
dTree2 <- rpart(Class ~ SepalLength + SepalWidth + PetalLength + PetalWidth + SepalArea + PetalArea + pcaF, method="class", data=d3, (parms=list(split="information"))

dTree3 <- rpart(Class ~ SepalLength + SepalWidth + PetalLength + PetalWidth + SepalArea + PetalArea + pcaF, method="class", data=d3, control=rpart.control(minsplit=5))