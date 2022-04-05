
library(bcp)

#change directory
dirHome = "G:/report/year-3/07-Fall-2020/#3Paper/data/changePointTimeSeries/additionalTest/iqr"
setwd(dirHome)

tgList = list.files(getwd())

#loop through each tide gauge
for(tg in 1: length(tgList)){
    setwd(dirHome)
    
    print(tgList[tg])
    x <- read.csv(tgList[tg])

    #run the bcp command
    #first remove nans
    # change value/rmse/corr  
    # change indexing depending on dataframe/csv
    x = x[!is.na(x$value),1:3]

    mBcp <- bcp(x$value)

    #concatenate results
    res <- cbind(x$year, mBcp$posterior.mean, mBcp$posterior.prob)
    colnames(res) <- c('year', 'mean', 'prob');

    #change directory
    setwd("G:/report/year-3/07-Fall-2020/#3Paper/data/changePointTimeSeries/additionalTest/iqrBCP")

    #save as csv
    write.csv(res, tgList[tg])
}









