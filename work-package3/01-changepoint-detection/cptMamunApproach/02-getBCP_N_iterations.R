#this script computes the bayesian changepoint probability 
#for N number of STD time series for all tide gauges

library(bcp)

home = "G:/report/year-3/07-Fall-2020/#3Paper/data/changePointTimeSeries/mamun-cpt-approach/era20c/0001-predCPT/wnd_v/01-randomizedSTD"
out = "G:/report/year-3/07-Fall-2020/#3Paper/data/changePointTimeSeries/mamun-cpt-approach/era20c/0001-predCPT/wnd_v/02-randomizedBCP"

setwd(home)
tgList = list.files(getwd())

#loop through each tide gauge
for(tg in 1: length(tgList)){
  
  curDir = paste(home, tgList[tg], sep = '/')
  setwd(curDir)
  
  print(tgList[tg]);

  itrList = list.files(getwd())

  #loop through each std time series
  for (itr in itrList){
    
    print(itr);
    
    
    setwd(curDir)
    x <- read.csv(itr);

    #change value/correlation/rmse 
    mBcp <- bcp(x$value);

    #concatenate results
    res <- cbind(x$year, mBcp$posterior.mean, mBcp$posterior.prob);
    colnames(res) <- c('year', 'mean', 'prob');
    
    #save as csv
    setwd(out);
    #create tg directory
    if (file.exists(tgList[tg])){
      setwd(paste(getwd(), tgList[tg], sep = '/'))
      write.csv(res, itr);
    }  else {
      dir.create(tgList[tg])
      setwd(paste(getwd(), tgList[tg], sep = '/'))
      write.csv(res, itr);
    }
  }
}
