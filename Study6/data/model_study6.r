library(lme4)
library(dplyr)
library(arm)
library(lmerTest)
library(dplyr)
library(brms)
library(ggplot2)
# Define the dataframe df_new here (not shown)
df_model <- read.csv("model_fitting_EV_allsubs.csv")
# Calculate the length of the data frame (number of rows)
num_trials <- nrow(df_model)

# Calculate the log likelihood of guessing
# log(0.5) * number of trials
LL_null <- log(0.5) * num_trials

dict_BICs <- list()

# Fit hierarchical regressions and extract BICs
prior <- c(prior_string("uniform(0.01,10)", lb=0),
           prior_(~cauchy(0,1), class = ~sd))
model_formula <- bf(choice ~ 0+PR_EV+(0+PR_EV|sub), family = bernoulli())
model <- brm(model_formula, chains = 2, iter = 2000, 
             control = list(adapt_delta = 0.99), data = df_model,
             prior = prior, save_pars = save_pars(all = TRUE))
bridge_sampler_obj <- bridge_sampler(model)
bridge_sampler_obj<-as.numeric(bridge_sampler_obj[1])
print(bridge_sampler_obj)
dict_BICs['PR'] <- bridge_sampler_obj[1]-LL_null

model_formula <- bf(choice ~ 0+SR_EV+(0+SR_EV|sub), family = bernoulli())
model <- brm(model_formula, chains = 2, iter = 2000, 
             control = list(adapt_delta = 0.99), data = df_model,
             prior = prior, save_pars = save_pars(all = TRUE))
bridge_sampler_obj <- bridge_sampler(model)
bridge_sampler_obj<-as.numeric(bridge_sampler_obj[1])
print(bridge_sampler_obj)
dict_BICs['SR'] <- bridge_sampler_obj[1]-LL_null

model_formula <- bf(choice ~ 0+MB_EV+(0+MB_EV|sub), family = bernoulli())
model <- brm(model_formula, chains = 2, iter = 2000, 
             control = list(adapt_delta = 0.99), data = df_model,
             prior = prior, save_pars = save_pars(all = TRUE))
bridge_sampler_obj <- bridge_sampler(model)
bridge_sampler_obj<-as.numeric(bridge_sampler_obj[1])
print(bridge_sampler_obj)
dict_BICs['MB'] <- bridge_sampler_obj[1]-LL_null

model_formula <- bf(choice ~ 0+BR_EV+(0+BR_EV|sub), family = bernoulli())
model <- brm(model_formula, chains = 2, iter = 2000, 
             control = list(adapt_delta = 0.99), data = df_model,
             prior = prior, save_pars = save_pars(all = TRUE))
bridge_sampler_obj <- bridge_sampler(model)
bridge_sampler_obj<-as.numeric(bridge_sampler_obj[1])
print(bridge_sampler_obj)
dict_BICs['BR'] <- bridge_sampler_obj[1]-LL_null

# Convert the log marginal likelihoods to a data frame
log_marginal_likelihoods_df <- data.frame(
  Variable = names(dict_BICs),
  LogMarginalLikelihood = as.numeric(unlist(dict_BICs)),
  stringsAsFactors = FALSE
)

# Define the desired order of the models
model_order <- c( "BR","MB", "SR","PR")

# Match the model order to the Variable column
log_marginal_likelihoods_df$Variable <- factor(log_marginal_likelihoods_df$Variable, levels = model_order)

# Now plot the log marginal likelihoods with models sorted by the specified order
my_plot <- ggplot(log_marginal_likelihoods_df, aes(x = Variable, y = LogMarginalLikelihood)) +
  geom_bar(stat = "identity", fill = "black") +
  coord_flip() +
  theme_minimal() +
  labs(x = NULL, y = "Bayes Factor relative to Null", title = "Model Comparison") +
  theme(plot.title = element_text(hjust = 0.5, size = 40),
        plot.background = element_rect(fill = "white", colour = "white"),
        panel.background = element_blank(),
        panel.grid = element_blank(),
        axis.text = element_text(size = 30),
        axis.ticks = element_blank(),
        axis.title.x = element_text(size = 30))

# Save the plot to a file
ggsave("model_comparison.png", plot = my_plot, dpi = 300, width = 6, height = 6, units = "in")

# results_lmm <- glmer(choice ~ 0+PR_EV+(0+PR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# results_lmm2 <- glmer(choice ~ 0+SR_EV+(0+SR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# results_lmm3 <- glmer(choice ~ 0+MB_EV+(0+MB_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# results_lmm4 <- glmer(choice ~ 0+BR_EV+(0+BR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# 
# BIC(results_lmm)
# BIC(results_lmm2)
# BIC(results_lmm3)
# BIC(results_lmm4)



# results_lmm <- glmer(choice ~ 0+PR_EV+(0+PR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# results_lmm2 <- glmer(choice ~ 0+SR_EV+(0+SR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# results_lmm3 <- glmer(choice ~ 0+MB_EV+(0+MB_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# results_lmm4 <- glmer(choice ~ 0+BR_EV+(0+BR_EV|sub),family = binomial, control = glmerControl(optimizer = "bobyqa"),data = df_new)
# 
# BIC(results_lmm)
# BIC(results_lmm2)
# BIC(results_lmm3)
# BIC(results_lmm4)


