library(dplyr)
library(brms)
library(ggplot2)

df3 <- read.csv('all_subs_Study1_actionvaluesrounded_PRvsGuessing.csv')
sub_idxs <- as.factor(df3$sub_num)

coords <- list(subj = unique(sub_idxs), obs_id = seq_along(sub_idxs))

dict_traces <- list()
dict_model <- list()
dict_BICs_prvg3 <- list()
sub_id <- unique(df3$sub_num)
len_questions <- 8
counter<-1
bad_cols <- c('choice', 'sub_num', 'Unnamed: 0', 'index_rows')
good_cols <- c('sr_many____ev','pr_many____ev','pr_one___norm_rwd','sr_one___norm_rwd')
name_cols <-c('SR','PR','PRG_Reward_Prob','SRG_Reward_Prob')
cols <- setdiff(colnames(df3), bad_cols)

for (col in good_cols) {
  if (grepl('rwd', col)) {
    name_col <- strsplit(col, '_rwd0')[[1]][1]
  } else if (grepl('prob', col)) {
    name_col <- strsplit(col, '_prob0')[[1]][1]
  } else {
    name_col <- col
  }
  
  print(paste('working on model :', name_col))
  
  probs_a0 <- as.matrix(df3[, grep(paste0(name_col, "_prob[0-3]_action0"), colnames(df3))])
  probs_a1 <- as.matrix(df3[, grep(paste0(name_col, "_prob[0-3]_action1"), colnames(df3))])
  rwds_a0 <- as.matrix(df3[, grep(paste0(name_col, "_rwd[0-3]_action0"), colnames(df3))])
  rwds_a1 <- as.matrix(df3[, grep(paste0(name_col, "_rwd[0-3]_action1"), colnames(df3))])
  
  all_rewards <- cbind(rwds_a0, rwds_a1)
  all_rewards_max <- apply(all_rewards, 1, max)
  
  r1 <- rwds_a0
  r2 <- rwds_a1
  p1 <- probs_a0
  p2 <- probs_a1
  
  length_data <- nrow(df3)
  
  
  p1_r1 <- matrix(p1 * r1, nrow = length_data)
  p2_r2 <- matrix(p2 * r2, nrow = length_data)
  
  df_a1_a2 <- data.frame(a1 = rowSums(p1_r1)-rowSums(p2_r2))
  
  df_a1_a2$a1_scaled <- scale(df_a1_a2$a1)
  
  df_model <- cbind(df3[c("choices", "sub_num")], df_a1_a2)
  
  
  model_formula <- bf(choices ~  0+a1_scaled + (0+a1_scaled | sub_num), family = bernoulli())
  
  prior <- c(prior_string("uniform(0.01,10)", lb=0),
              prior_(~cauchy(0,1), class = ~sd))
  if (col == "sr_many____ev") {
    dict_BICs_prvg3[[name_cols[counter]]] <- 748.6}
  else{
    model <- brm(model_formula, chains = 2, iter = 2000, 
               control = list(adapt_delta = 0.99), data = df_model,
               prior = prior, save_pars = save_pars(all = TRUE))
  


  # Call bridge_sampler with the compiled model
  bridge_sampler_obj <- bridge_sampler(model)
  bridge_sampler_obj<-as.numeric(bridge_sampler_obj[1])
  print(bridge_sampler_obj)
  dict_BICs_prvg3[[name_cols[counter]]] <- bridge_sampler_obj[1]+1247.66492501}
  counter<-counter+1

}

# Convert the log marginal likelihoods to a data frame
log_marginal_likelihoods_df <- data.frame(
  Variable = names(dict_BICs_prvg3),
  LogMarginalLikelihood = as.numeric(unlist(dict_BICs_prvg3)),
  stringsAsFactors = FALSE
)

# Plot the log marginal likelihoods
ggplot(log_marginal_likelihoods_df, aes(x = reorder(Variable, LogMarginalLikelihood), y = LogMarginalLikelihood)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  coord_flip() +
  theme_minimal() +
  labs(x = "Variable", y = "Change ln(likelihood) from Null", title = "Model Comparison") +
  theme(plot.title = element_text(hjust = 0.5))

                      