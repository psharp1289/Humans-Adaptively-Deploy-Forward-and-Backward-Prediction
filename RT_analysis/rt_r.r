library(lme4)
library(dplyr)
library(arm)
library(lmerTest)
# Define the dataframe df_new here (not shown)
df_new <- read.csv("rt_df_for_r.csv")




# Fit hierarchical regressions and extract BICs
results_lmm <- lmer(log_rt_planning ~ PR_individual_answers+trial_num+(1+PR_individual_answers|sub)+(1+PR_individual_answers|experiment),
                          ,data = df_new)
    
    res_obj<-coef(summary(results_lmm))
		res_obj    
		summary(results_lmm)
		BIC(results_lmm)

