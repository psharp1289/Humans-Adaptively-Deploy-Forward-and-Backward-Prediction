
library(brms)
library(bayesplot)

df_new <- read.csv("all_rt_data.csv")

# Fit Bayesian hierarchical regression
results_brm <- brm(
  log_rt_planning ~ 1 + PR_individual_answers + trial_num + 
    (1 + PR_individual_answers | sub), 
  data = df_new,
  family = gaussian(),
  prior = c(
    set_prior("normal(0, 5)", class = "b"),
    set_prior("normal(0, 5)", class = "sd"),
    set_prior("lkj(2)", class = "cor")
  ),
  iter = 2000, 
  warmup = 1000, 
  chains = 4, 
  cores = 4, 
  control = list(adapt_delta = 0.95)
)

# Show results
summary(results_brm)

# Plot posterior distributions
mcmc_areas(as.array(results_brm), pars = "b_PR_individual_answers")

library(ggplot2)
library(dplyr)
library(tidyr)
library(bayestestR)

# Extract posterior samples
posterior_samples <- as.data.frame(as.array(results_brm))

# Combine traces for PR_individual_answers
pr_individual_answers_samples <- posterior_samples %>%
  select(ends_with("b_PR_individual_answers")) %>%
  pivot_longer(cols = ends_with("b_PR_individual_answers"), 
               names_to = "trace", 
               values_to = "value") %>%
  mutate(value = as.numeric(value))

# Calculate the 95% HDI
hdi_values <- hdi(pr_individual_answers_samples$value, ci = 0.95)
print(hdi_values$lower)
# Create the density plot for PR_individual_answers
p <- ggplot(pr_individual_answers_samples, aes(x = value)) +
  geom_density(fill = "blue", alpha = 0.5) +
  geom_vline(xintercept = 0, linetype = "solid", color = "black", size = 1.5) +  # Making the line a bit thicker for visibility
  labs(
    title = "Posterior Distribution of PR_individual_answers with 95% HDI",
    subtitle = "Bayesian Hierarchical Model using brms",
    x = "Effect Size",
    y = "Density"
  ) 
  theme_minimal()

# Show the plot
print(p)


