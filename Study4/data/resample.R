library(lme4)
library(dplyr)
library(arm)

# Define the dataframe df_new here (not shown)
df_new <- read.csv("data_rw_bysub_fixed.csv")

# Initialize list to store BIC differences
all_wins <- list()
all_wins2 <- list()

# Outer loop to iterate over 100 replicates

pvals_m1 <- list()
pvals_m2 <- list()
pvals_m3 <- list()

  
  
for (i in 1:1000){
    
    # Sample 100 sub_ids with replacement
    sub_ids_selected <- sample(unique(df_new$sub_id), 1000, replace = TRUE)


    
    # Initialize empty dataframe to store selected data
    df_selected <- data.frame()
    
    counter<-1
    # Inner loop to iterate over each sampled subject
    
    for (k in sub_ids_selected) {
      # Get data for current subject and assign unique sub_id_new
      sub_data <- df_new %>%
        filter(sub_id == k) %>%
        mutate(sub_id_to_use = rep(counter, each = 14))
      counter<-counter+1
      
      # Append sub_data to df_selected
      df_selected <- bind_rows(df_selected, sub_data)
      
    }

        
    
    # Fit hierarchical regressions and extract BICs
    results_lmm <- glmer(q ~e +s_log+(1|sub_id_to_use)+(1|trial),
                         family = binomial, data = df_selected,
                         control = glmerControl(optimizer = "bobyqa"))
    
    res_obj<-summary(results_lmm)
    pval<-(res_obj$coefficients[11])/2.0

    results_lmm2 <- glmer(q ~ e+m_log+(1|sub_id_to_use)+(1|trial),
                          family = binomial, data = df_selected,
                          control = glmerControl(optimizer = "bobyqa"))
    
    
    res_obj2<-summary(results_lmm2)
    pval2<-(res_obj2$coefficients[11])/2.0
    
    results_lmm3 <- glmer(q ~ e+(1|sub_id_to_use)+(1|trial),
                          family = binomial, data = df_selected,
                          control = glmerControl(optimizer = "bobyqa"))
    
    
    res_obj3<-summary(results_lmm3)
    pval3<-(res_obj3$coefficients[8])/2.0

    

    
    
    # Append BIC difference to list
    pvals_m1[[i]] <- pval
    pvals_m2[[i]] <- pval2
    pvals_m3[[i]] <- pval3
  }
  
  
  
  # Count number of BIC differences above 0
  n_above_0 <- sum(unlist(pvals_m1) < 0.05)
  n_above_0_2 <- sum(unlist(pvals_m2) < 0.05)
  n_above_0_3 <- sum(unlist(pvals_m3) < 0.05)
  


  # Print result
  cat(sprintf("percent sig p-val model 1: %f", n_above_0/300.0))
  cat(sprintf("percent sig p-val model 2: %f", n_above_0_2/300.0))
  cat(sprintf("percent sig p-val model 3: %f", n_above_0_3/300.0))
  

 

