# Variables
- N: Stands for the number of periods, which is the total number of compounding periods for the investment. This key is used to enter the number of years, months, or days for which the investment is held.

- I/Y: Stands for the interest rate per year or per period. This key is used to enter the interest rate for the investment. You can enter the annual rate or the rate per compounding period.

- PV: Stands for the present value, which is the value of the investment at the beginning of the investment period. This key is used to enter the initial investment amount.

- PMT: Stands for the payment amount, which is the fixed payment amount made at the end of each compounding period. This key is used to enter the regular payment amount made on the investment.

- FV: Stands for the future value, which is the value of the investment at the end of the investment period. This key is used to calculate the future value of the investment based on the initial investment amount, the regular payment amount, and the interest rate.

# Formulae
## Case 1: Unknown FV:
$FV = -(PV \times (1+i)^n + PMT \times \frac{(1+i)^n-1}{i})$  
## Case 2 : Unknown PV:
$PV = -(FV \times (\frac{1}{1+i})^n + PMT \times \frac{1 - (\frac{1}{1+i})^n}{i})$
## Case 3 : Unknown PMT:
$PMT = \frac{-FV - PV \times (1 + i)^n}{\frac{(1 + i)^n - 1}{i}}$
## Case 4 : Unknown N:
$n = \frac{\ln(\frac{FV+\frac{PMT}{i}}{PV + \frac{PMT}{i}})}{\ln(1 + i)}$
## Case 5 : Unknown I/Y:
To solve for i, we need to use numerical methods such as the bisection method:
### Bisection method:
The bisection method is a simple numerical algorithm used to find the root of a function. The algorithm works by initially setting two endpoints, $a$ and $b$, on either side of the root. The midpoint $c$ is then calculated and used to evaluate the function at that point. Depending on the sign of the function value at $c$, the interval $[a, c]$ or $[c, b]$ is selected as the new interval containing the root. This process is repeated iteratively until the interval containing the root is found to within a specified tolerance.

Here is a step-by-step description of the bisection method as an algorithm:

1. Set the initial endpoints $a$ and $b$ on either side of the root.
2. Calculate the midpoint $c$ as $c = (a + b) / 2$.
3. Evaluate the function $f$ at $c$.
4 If $f(c)$ is equal to zero or within a specified tolerance, then stop and return c as the root.
5. If $f(c)$ has the same sign as $f(a)$, set $a = c$, otherwise set $b = c$.
6. Go back to step 2 and repeat until the interval containing the root is found to within a specified tolerance.
The bisection method is guaranteed to converge to a root if the function is continuous and changes sign over the interval $[a, b]$. However, it can be slow to converge for some functions and may require a large number of iterations to achieve the desired tolerance.
