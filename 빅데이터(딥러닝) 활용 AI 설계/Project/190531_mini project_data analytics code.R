library(tm)
library(KoNLP)
library(stringr)
library(stringr)
library(SnowballC)
library(dplyr)

load("C:/rwork/newyork times/northKorea_18_04.Rdata")
head(northKorea2018.04$body)

#####뉴욕타임즈 기사 전처리######
NA19_4<-as.character(northKorea2018.04$body)

uppers <- table(unlist(lapply(NA19_4, function(x) (str_extract_all(x, "\\b[[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}\\b")))))
uppers <- table(unlist(lapply(NA19_4, function(x) (str_extract_all(x, "\\b[[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}[[:punct:]][[:lower:]]{1}[[:alpha:]]{0,}\\b")))))
uppers <- table(unlist(lapply(NA19_4, function(x) (str_extract_all(x, "\\b[[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}\\b")))))
uppers <- table(unlist(lapply(NA19_4, function(x) (str_extract_all(x, "\\b[[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:upper:]]{1}[[:alpha:]]{0,}\\b")))))
uppers <- table(unlist(lapply(NA19_4, function(x) (str_extract_all(x, "\\b[[:upper:]]{1}[[:alpha:]]{0,}[[:space:]][[:alpha:]]{0,}\\b")))))
head(sort(uppers,decreasing = T),10)

NA19_4<-str_replace_all(NA19_4,"The New York Times","The_New_York_Times")
NA19_4<-str_replace_all(NA19_4,"United States","United_States")
NA19_4<-str_replace_all(NA19_4,"North Korea","North_Korea")
NA19_4<-str_replace_all(NA19_4,"South Korea","South_Korea")
NA19_4<-str_replace_all(NA19_4,"President Trump","President_Trump")
NA19_4<-str_replace_all(NA19_4,"North Korean","North_Korean")
NA19_4<-str_replace_all(NA19_4,"South Korean","South_Korean")
NA19_4<-str_replace_all(NA19_4,"Kim Jong","Kim_Jong")
NA19_4<-str_replace_all(NA19_4,"White House","White_House")
NA19_4<-str_replace_all(NA19_4,"President Xi Jinping","President_Xi_Jinping")
NA19_4<-str_replace_all(NA19_4,"President Barack Obama","President_Barack_Obama")
NA19_4<-str_replace_all(NA19_4,"President Emmanuel Macron","President_Emmanuel_Macron")

myarticle<-VCorpus(VectorSource(NA19_4))


#수치표현 삭제
articleCorpus<-tm_map(myarticle,removeNumbers)

#특수 문자 및 불용어 삭제
mytempfunct<-function(myobject,oldexp,newexp){
  tm_map(myobject,content_transformer(function(x,pattern)gsub(pattern,newexp,x)),oldexp)
  }
articleCorpus<-mytempfunct(articleCorpus,"#","")
articleCorpus<-mytempfunct(articleCorpus,"-","")
articleCorpus<-mytempfunct(articleCorpus,"--","")
articleCorpus<-mytempfunct(articleCorpus,"__________","")
articleCorpus<-mytempfunct(articleCorpus,"___","")
articleCorpus<-mytempfunct(articleCorpus,"__","")
articleCorpus<-mytempfunct(articleCorpus,"____","")
articleCorpus<-mytempfunct(articleCorpus,"_____","")
articleCorpus<-mytempfunct(articleCorpus,"__________ ","")
articleCorpus<-mytempfunct(articleCorpus,"___________________","")
articleCorpus<-mytempfunct(articleCorpus,"\\(","")
articleCorpus<-mytempfunct(articleCorpus,"\\)","")
articleCorpus<-mytempfunct(articleCorpus,"\\<","")
articleCorpus<-mytempfunct(articleCorpus,"\\>","")
articleCorpus<-mytempfunct(articleCorpus,"·","")
articleCorpus<-mytempfunct(articleCorpus,"‘","")
articleCorpus<-mytempfunct(articleCorpus,"’","")
articleCorpus<-mytempfunct(articleCorpus,"\\?","")
articleCorpus<-mytempfunct(articleCorpus,"\\.","")
articleCorpus<-mytempfunct(articleCorpus,",","")
articleCorpus<-mytempfunct(articleCorpus,"-","")
articleCorpus<-mytempfunct(articleCorpus,"\\]","")
articleCorpus<-mytempfunct(articleCorpus,"\\[","")
articleCorpus<-mytempfunct(articleCorpus,"@","")
articleCorpus<-mytempfunct(articleCorpus,"//","")
articleCorpus<-mytempfunct(articleCorpus,"\\$","")
articleCorpus<-mytempfunct(articleCorpus,"\\&","")
articleCorpus<-mytempfunct(articleCorpus,"???","")
articleCorpus<-mytempfunct(articleCorpus,"”","")
articleCorpus<-mytempfunct(articleCorpus,"???","")
articleCorpus<-mytempfunct(articleCorpus,"“","")
articleCorpus<-mytempfunct(articleCorpus,"???","")
articleCorpus<-mytempfunct(articleCorpus,"(-)[[:space:]]","")
articleCorpus<-tm_map(articleCorpus,stripWhitespace)
articleCorpus<-tm_map(articleCorpus,removeNumbers) 
articleCorpus<-tm_map(articleCorpus,content_transformer(tolower))
articleCorpus<-tm_map(articleCorpus,removeWords,words=stopwords("SMART")) #불용어 사전
articleCorpus<-tm_map(articleCorpus,removeWords,words="mr")
# articleCorpus<-tm_map(articleCorpus,removeWords,words="trumps") #"trump"는 긍정 단어이므로, 필요시 삭제
# articleCorpus<-tm_map(articleCorpus,removeWords,words="trump")



#TF-IDF
#전체 문서에서 해당 단어가 몇번 등장 했는지 알아보는 명령어 
dtm.e<-DocumentTermMatrix(articleCorpus)
dtm.e
inspect(dtm.e)
dtmlist<-apply(dtm.e[,],2,sum) #tdm:행(단어)열(문서) 표 
word.freq<-head(sort(dtmlist,decreasing = T),30)

word.freq.df <- data.frame(attr(word.freq, "names"), unname(word.freq))
colnames(word.freq.df)<-c("Var1","Freq")


#단어 분리 및 상위 20개 단어 추출
wordcount<-table(unlist(lapply(articleCorpus,function(x)str_extract_all(x,boundary("word")))))
wordcount_df<-as.data.frame(wordcount,stringsAsFactors = F)
dfword<-filter(wordcount_df,nchar(Var1)>=3)

top20<-dfword %>%
  arrange(desc(Freq)) %>%
  head(20)


#막대그래프 
library(ggplot2)
order<-arrange(top20,Freq)$Var1 #freq를 기준으로 오름차순한 word 출력
ggplot(data=top20,aes(x=Var1,y=Freq))+
  ylim(0,1300)+
  geom_col(color='red', fill='white')+
  geom_text(aes(label=Freq),hjust=-0.8)+ #수치 추가(geom_text 도움말 참고하기)
  coord_flip()+
  scale_x_discrete(limit=order)+
  ylab("빈도수")+
  xlab("단어")+
  ggtitle("단어별 빈도수")+
  theme(text = element_text(size=15))

#word cloud
library(wordcloud)
pal<-brewer.pal(8,"Spectral") #Paired, Dark2, Spectral
wordcloud(words=dfword$Var1,freq=dfword$Freq,colors=pal,
          min.freq=10,
          max.words=100,
          scale=c(5,0.5),
          random.order=F)


#bi-gram 
library(RWeka)
bigramTokenizer<-function(x){
  NGramTokenizer(x,Weka_control(min=2,max=2))
}
ngram.tdm<-TermDocumentMatrix(articleCorpus,control = list(tokenize=bigramTokenizer))
ngram.tdm$dimnames$Terms


#전체 문서에서 해당 단어가 몇번 등장 했는지 알아보는 명령어 
bigramlist<-apply(ngram.tdm[,],1,sum)  
class(bigramlist)
bigramGraph<-head(sort(bigramlist,decreasing = T),20)

bigram.word <- data.frame(attr(bigramGraph, "names"), unname(bigramGraph))
colnames(bigram.word)<-c("word","freq")

#bi-gram 빈도수 막대그래프 
order<-arrange(bigram.word,freq)$word
ggplot(data=bigram.word,aes(x=word,y=freq))+
  geom_col(color='blue', fill='white')+
  geom_text(aes(label=freq),hjust=-0.8)+ #수치 추가(geom_text 도움말 참고하기)
  coord_flip()+
  ylim(0,200)+
  scale_x_discrete(limit=order)+
  ylab("빈도수")+
  xlab("단어")+
  ggtitle("단어별 빈도수")+
  theme(text = element_text(size=15)) #그래프 내에 글씨 크기 조정


#######감성분석
library(tidyr) 
library(tidytext)

load("C:/rwork/newyork times/northKorea_18_04.Rdata")
NA19_4<-as.character(northKorea2018.04$body)
#"trump" 긍정 단어이므로 삭제.
NA19_4<-str_replace_all(NA19_4,"Trumps","")
NA19_4<-str_replace_all(NA19_4,"Trump","")
NA19_4<-str_replace_all(NA19_4,"trump","")
NA19_4<-str_replace_all(NA19_4,"trumps","")

NAarticle<-c(rep(NA,length(NA19_4)))
for(i in 1:length(NA19_4)){
  NAarticle[i]<-as.character(mypaper[[i]][1])
}

my.article.text<-data_frame(article.id=1:length(NA19_4),doc=NAarticle)
my.article.text

my.article.text.word<-my.article.text %>% 
  unnest_tokens(word,doc) 

my.article.text.word

#감정분석 사전과 join
#bing 사전
get_sentiments("bing")
myresult.sa<-my.article.text.word%>% 
  inner_join(get_sentiments("bing")) %>%
  count(word,article.id,sentiment) %>% #n:단어 등장 횟수 
  spread(sentiment,n,fill=0)

myagg<-myresult.sa %>% group_by(article.id) %>% 
            summarise(pos.sum=sum(positive),
            neg.sum=sum(negative),
            pos.sent=pos.sum-neg.sum,
            tot=pos.sum+neg.sum) %>% 
            mutate(group=ifelse(pos.sent>=0,"positive","negative")) %>% 
            mutate(ratio=round(neg.sum/tot*100,1))

#전체 부정문 비중도
neg.ratio=round(sum(myagg$neg.sum)/sum(myagg$tot)*100,1) #48.5

#한 달간의 긍정/부정 검사결과
sum(myagg$pos.sent)

#한 달동안의 기사 긍정/부정 검사 시각화
ggplot(myagg,aes(article.id,pos.sent,fill=group))+
  geom_col(position="dodge")+
  xlab("article number")+
  ylab("posistive/negative")+
  ggtitle("한 달간의 기사 긍정/부정")+
  theme(text = element_text(size=15)) #그래프 내에 글씨 크기 조정

#각 기사의 부정문 비중도
ggplot(myagg,aes(article.id,ratio,fill=ratio))+
  geom_col()+
  geom_hline(yintercept=50, colour="darkgrey", lty="dashed", size=2)+
  theme(text = element_text(size=15))

#nrc 사전(anger,anticipation,disgust, fear, joy, negative, positive, sadness, surprise, trust)
get_sentiments("nrc")
myresult.nrc<-my.article.text.word%>% 
  inner_join(get_sentiments("nrc")) %>% #230개의 단어로 구성
  count(word,article.id,sentiment) %>% #n:단어 등장 횟수 
  spread(sentiment,n,fill=0)

mynrc<-myresult.nrc %>% group_by(article.id) %>% 
            summarise(anger=sum(anger),
            anticipation=sum(anticipation),
            disgust=sum(disgust),
            fear=sum(fear),
            joy=sum(joy),
            negative=sum(negative),
            positive=sum(positive),
            sadness=sum(sadness),
            surprise=sum(surprise),
            trust=sum(trust))

#nrc 감정에 따른 빈도수 
mynrc.sum<-colSums(mynrc[,2:11])
str(mynrc.sum)
nrcvalue<-data.frame(attr(a, "names"), unname(a))
colnames(nrcvalue)<-c("sentiment","freq")

ggplot(data=nrcvalue,aes(x=sentiment,y=freq,fill=sentiment))+
  geom_col()+
  scale_fill_brewer(palette = "Spectral")+
  guides(fill=F)+
  coord_flip()+
  ylab("빈도수")+
  xlab("감정")+
  ggtitle("18년 4월 NRC 감정 분석 막대그래프 ")+
  theme(text = element_text(size=15)) #그래프 내에 글씨 크기 조정
