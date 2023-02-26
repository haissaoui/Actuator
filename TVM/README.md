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
$i = (\frac{FV+\frac{PMT}{i}}{PV + \frac{PMT}{i}})^\frac{1}{n}$
