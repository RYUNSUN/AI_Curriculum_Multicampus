library(dplyr)
library(stringr)
library(ggplot2)
#1. 캐글 타이타닉 데이터 중, train.csv파일에 있는 Name 컬럼에서 호칭을 추출한 후,
#범주형으로 치환하시오.(가장 많이 등장한 상위 5개의 호칭만 치환할 것)
#예시)
#Braund, Mr. Owen Harris => Mr. => '1'
#Cumings, Mrs. John Bradley (Florence Briggs Thayer) => Mrs. => '2'
str(titanic$Name)
titanic$Title<-str_extract_all(titanic$Name,"[[:alpha:]]{2,}\\.",simplify = T)

temp<-as.data.frame(table(str_extract_all(titanic$Name,"[[:alpha:]]{2,}\\.",simplify = T)))
titanic_title<-arrange(temp,desc(temp$Freq)) %>% 
  head(5)
titanic_title$Var1<-factor(c(1:5))

#titanic$Title<-ifelse(titanic$Title=="Mr.",1,
#         ifelse(titanic$Title=="Miss.",2,
#                ifelse(titanic$Title=="Mrs.",3,
#                       ifelse(titanic$Title=="Master",4,
#                              ifelse(titanic$Title=="Dr.",5,NA)))))


#2. 1번 문제에서 각 호칭별 빈도수를 조사하고, 시각화 하시오.
ggplot(titanic_title,aes(reorder(Var1,-Freq),y=Freq))+
  geom_col()+
  xlab("호칭별")+
  ylab("빈도수")+
  ggtitle("호칭별 빈도수")


#3. 뉴욕타임즈 신문에 실린 기사중 일부를 발췌한 후, 텍스트 처리하시오
#(숫자 제거, 대문자 시작단어 추출 등 수업에서 다뤄진 기능 위주로 연습할 것)
newyork<-"BRUSSELS ??? Populists and nationalists who want to chip away at the European Union’s powers increased their share in Europe’s Parliament after four days of continent-wide elections, but it was not the deluge that many traditionalists had feared. When the vote counting is done, the populists are expected to get around 25 percent of the 751 seats, up from 20 percent five years ago, figures released by the European Union showed on Sunday."

newyork<-str_replace_all(newyork,"[[:space:]]???[[:space:]]"," ")
newyork<-str_replace_all(newyork,"-"," ")
newyork<-str_replace_all(newyork,"\\’","")
newyork<-str_replace_all(newyork,"\\,","")
newyork<-str_replace_all(newyork,"\\.","")

#수치로된 자료를 추출
str_extract_all(newyork,"[[:digit:]]{0,}")
table(unlist(str_extract_all(newyork,"[[:digit:]]{0,}")))
#대문자로 시작하는 단어 추출
str_extract_all(newyork,"[[:upper:]]{1,}[[:alpha:]]{1,}")
table(unlist(str_extract_all(newyork,"[[:upper:]]{1,}[[:alpha:]]{1,}")))
