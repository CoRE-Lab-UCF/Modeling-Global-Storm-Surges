% To reconstruct storm surges using the best models % 

% Load best model time series 

cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model'
load('best_mdl_number.mat')

for ii = 1:length(bestmdl_num)
    if bestmdl_num(ii, 3) == 1
        base_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_1\MLR_Kfold_10X10_17yrs'
    elseif bestmdl_num(ii, 3) == 2
        base_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\M2.5\mdl2p5_MLR_Kfold_4daily_10X10_17yrs'
    else
        base_path = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_3\M3.5\mdl3p5_RF_Kfold_4daily_10X10_17yrs'
    end
    
    cd(base_path)
    lst = dir('*.mat')
    cd(fullfile(base_path, lst(ii).name))
    a = dir('*.mat');
    load(a.name) %loading results of pca and kfold validation
    clearvars -except ii bestmdl_num m123_732 base_path a vars y_surge 
    
    % Add date/time for the daily max surge
    cd 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
    sg_lss = dir('*4d10X10')
    cd(sg_lss(ii).name)
    load('surge_dmax.mat')
    find(surge_sub(:,2) ~= y_surge)
    
    
    % Apply stepwise regression - with all surge record
    
    [b,se,pval,inmodel,stats,nextstep,history] = stepwisefit(vars, y_surge);
    
    % Reconstructing daily max surge 
    vars_new = vars(:,find(inmodel == 1));
    b_new = b(find(inmodel == 1));
    y_recsurge = stats.intercept + vars_new*b_new;

    
end

