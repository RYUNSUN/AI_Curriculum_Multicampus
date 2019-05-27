exam<-read.csv("Data/csv_exam.csv")
exam
exam %>% 
  filter(math>=50 & english >=80) %>% 
  mutate(tot_avg=(math+english+science)/3) %>% 
  group_by(class) %>% 
  summarise(class_mean<-mean(tot_avg))

exam$tot<-(exam$math+exam$english+exam$science)/3
aggregate(data=exam,)