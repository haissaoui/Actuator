# Case 1: Unknown FV:
$FV = PV \times (1+i)^n + PMT \times \frac{(1+i)^n-1}{i}$
# Case 2: Unkown PV:
$PV = FV \times (\frac{1}{1+i})^n + PMT \times \frac{1-(\frac{1}{n+1})^n}{i}$
# Case 3: Unkown PMT:
$PMT = \frac{FV - PV\times (1+i)^n}{\frac{(1+i)^n-1}{i}}$
# Case 4: Unkown N:
$n = \frac{\log(\frac{FV+\frac{PMT}{i}}{PV+\frac{PMT}{i}})}{\log(1+i)}$
