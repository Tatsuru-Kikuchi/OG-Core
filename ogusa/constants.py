import taxcalc


SHOW_RUNTIME = False  # Flag to display RuntimeWarings when run model

EPSILON = 1e-10
PATH_EXISTS_ERRNO = 17

REFORM_DIR = "OUTPUT_REFORM"
BASELINE_DIR = "OUTPUT_BASELINE"

# Default year for model runs
DEFAULT_START_YEAR = 2020

# Latest year TaxData extrapolates to
TC_LAST_YEAR = 2029

# Year of data used (e.g. PUF or CPS year)
CPS_START_YEAR = taxcalc.Records.CPSCSV_YEAR
PUF_START_YEAR = taxcalc.Records.PUFCSV_YEAR

VAR_LABELS = {'Y': 'GDP ($Y_t$)', 'C': 'Consumption ($C_t$)',
              'L': 'Labor ($L_t$)',
              'G': 'Government Expenditures ($G_t$)',
              'TR': 'Lump sum transfers ($TR_t$)',
              'B': 'Wealth ($B_t$)', 'I_total': 'Investment ($I_t$)',
              'K': 'Capital Stock ($K_t$)',
              'K_d': 'Domestically-owned Capital Stock ($K^d_t$)',
              'K_f': 'Foreign-owned Capital Stock ($K^f_t$)',
              'D': 'Government Debt ($D_t$)',
              'D_d': 'Domestically-owned Gov Debt ($D^d_t$)',
              'D_f': 'Foreign-owned Gov Debt ($D^f_t$)',
              'r': 'Real interest rate ($r_t$)',
              'r_gov': 'Real interest rate on gov debt ($r_{gov,t}$)',
              'r_hh': 'Real interest rate on HH portfolio ($r_{hh,t}$)',
              'w': 'Wage rate', 'BQ': 'Aggregate bequests ($BQ_{j,t}$)',
              'total_revenue': 'Total tax revenue ($REV_t$)',
              'business_revenue': 'Business tax revenue',
              'IITpayroll_revenue': 'IIT and payroll tax revenue',
              'n_mat': 'Labor Supply ($n_{j,s,t}$)',
              'c_path': 'Consumption ($c_{j,s,t}$)',
              'bmat_splus1': 'Savings ($b_{j,s+1,t+1}$)',
              'bq_path': 'Bequests ($bq_{j,s,t}$)',
              'bmat_s': 'Savings ($b_{j,s,t}$)',
              'y_before_tax_mat': 'Before tax income',
              'etr_path': 'Effective Tax Rate ($ETR_{j,s,t}$)',
              'mtrx_path':
              'Marginal Tax Rate, Labor Income ($MTRx_{j,s,t}$)',
              'mtry_path':
              'Marginal Tax Rate, Capital Income ($MTRy_{j,s,t}$)',
              'tax_path':
              'Total Taxes',
              'nssmat': 'Labor Supply ($\\bar{n}_{j,s}$)',
              'bssmat_s': 'Savings ($\\bar{b}_{j,s}$)',
              'bssmat_splus1': 'Savings ($\\bar{b}_{j,s+1}$)',
              'cssmat': 'Consumption ($\\bar{c}_{j,s}$)',
              'yss_before_tax_mat': 'Before-tax Income',
              'etr_ss': 'Effective Tax Rate ($\\bar{ETR}_{j,s}$)',
              'mtrx_ss':
              'Marginal Tax Rate, Labor Income ($\\bar{MTRx}_{j,s}$)',
              'mtry_ss':
              'Marginal Tax Rate, Capital Income ($\\bar{MTRy}_{j,s}$)',
              'ETR': 'Effective Tax Rates',
              'MTRx': 'Marginal Tax Rates on Labor Income',
              'MTRy': 'Marginal Tax Rates on Capital Income',
              'Yss': 'GDP ($\\bar{Y}$)',
              'Css': 'Consumption ($\\bar{C}$)',
              'Lss': 'Labor ($\\bar{L}$)',
              'Gss': 'Government Expenditures ($\\bar{G}$)',
              'TR_ss': 'Lump sum transfers, ($\\bar{TR}$)',
              'Bss': 'Wealth ($\\bar{B}$)',
              'Iss_total': 'Investment ($\\bar{I}$)',
              'Kss': 'Capital Stock ($\\bar{K}$)',
              'K_d_ss':
                  'Domestically-owned Capital Stock ($\\bar{K}^d$)',
              'K_f_ss': 'Foreign-owned Capital Stock ($\\bar{K}^f$)',
              'Dss': 'Government Debt ($\\bar{D}$)',
              'D_d_ss': 'Domestically-owned Gov Debt ($\\bar{D}^d$)',
              'D_f_ss': 'Foreign-owned Gov Debt ($\\bar{D}^f$)',
              'rss': 'Real interest rate ($\\bar{r}$)',
              'r_gov_ss':
                  'Real interest rate on gov debt ($\\bar{r}_{gov}$)',
              'r_hh_ss':
                  'Real interest rate on HH portfolio ($\\bar{r}_{hh}$)',
              'wss': 'Wage rate ($\\bar{w}$)',
              'BQss': 'Aggregate bequests ($\\bar{BQ}_{j}$)',
              'total_revenue_ss': 'Total tax revenue ($\\bar{REV}$)',
              'business_revenue': 'Business tax revenue',
              'IITpayroll_revenue': 'IIT and payroll tax revenue',
              'debt_service_ss':
                  'Debt service cost ($\\bar{r}_{gov}\\bar{D}$)',
              'D/Y': 'Debt to GDP ratio', 'T_Pss': 'Government Pensions'
              }

ToGDP_LABELS = {'D': 'Debt-to-GDP ($D_{t}/Y_t$)',
                'D_d': 'Domestically-owned Debt-to-GDP ($D^d_{t}/Y_t$)',
                'D_f': 'Foreign-owned Debt-to-GDP ($D^f_{t}/Y_t$)',
                'G': 'Govt Spending-to-GDP ($G_{t}/Y_t$)',
                'K': 'Capital-Output Ratio ($K_{t}/Y_t$)',
                'K_d':
                'Domestically-owned Capital-Output Ratio ($K^d_{t}/Y_t$)',
                'K_f':
                'Foreign-owned Capital-Output Ratio ($K^f_{t}/Y_t$)',
                'C': 'Consumption-Output Ratio ($C_{t}/Y_t$)',
                'I': 'Investment-Output Ratio ($I_{t}/Y_t$)',
                'total_revenue': 'Tax Revenue-to-GDP ($REV_{t}/Y_t$)'}

GROUP_LABELS = {0: '0-25%', 1: '25-50%', 2: '50-70%', 3: '70-80%',
                4: '80-90%', 5: '90-99%', 6: 'Top 1%'}

CBO_UNITS = {
    'Y': r'Billions of \$', 'r': 'Percent', 'w_growth': 'Percent',
    'L_growth': 'Percent', 'I_total': r'Billions of \$', 'L': '2012=100',
    'C': r'Billions of \$', 'T_P': r'Billions of \$',
    'G': r'Billions of \$', 'iit_revenue': r'Billions of \$',
    'payroll_tax_revenue': r'Billions of \$',
    'business_revenue': r'Billions of \$', 'wL': r'Billions of \$',
    'D': r'Billions of \$'}

PARAM_LABELS = {
    'start_year': ['Initial year', r'$\texttt{start_year}$'],
    # 'Gamma': ['Initial distribution of savings', r'\hat{\Gamma}_{0}'],
    # 'N': ['Initial population', 'N_{0}'],
    'omega': ['Population by age over time',
              r'${{\omega_{s,t}}}_{s=1}^{S}$'],
    # 'fert_rates': ['Fertility rates by age',
    #                r'\left{f_{s}\right}_{s=1}^{S}'],
    'imm_rates': ['Immigration rates by age',
                  r'${{i_{s}}}_{s=1}^{S}$'],
    'rho': ['Mortality rates by age',
            r'${{\rho_{s}}}_{s=1}^{S}$'],
    'e': ['Deterministic ability process',
          r'${{e_{j,s}}}_{j,s=1}^{J,S}$'],
    'lambdas': ['Lifetime income group percentages',
                r'${{\lambda_{j}}}_{j=1}^{J}$'],
    'J': ['Number of lifetime income groups', '$J$'],
    'S': ['Maximum periods in economically active individual life',
          '$S$'],
    'E': ['Number of periods of youth economically outside the model',
          '$E$'],
    'T': ['Number of periods to steady-state', '$T$'],
    'retirement_age': ['Retirement age', '$R$'],
    'ltilde': ['Maximum hours of labor supply', r'$\tilde{l}$'],
    'beta': ['Discount factor', r'$\beta$'],
    'sigma': ['Coefficient of constant relative risk aversion',
              r'$\sigma$'],
    'frisch': ['Frisch elasticity of labor supply', r'$\nu$'],
    'b_ellipse': ['Scale parameter in utility of leisure', '$b$'],
    'upsilon': ['Shape parameter in utility of leisure', r'$\upsilon$'],
    # 'k': ['Constant parameter in utility of leisure', 'k'],
    'chi_n': ['Disutility of labor level parameters',
              r'$\left{\chi^{n}_{s}\right}_{s=1}^{S}$'],
    'chi_b': ['Utility of bequests level parameters',
              r'$\left{\chi^{b}_{j}\right}_{j=1}^{J}$'],
    'use_zeta': [
        'Whether to distribute bequests between lifetime income groups',
        r'$\texttt{use_zeta}$'],
    'zeta': ['Distribution of bequests', r'$\zeta$'],
    'Z': ['Total factor productivity', '$Z_{t}$'],
    'gamma': ['Capital share of income', r'$\gamma$'],
    'epsilon': ['Elasticity of substitution between capital and labor',
                r'\varepsilon'],
    'delta': ['Capital depreciation rate', r'$\delta$'],
    'g_y': [
        'Growth rate of labor augmenting technological progress',
        r'$g_{y}$'],
    'tax_func_type': ['Functional form used for income tax functions',
                      r'$\texttt{tax_func_type}$'],
    'analytical_mtrs': ['Whether use analytical MTRs or estimate MTRs',
                        r'$\texttt{analytical_mtrs}$'],
    'age_specific': ['Whether use age-specific tax functions',
                     r'$\texttt{age_specific}$'],
    'tau_payroll': ['Payroll tax rate', r'$\tau^{p}_{t}$'],
    # 'theta': ['Replacement rate by average income',
    #           r'\left{\theta_{j}\right}_{j=1}^{J}'],
    'tau_bq': ['Bequest (estate) tax rate', r'$\tau^{BQ}_{t}}$'],
    'tau_b': ['Entity-level business income tax rate',
              r'$\tau^{b}_{t}$'],
    'delta_tau': ['Rate of depreciation for tax purposes',
                  r'$\delta^{\tau}_{t}$'],
    'tau_c': ['Consumption tax rates', r'$\tau^{c}_{t,s,j}$'],
    'h_wealth': ['Coefficient on linear term in wealth tax function',
                 '$H$'],
    'm_wealth': ['Constant in wealth tax function', '$M$'],
    'p_wealth': ['Coefficient on level term in wealth tax function',
                 '$P$'],
    'budget_balance': ['Whether have a balanced budget in each period',
                       r'$\texttt{budget_balance}$'],
    'baseline_spending': ['Whether level of spending constant between '
                          + 'the baseline and reform runs',
                          r'$\texttt{baseline_spending}$'],
    'alpha_T': ['Transfers as a share of GDP', r'$\alpha^{T}_{t}$'],
    'eta': ['Distribution of transfers', r'$\eta_{j,s,t}$'],
    'alpha_G': ['Government spending as a share of GDP',
                r'$\alpha^{G}_{t}$'],
    'tG1': ['Model period in which budget closure rule starts',
            r'$t_{G1}$'],
    'tG2': ['Model period in which budget closure rule ends',
            r'$t_{G2}$'],
    'rho_G': ['Budget closure rule smoothing parameter', r'$\rho_{G}$'],
    'debt_ratio_ss': ['Steady-state Debt-to-GDP ratio',
                      r'$\bar{\alpha}_{D}$'],
    'initial_debt_ratio': ['Initial period Debt-to-GDP ratio',
                           r'$\alpha_{D,0}$'],
    'r_gov_scale': ['Scale parameter in government interest rate wedge',
                    r'$\tau_{d,t}$'],
    'r_gov_shift': ['Shift parameter in government interest rate wedge',
                    r'$\mu_{d,t}$'],
    'AIME_num_years': ['Number of years over which compute AIME',
                       r'$\texttt{AIME_num_years}$'],
    'AIME_bkt_1': ['First AIME bracket threshold',
                   r'$\texttt{AIME_bkt_1}$'],
    'AIME_bkt_2': ['Second AIME bracket threshold',
                   r'$\texttt{AIME_bkt_2}$'],
    'PIA_rate_bkt_1': ['First AIME bracket PIA rate',
                       r'$\texttt{PIA_rate_bkt_1}$'],
    'PIA_rate_bkt_2': ['Second AIME bracket PIA rate',
                       r'\texttt{PIA_rate_bkt_2}'],
    'PIA_rate_bkt_3': ['Third AIME bracket PIA rate',
                       r'$\texttt{PIA_rate_bkt_3}$'],
    'PIA_maxpayment': ['Maximum PIA payment',
                       r'$\texttt{PIA_maxpayment}$'],
    'PIA_minpayment': ['Minimum PIA payment',
                       r'$\texttt{PIA_maxpayment}$'],
    'replacement_rate_adjust': ['Adjustment to replacement rate',
                                r'$theta_{adj,t}$'],
    'small_open': ['Whether modeling a small, open economy',
                   r'$\texttt{small_open}$'],
    'world_int_rate': ['World interest rate', r'$r^{*}_{t}$'],
    'initial_foreign_debt_ratio': [
        'Share of government debt held by foreigners in initial period',
        r'$D_{f,0}$'],
    'zeta_D': ['Share of new debt issues purchased by foreigners',
               r'$\zeta_{D, t}$'],
    'zeta_K': ['Share of excess capital demand satisfied by foreigners',
               r'$\zeta_{K, t}$'],
    'nu': ['Dampening parameter for TPI', r'$\xi$'],
    'maxiter': ['Maximum number of iterations for TPI',
                r'$\texttt{maxiter}$'],
    'mindist_SS': ['SS solution tolerance', r'$\texttt{mindist_SS}$'],
    'mindist_TPI': ['TPI solution tolerance', r'$\texttt{mindist_TPI}$']
}

# Ignoring the following:
# 'starting_age', 'ending_age', 'constant_demographics',
# 'constant_rates', 'zero_taxes'
