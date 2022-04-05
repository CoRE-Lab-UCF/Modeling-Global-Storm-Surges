### Trend calculation – sensitivity analysis

* Choose 1900-2010 period as this is common for G-20CR and G-E20C and in some cases for observations too

* Choose a window length of 30 years (allow user to modify in script)

`for yr in years:`
`	for w in window:`
`		if (yr + w) > 1930:`
`			continue`
`		else:`
`			print("year: {} window: {} {}-{}".format(yr, w, yr, yr+w))`


* Pick 2/3 tide gauges with 1900-2010 period after data preparation 

* Get annual 99th/95th percentiles

For each window, filter the three time series based on observation time series

Check if all three start at the current start_year and end at current end_year

Check completeness (75% but allow user to change) @each window and if not fulfilled, disregard – or make trend value and p value as nan

