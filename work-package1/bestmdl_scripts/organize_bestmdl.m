% To organize files for the best model %

% Define m1 m2 m3 directories

m1 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_1\03_27_2019\M1_Kfold_randomized_v2'
cd(m1); lst_m1 = dir('*.mat');
m2 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\04_01_2019\M2_Kfold_randomized_v2'
cd(m2); lst_m2 = dir('*.mat');
m3 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_3\04_04_2019\M3_Kfold_randomized_v2'
cd(m3); lst_m3 = dir('*mat');

b_pat = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\BestMdl_v2' % destination folder

% load results of best model
cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\bestmdl_results'
load('FinalModel4Plot.mat');

for ii = 1:length(final_mdl)
    if final_mdl(ii, 3) == 1
       cd(m1); mdl = lst_m1(ii).name;
       load(mdl);
    elseif final_mdl(ii, 3) == 2
        cd(m2); mdl = lst_m2(ii).name;
        load(mdl);
    else
        cd(m3); mdl = lst_m3(ii).name;
        load(mdl);
    end
    
    if final_mdl(ii, 1:2) ~= [lon_t lat_t]
        return;
    else
        copyfile(mdl, b_pat);
    end
    clearvars -except m1 m2 m3 lst_m1 lst_m2 lst_m3 b_pat final_mdl ii 
end 


