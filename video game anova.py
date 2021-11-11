# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

games = pd.read_csv('https://raw.githubusercontent.com/chelseatwan/dataset_anova/main/vgsales.csv')

# DV = NA_Sales


# IV Factor 1 = platform
# The null hypothesis (H0) is that there is no difference between video game platforms 
# and NA sales.
# The alternative hypothesis (H1) is sthat there is a difference between the platform and NA sales.
model1 = smf.ols("NA_Sales ~ C(Platform)", data = games).fit()
anova_table1 = sm.stats.anova_lm(model1, typ=2)
anova_table1
# P value is significant at 6.33e-177.
# Significant differences between video game consoles when it comes to NA sales.


# IV Factor 2 = Genre
# The null hypothesis (H0) is that there is no difference between video game genre
# and NA sales.
# The alternative hypothesis (H1) is sthat there is a difference between the genre and NA sales.
model2 = smf.ols("NA_Sales ~ C(Genre)", data = games).fit()
anova_table2 = sm.stats.anova_lm(model2, typ=2)
anova_table2
# P value is significant at 3.39e-47,
# Signifanct differences between video game genres when it comes to NA sales.


# IV Factor 3 = Publisher
# The null hypothesis (H0) is that there is no difference between the publisher and NA sales.
# The alternative hypothesis (H1) is sthat there is a difference between the the publisher and NA salels.
model3 = smf.ols("NA_Sales ~ C(Publisher)", data = games).fit()
anova_table3 = sm.stats.anova_lm(model3, typ=2)
anova_table3
# P value is significant at 1.20e-109,
# Signifanct differences between video game publishers when it comes to NA sales.
