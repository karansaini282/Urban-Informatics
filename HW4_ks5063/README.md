# HomeWork 4

This repository is a submission for Homework 4 for PUI 2018.

* Assignment 1 + Extra Credit : Done by Karan (ks5063)
    * First step was changing dictionary keys from distribution size to indices to prevent overwriting of keys.
    * Normal distribution was assigned mean = 100 using loc = 100. Sample mean vs Sample size was observed.
    * Poisson distribution was assigned mean = 100 using lam = 100. Sample mean vs Sample size was observed.
    * Binomial distribution was assigned mean = 100 using n = 200 and p = 0.5. Sample mean vs Sample size was observed.
    * Lognormal distribution was assigned mean = 100 using mean = np.log(100) - 0.5. Sample mean vs Sample size was observed.
    * All distributions were combined.
        * Sample mean vs Sample size was observed.
        * Gaussian curve was fitted to the histogram.
* Assignment 2 : Done by Saloni (ss12513)
   * An idea is formulated by observing categorical fields in the data and observing patterns with numerical data.
   * NULL HYPOTHESIS is stated. This is the hypotheis to be tested which is measureable.
   * ALTERNATIVE HYPOTHESIS is stated.
   * A significance level of 0.05 is chosen.
   * Environment variable is PUIDATA is set. The dataset is downloaded, unzipped and moved to PUIDATA.
   * The dataset is read using python to a dataframe.
   * Top few rows of the dataframe is displayed.
   * Top few rows of the reducted dataframe is displayed. The fields of interest are usertype and birth year. Age is calculated from the birth year.
   * Distribution of the remaining data is plot using bar graph and histogram. 

* Assignment 3 : Saloni has done hypothesis creation and Z-test. Karan has done interpretation of result.
   * IDEA: The new bus routes of bus line X8 improves circulation.
   * To test this the NULL HYPOTHESIS and ALTERNATIVE HYPOTHESIS are set.
   * NULL HYPOTHESIS: The average duration of trips of the new bus routes of bus line X8 is the same or higher than that of the original bus routes, significance level = 0.05.
   * ALTERNATIVE HYPOTHESIS: The average duration of the new bus routes of bus line X8 is significantly lower.
   * Environment variable is PUIDATA is set. The dataset is downloaded and moved to PUIDATA.
   * The times.txt file is read and the journey durations of the sample are stored.
   * The population mean and population standard devation are set to 36 and 6 respectively as given by the problem statement. The sample mean is calcluated. 
   * Z-statistic is calculated as 2.55639718617. The z-statistic is compared with the significance level and the Null Hypothesis is rejected.  
