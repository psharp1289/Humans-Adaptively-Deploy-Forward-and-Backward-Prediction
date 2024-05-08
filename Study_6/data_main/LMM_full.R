library(lme4)
library(dplyr)
library(arm)
library(lmerTest)
library(performance)

# Define the dataframe df_new here (not shown)
df_new <- read.csv("data_rw_bysub_fixed_full.csv")

# Fit hierarchical regression and extract BICs
results_lmm <- glmer(Choice~Divergence+AvgSuccProblog+(Divergence+AvgSuccProblog|sub_id)+(1|trial), family="binomial", data=df_new)
summary(results_lmm)

# Model diagnostics
print(AIC(results_lmm))
print(BIC(results_lmm))
print(logLik(results_lmm))
print(VarCorr(results_lmm))
plot(resid(results_lmm))

results_lmm2 <- glmer(Choice~Divergence+AvgPredProblog+(Divergence+AvgPredProblog|sub_id)+(1|trial), family="binomial", data=df_new)
summary(results_lmm2)

# Model diagnostics for second model
print(AIC(results_lmm2))
print(BIC(results_lmm2))
print(logLik(results_lmm2))
print(VarCorr(results_lmm2))
plot(resid(results_lmm2))
