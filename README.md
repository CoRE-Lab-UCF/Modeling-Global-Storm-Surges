# Modeling Global Storm Surges in the Past, Present, and Future and the Associated Socio-Economic Impacts

This is a collection of scripts used for the NASA funded project "Modeling Global Storm Surges in the Past, Present, and Future and the Associated Socio-Economic Impacts". The results from the project are published as [Tadesse et al. (2020)](https://www.frontiersin.org/articles/10.3389/fmars.2020.00260/full) and [Tadesse and Wahl (2021)](https://doi.org/10.1038/s41597-021-00906-x).

Under this project, a database of "Global Storm Surge Reconstructions (GSSR)" was developed, which can be accessed here 👇  

<a href="http://gssr.info/"><img width="1093" alt="gssr" src="https://user-images.githubusercontent.com/15319503/158024519-691f256b-ce7b-43f9-bd54-ab7be0eb5716.png"></a>


</p>
 <p align="center">
  <a href="https://twitter.com/CoRELabUCF"><img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter@CoRELabUCF"></a>
 <a href="http://gssr.info/"><img src="https://img.shields.io/badge/gssr.info%20-%2302569B.svg?&style=for-the-badge&logo=WordPress&logoColor=white" alt="GSSR"></a>
</p>


## 1. Background

Understanding how the storm surge climate has changed in the past is important to predict the future. Unfortunately, a major hurdle in the study of storm surges is that observational records from tide gauges are often short, making it difficult to assess long-term trends and decadal variability as well as performing robust statistical analyses. For example, as a rule of thumb in extreme value analysis, extrapolation should be limited to return periods not longer than four times the available record length. This means in order to extrapolate to a 100-year storm surge event, at least 25 years of data are needed. However, 45% of the tide gauges in the [GESLA-2](https://www.gesla.org/) database have less than 25 years of data, which clearly limits our ability to derive robust statistics and assess long-term changes.

## 2. What we provide

The Global Storm Surge Reconstruction (GSSR) database includes daily maximum surge values for the past at 882 tide gauges distributed along the global coastline. The data-driven models employed for the surge reconstruction were developed by [Tadesse et al. (2020)](https://www.frontiersin.org/articles/10.3389/fmars.2020.00260/full). We use five different atmospheric reanalysis products with different spatial and temporal resolution to produce surge information for the periods covered by the different reanalyses. The web-map above allows the user to download daily maximum surge values for individual tide gauges and reanalysis products. The reanalysis that leads to the best validation results is marked with "best reconstruction" (note that in some locations data is not available for all reanalyses as there is no overlap in the periods covered by the tide gauges and the reanalysis). The full surge reconstruction for each reanalysis (comprised of 882 compressed individual .csv files for the different tide gauges) can be downloaded from the following links:

- 20-CR Surge Reconstruction [1836 - 2015]
- ERA-20C Surge Reconstruction [1900 - 2010]
- ERA-Interim Surge Reconstruction [1979 - 2019]
- MERAA-2 Reconstruction [1980 - 2019]
- ERA-Five Reconstruction [1979 - 2019]


## 3. Predictor and Predictand Datasets

- ERA-Interim global atmospheric reanalysis,
- ERA-20C global atmospheric reanalysis,
- 20CRV3 (NOAA-CIRES) atmospheric reanalysis,
- MERRA-2 atmospheric reanalysis,
- ERA-Five atmospheric reanalysis,
- Global Extreme Sea Level Analysis - Sea-level Data

## 4. Methodology

The data-driven models used to develop GSSR are described in detail in [Tadesse et al. (2020)](https://www.frontiersin.org/articles/10.3389/fmars.2020.00260/full).

![alt text](http://gssr.info/images/figure1.png)

## 5. Model Validation

Validation results of the data-driven models for the surge reconstructions derived with the five different reanalysis products can be downloaded through the following links (note that the validation was carried out for the common period from 1980 to 2010 where all reanalyses have data):

- 20-CR Validation
- ERA-20C Validation
- ERA-Interim Validation
- MERAA-2 Validation
- ERA-Five Validation


## 6. Acknowledgement

The research that resulted in the development of the GSSR database was funded by the National Aeronautics and Space Administration (NASA) under the New (Early Career) Investigator Program in Earth Science ( grant number: 80NSSC18K0743)

Reports, articles, or manuscripts that make use of GSSR data shall include an acknowledgement to this web site and refer to the paper by Tadesse et al. (2021). We would be grateful to be notified of such papers and, if possible, sent copies of them. The following citation shall be used to refer to the paper:

###  Reference/Citation

> Tadesse M., Wahl T. and Cid A. (2020). Data-Driven Modeling of Global Storm Surges. Frontiers in Marine Science, 7:260. https://doi.org/10.3389/fmars.2020.00260

> Tadesse, M.G., Wahl, T. (2021). A database of global storm surge reconstructions. Nature Scientific Data 8, 125. https://doi.org/10.1038/s41597-021-00906-x 
