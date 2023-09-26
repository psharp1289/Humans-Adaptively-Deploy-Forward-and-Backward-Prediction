library(lme4)
library(dplyr)
library(arm)
library(lmerTest)
# Define the dataframe df_new here (not shown)
df_new <- read.csv("model_fitting_EV_allsubs.csv")




# Fit hierarchical regressions and extract BICs
results_lmm <- glmer(choice ~ 0+PR_EV+(0+PR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
results_lmm2 <- glmer(choice ~ 0+SR_EV+(0+SR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
results_lmm3 <- glmer(choice ~ 0+MB_EV+(0+MB_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
results_lmm4 <- glmer(choice ~ 0+BR_EV+(0+BR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)

BIC(results_lmm)
BIC(results_lmm2)
BIC(results_lmm3)
BIC(results_lmm4)

