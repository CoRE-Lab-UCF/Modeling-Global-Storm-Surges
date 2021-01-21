import numpy as np
import warnings
import os
import statsmodels.formula.api as smf
import pandas as pd
import functools
import re
warnings.filterwarnings('ignore')


class stepwise:

    def __init__(self,step,fit_intercept):
        self.step = step
        self.fit_intercept = fit_intercept

    def reduce_concat(self,x, sep=""):
        return functools.reduce(lambda x, y: str(x) + sep + str(y), x)

    def fit(self,data,null_formula,full_formula,response):

        """Linear model designed by forward selection.
        Parameters:
        -----------
        data : pandas DataFrame with all possible predictors and response
        response: string, name of response column in data
        Returns:
        --------
        model: an "optimal" fitted statsmodels linear model
               with an intercept
               selected by forward selection
               evaluated by aic
        """

        null_temp        = re.split('~',null_formula)
        null_predic_com  = null_temp[1].split('+')
        null_predic      = null_predic_com[1:len(null_predic_com)]
        full_temp        = re.split('~',full_formula)
        full_predic_com  = full_temp[1].split('+')
        full_predic      = full_predic_com[1:len(full_predic_com)]
        indices          = [i for i,id in enumerate(full_predic) if id not in null_predic]
        domain           = [full_predic[i] for i in indices]
        start            = set(null_predic)
        remaining        = set(domain)
        selected         = null_predic
        current_score, best_new_score = float('inf'), float('inf')
        score_selected   = []
        variable_added   = []
        
        while (remaining and current_score == best_new_score and self.step >0):
            scores_with_candidates = []
            for candidate in remaining:
                formula = "{} ~ {}".format(response,' + '.join(selected + [candidate]))
                if self.fit_intercept == 0:
                    formula = formula + "-1"
                score = smf.ols(formula, data).fit().aic
                scores_with_candidates.append((score, candidate))
            scores_with_candidates.sort()
            best_new_score, best_candidate = scores_with_candidates.pop(0)
            if current_score > best_new_score:
                remaining.remove(best_candidate)
                selected.append(best_candidate)
                score_selected.append(best_new_score)
                variable_added.append(best_candidate)
                current_score = best_new_score
            self.step=self.step-1
        formula = "{} ~ {}".format(response,' + '.join(selected))
        if self.fit_intercept == 0:
            formula = formula + "-1"
        model = smf.ols(formula, data).fit()
        return model

