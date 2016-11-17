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

df <- read.csv("house-votes-84.data", header = FALSE)
names(df)[1] ="party"
names(df)[2] = "handicapped-infants"
names(df)[3] = "water-project"
names(df)[4] = "budget"
names(df)[5] =  "physician-fee-freeze"
names(df)[6] =  "el-salvador aid"
names(df)[7] =  "religion in schools"
names(df)[8] =  "anti-satellite"
names(df)[9] = "nicaraguan aid"
names(df)[10] = "missile"
names(df)[11] = "immigration"
names(df)[12] = "synfuel cutback"
names(df)[13] = "education spending"
names(df)[14] = "superfund right to sue"
names(df)[15] = "crime"
names(df)[16] = "duty free exports"
names(df)[17] = "south africa"



treePrint <- rpart(party~.,data = df, method = "class", control=rpart.control(minsplit=1, cp=0))
treePrint
printcp(treePrint)
plot(treePrint, uniform=TRUE,main="Congress Regression Tree")
text(treePrint, use.n=TRUE, all=TRUE, cex=.7)
