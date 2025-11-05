# %% [markdown]
# # Autocorrelation Lab — ISQ Trajectory
#
# Goal: detect serial correlation and compare remedies (lags, GLS AR(1), HAC SEs).

# %% [markdown]
# ## 0. Setup & reshape

# %%
# TODO: load the same CSV as df

# %%
# TODO: reshape ISQ columns (isq_w0...isq_w8) from wide to long -> df_long with columns: implant_id, week, isq
# hint: pd.melt with id_vars=[...], value_vars=[...]

# %% [markdown]
# ## 1. Visual check

# %%
# TODO: pick a few implant_ids and plot ISQ vs week (plt.plot) to see dip/recovery

# %% [markdown]
# ## 2. Simple time-series regression

# %%
# TODO: merge baseline predictors (e.g., torque_ncm, bone_density) into df_long (by implant_id)

# %%
# TODO: fit OLS: isq ~ week + week^2 + torque_ncm (+ other controls)

# %%
# TODO: store residuals

# %% [markdown]
# ## 3. Autocorrelation diagnostics

# %%
# TODO: plot ACF of residuals (statsmodels.graphics.tsaplots.plot_acf)

# %%
# TODO: compute Durbin–Watson (sms.durbin_watson) and Ljung–Box (statsmodels.stats.diagnostic.acorr_ljungbox)

# %% [markdown]
# ## 4. Remedies and comparison

# %%
# TODO: add lagged isq (grouped by implant_id) -> isq_lag1; refit model and compare residual ACF

# %%
# TODO: fit GLS with AR(1) errors and compare summary to OLS
# hint: statsmodels.regression.linear_model.GLSAR or sm.tsa.statespace.SARIMAX

# %%
# TODO: compute HAC/Newey–West SEs on the OLS fit and compare standard errors
# hint: results.get_robustcov_results(cov_type='HAC', maxlags=1 or 2)

# %% [markdown]
# ## 5. Conclusions
#
# What changed across remedies? Which approach is most defensible clinically vs statistically?

# %%
# TODO: write markdown/print summary

