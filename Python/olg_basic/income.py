'''
------------------------------------------------------------------------
Last updated 7/1/2014

Functions for created the matrix of ability levels, e, and the 
probabilities, f, to be used in OLG_fastversion.py

This py-file calls the following other file(s):
            data/income_data.asc
------------------------------------------------------------------------
'''

'''
------------------------------------------------------------------------
    Packages
------------------------------------------------------------------------
'''

import numpy as np
import pandas as pd

'''
------------------------------------------------------------------------
    Read Data
------------------------------------------------------------------------
The data comes from **************
The data has the age and hourly wage for each observation
------------------------------------------------------------------------
'''

data = pd.read_table("data/income_data.asc", sep=',', header=0)
data = data.query("19 < PRTAGE < 80")
data['age'], data['wage'] = data['PRTAGE'], data['PTERNHLY']
del data['HRHHID'], data['OCCURNUM'], data['YYYYMM'], data[
    'HRHHID2'], data['PRTAGE'], data['PTERNHLY']

markov_dta = pd.read_csv("data/PSIDdata.csv", sep=',', header=0)
markov_dta['age_99'], markov_dta['wage_99'] = markov_dta[
    'ER33504'], markov_dta['ER33537O']
markov_dta['age_01'], markov_dta['wage_01'] = markov_dta[
    'ER33604'], markov_dta['ER33628O']
del markov_dta['ER33504'], markov_dta['ER33537O'], markov_dta[
    'ER33604'], markov_dta['ER33628O'], markov_dta['ER30001'], markov_dta[
    'ER30002'], markov_dta['ER33501'], markov_dta['ER33502'], markov_dta[
    'ER33503'], markov_dta['ER33601'], markov_dta['ER33602'], markov_dta[
    'ER33603'], 
markov_dta = markov_dta.query("19 < age_99 < 80")
markov_dta = markov_dta.query("19 < age_01 < 80")
markov_dta = markov_dta.query("wage_99 != -99")
markov_dta = markov_dta.query("wage_01 != -99")
markov_dta = markov_dta.query("wage_99 != 0")
markov_dta = markov_dta.query("wage_01 != 0")
markov_dta = markov_dta.query("wage_99 != 999")
markov_dta = markov_dta.query("wage_01 != 999")
markov_dta = markov_dta.reset_index()
# del markov_dta['index']


def get_e(S, J):
    '''
    Parameters: S - Number of age cohorts
                J - Number of ability levels by age

    Returns:    e - S x J matrix of J working ability levels for each 
                    age cohort measured by hourly wage, normalized so 
                    the mean is one
    '''
    age_groups = np.linspace(20, 80, S+1)
    e = np.zeros((S, J))
    for i in xrange(S):
        incomes = data.query('age_groups[i]<=age<age_groups[i+1]')
        inc = np.array(incomes['wage'])
        inc.sort()
        for j in xrange(J):
            e[i, j] = inc[len(inc)*(j+.5)/J]
    e /= e.mean()
    return e


def get_f_simple(S, J):
    '''
    Parameters: S - Number of age cohorts
                J - Number of ability levels by age

    Returns:    f - S x J matrix of probabilities for each ability level
                    by age group
    '''
    f = np.ones((S, J))*(1.0/J)
    return f


def get_f(S, J):
    f = np.zeros((J, J))
    sort99 = np.array(markov_dta['wage_99'])
    sort01 = np.array(markov_dta['wage_01'])
    sort99.sort()
    sort01.sort()
    percentiles99 = np.zeros(J-1)
    percentiles01 = np.zeros(J-1)
    for j in xrange(J-1):
        percentiles99[j] = sort99[len(sort99)*(j+1)/J]
        percentiles01[j] = sort01[len(sort01)*(j+1)/J]
    for ind99 in xrange(J):
        if ind99 == 0:
            num_in_99df = markov_dta.query('wage_99 <= percentiles99[ind99]')
            num_in_99 = np.array(num_in_99df.count()[0])
        elif ind99 < J-1:
            num_in_99df = markov_dta.query('percentiles99[ind99-1] < wage_99 <= percentiles99[ind99]')
            num_in_99 = np.array(num_in_99df.count()[0])
        else:
            num_in_99df = markov_dta.query('percentiles99[ind99-1] < wage_99')
            num_in_99 = np.array(num_in_99df.count()[0])
        for ind01 in xrange(J):
            if ind01 == 0:
                num_in_both = num_in_99df.query('wage_01 <= percentiles01[ind01]').count()
                num_in_both = np.array(num_in_both[0])
            elif ind01 < J-1:
                num_in_both = num_in_99df.query('percentiles01[ind01-1] < wage_01 <= percentiles01[ind01]').count()
                num_in_both = np.array(num_in_both[0])
            else:
                num_in_both = num_in_99df.query('percentiles01[ind01-1] < wage_01').count()
                num_in_both = np.array(num_in_both[0])
            f[ind99, ind01] = float(num_in_both) / num_in_99
    f = np.linalg.matrix_power(f, 60/S)
    f = np.tile(f.reshape(1, J, J), (S, J, J))
    return f
