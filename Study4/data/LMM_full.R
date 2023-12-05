library(lme4)
library(dplyr)
library(arm)
library(lmerTest)
# Define the dataframe df_new here (not shown)
df_new <- read.csv("data_rw_bysub_fixed_full.csv")




# Fit hierarchical regressions and extract BICs
results_lmm <- glmer(Choice~Divergence+AvgSuccProblog+(Divergence+AvgSuccProblog|sub_id)+(1|trial),family="binomial",
                     data = df_new)

res_obj<-coef(summary(results_lmm))
res_obj    
summary(results_lmm)

results_lmm2 <- glmer(Choice~Divergence+AvgPredProblog+(Divergence+AvgPredProblog|sub_id)+(1|trial),family="binomial",
                      data = df_new)

res_obj2<-coef(summary(results_lmm2))
res_obj2    
summary(results_lmm2)