import pymc as pm
import numpy as np
import pandas as pd
from scipy.special import expit
df_new=pd.read_csv('data_rw_bysub_fixed_full.csv')

sub_idxs, subjs = pd.factorize(df_new.sub_id)
trial_idxs, trials = pd.factorize(df_new.trial)

coords = {
    "subj": subjs,
    "obs_id": np.arange(len(sub_idxs)),
    "trial": trials,
}

with pm.Model(coords=coords) as hierarchical_model2:
    sub_idxs = pm.Data("sub_idxs", sub_idxs, dims="obs_id")
    trial_idxs = pm.Data("trial_idxs", trial_idxs, dims="obs_id")

    log_pred = pm.Data("log_pred_data", df_new.m_log.values, dims="obs_id")
    diverginess = pm.Data("div_data", df_new.e.values, dims="obs_id")

    # Hyperpriors for hierarchical effects of subject and trial
    sigma_trial = pm.HalfNormal("var_trial", 10)
    sigma_subject = pm.HalfNormal("var_subj", 10)

    # Fixed effects for diverginess and log_pred_prob and general intercept
    diverginess_effect = pm.Normal("div", 0, 1)
    log_pred_effect = pm.Normal("pred", 0, 1)
    intercept = pm.Normal("Intercept", 0, 1)

    # Subject-level effects of trial and subject
    trial_effect = pm.Normal("trial_effect", mu=0, sigma=sigma_trial, dims="trial")
    subj_effect = pm.Normal("subj_effect", mu=0, sigma=sigma_subject, dims="subj")

    # Reparameterize theta using a Beta distribution
    omega = pm.Deterministic(
        "mu",(intercept
        + (diverginess_effect * diverginess)
        + (log_pred_effect * log_pred)
        + subj_effect[sub_idxs]
        + trial_effect[trial_idxs]))

    theta = pm.Deterministic('logistic link', pm.math.invlogit(omega))

    # Data likelihood
    y = pm.Bernoulli("data", p=theta, observed=df_new.q.values, dims="obs_id")


with hierarchical_model2:
    trace_logistic_model2 = pm.sample(draws=1000, target_accept=0.99, tune=1000, cores=1)