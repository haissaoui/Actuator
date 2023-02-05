# This function determine the effective rate of interest
def effective_rate_of_interest(a_t, a_t_m_1):
    i_t = (a_t - a_t_m_1) / a_t_m_1
    return i_t


# This function determine the effective rate of discount
def effective_rate_of_discount(a_t, a_t_m_1):
    d_t = (a_t - a_t_m_1) / a_t
    return d_t


# This function calculate the accumulated value
def accumulated_value(a_0, i, t):
    a_v = a_0 * (1 + i) ** t
    return a_v


# This function convert the rate of interest to rate of discount
def interest_to_discount_converter(i):
    d = 1 - 1 / (1+i)
    return d


# This function convert the rate of discount to rate of interest
def discount_to_interest_converter(d):
    i = 1/(1 - d) - 1
    return i


# This function convert effective annual rate of interest to nominal periodic rate
def nominal_to_effective_interest_rate(i, m):
    i_m = m * ((1 + i) ** (1 / m) - 1)
    return i_m
