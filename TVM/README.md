# Case 1: Unknown FV:
$FV = PV \times (1+i)^n + PMT \times \frac{(1+i)^n-1}{i}$  
# Case 2 : Unknown PV:
$PV = FV \times (\frac{1}{1+i})^n + PMT \times \frac{1 - (\frac{1}{1+i})^n}{i}$
# Case 3 : Unknown PMT:
$PMT = \frac{FV - PV \times (1 + i)^n}{\frac{(1 + i)^n - 1}{i}}$
# Case 4 : Unknown N:
$n = \frac{1}{\ln(1 + i)}\times\frac{FV+\frac{PMT}{i}}{PV + \frac{PMT}{i}}$
