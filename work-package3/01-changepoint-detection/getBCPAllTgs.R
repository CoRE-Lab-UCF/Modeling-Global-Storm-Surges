#get all tgs
home = "D:/OneDrive - Knights - University of Central Florida/UCF/Projekt.28/Report/07-Fall-2020/#3Paper/data/changePointTimeSeries/era20cSTD"
out = "D:/OneDrive - Knights - University of Central Florida/UCF/Projekt.28/Report/07-Fall-2020/#3Paper/data/changePointTimeSeries/era20cBCP"

setwd(home)
tgList = list.files(getwd())


for(tg in tgList){
  setwd(home)
  
  print(tg);
  x <- read.csv(tg);
  
  mBcp <- bcp(x$value);
  
  #concatenate results
  res <- cbind(x$year, mBcp$posterior.mean, mBcp$posterior.prob);
  colnames(res) <- c('year', 'mean', 'prob');
  
  #save as csv
  setwd(out);
  write.csv(res, tg);
}