
library(quantreg)


#read de-seasoned data
home = "G:/report/year-3/07-Fall-2020/#3Paper/data/changePointTimeSeries/mamun-cpt-approach/era20c/09-deSeasoned"

setwd(home)

tgList = list.files(getwd())

for(tg in tgList){
  setwd(home)
  
  print(tg);
  
  x <- read.csv(tg);
  
  lon = x$lon[1];
  lat = x$lat[1]
  
  dat = cbind(as.numeric(x$date), x$sasnAdjusted_mm)
  
  #print(dat)
  
  quants <- c(0.90, 0.95, 0.99, 0.999)
  #quants <- c(0.05, 0.25, 0.5, 0.75, 0.90, 0.95, 0.99, 0.999)
  #quants <- c(seq(0.01, 0.99, by = 0.01))
  #print(quants)
  
  res <- data.frame()
  
  for(q in 1:length(quants)) {
    print(quants[q])
    qr <- rq(dat[,2]~dat[,1], tau = quants[q])
    #print(summary(qr))
    
    res[q,1] = quants[q]
    res[q,2] = as.table(summary(qr)$coefficients)[2,][1]
    res[q,3] = as.table(summary(qr)$coefficients)[2,][2]
    res[q,4] = as.table(summary(qr)$coefficients)[2,][4]
    res[q,5] = lon;
    res[q,6] = lat;
    
    colnames(res) <- c('tau', 'value', 'stdError', 'pval', 'lon', 'lat')
    
    setwd("G:/report/year-3/07-Fall-2020/#3Paper/data/changePointTimeSeries/mamun-cpt-approach/era20c/10-quntReg")
    write.csv(res, tg);
  }
}

