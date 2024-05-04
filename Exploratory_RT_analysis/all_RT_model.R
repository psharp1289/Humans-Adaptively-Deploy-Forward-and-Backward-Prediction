library(lme4)
library(dplyr)
library(arm)
library(lmerTest)

# Load the data from CSV
df_new <- read.csv("rt_all_normalized.csv")

# Standardize the pr_raw column and add it as PR
df_new$PR <- scale(df_new$pr_raw)

# Save the updated dataframe with standardized PR to a new CSV
write.csv(df_new, "RT_with_standardizedPR.csv", row.names = FALSE)

# Fit hierarchical regressions and extract BICs
results_lmm <- lmer(log_rt_planning ~ PR_individual_answers + trial_num + (PR_individual_answers + trial_num | sub) + (PR_individual_answers + trial_num | experiment), data = df_new)

# Extract and print the coefficients summary and BIC
res_obj <- coef(summary(results_lmm))
print(res_obj)
print(summary(results_lmm))
print(BIC(results_lmm))
