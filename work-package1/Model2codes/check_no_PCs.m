% To count the number of predictors used after PCA

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\M2.5\mdl2p5_PCA_4Xdaily10X10_17yrs'
dd = dir('*.mat')
prd = [];
for mt = 1:length(dd)
    load(dd(mt).name)
    [a b] = size(vars);
    prd = [prd; b]; 
end

save('numb_predictors_afterPCA_449TGs.mat')
