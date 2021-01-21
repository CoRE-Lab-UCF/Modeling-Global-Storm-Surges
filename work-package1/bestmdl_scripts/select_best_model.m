% To choose the best model for each TG (considering Correlation, RMSE and NSE) %

cd ('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\bestmdl_results')
load('M1+M2+M3_results.mat')

best_mdl(:,1:2) = kfold_M1(:,1:2);

for ii = 1:length(kfold_M1)
    ii
    %best correlation
    corl = [kfold_M1(ii, 3) kfold_M2(ii, 3) kfold_M3(ii, 3)];
    [a b] = max(corl);
    best_mdl(ii,3) = a; 
    
    %corresponding pval for correlation
    if b == 1
        best_mdl(ii,4) = kfold_M1(ii, 4);
    elseif b == 2
        best_mdl(ii,4) = kfold_M2(ii, 4);
    else
        best_mdl(ii,4) = kfold_M3(ii, 4);
    end
    
    % model number for best correlation
    best_mdl(ii,5) = b;
    
    %best RMSE
    rmse = [kfold_M1(ii, 5) kfold_M2(ii, 5) kfold_M3(ii, 5)];
    [a b] = min(rmse);
    best_mdl(ii,6:7) = [a b];
    
    %best NSE
    nse = [kfold_M1(ii, 7) kfold_M2(ii, 7) kfold_M3(ii, 7)];
    [a b] = max(nse); 
    best_mdl(ii,8:9) = [a b]; 
    
    %choosing the best model
    c = [best_mdl(ii,5) best_mdl(ii,7) best_mdl(ii,9)];
    d = unique(c);
    if length(d) == 1
        best_mdl(ii,10) = d; %best model for the TG at hand
    elseif length(d) == 2
        best_mdl(ii,10) = mode(c); %choose most common
    else 
        best_mdl(ii,10) = NaN;
    end
end

%% Final model with fewer variables

final_mdl(:,1:2) = best_mdl(:,1:2); % lon and lat of TG
final_mdl(:,3) = best_mdl(:,10); % best model for this TG

for jj = 1:length(final_mdl)
    jj
    if final_mdl(jj,3) == 1
        final_mdl(jj,4) = kfold_M1(jj, 3); % correlation
        final_mdl(jj,5) = kfold_M1(jj, 4); % pval - significance
        final_mdl(jj,6) = kfold_M1(jj, 5); % rmse
        final_mdl(jj,7) = kfold_M1(jj, 6); % relative rmse
        final_mdl(jj,8) = kfold_M1(jj, 7); % nse
    elseif final_mdl(jj,3) == 2
        final_mdl(jj,4) = kfold_M2(jj, 3);
        final_mdl(jj,5) = kfold_M2(jj, 4); % pval - significance
        final_mdl(jj,6) = kfold_M2(jj, 5); % rmse
        final_mdl(jj,7) = kfold_M2(jj, 6); % relative rmse
        final_mdl(jj,8) = kfold_M2(jj, 7); % nse
    else
        final_mdl(jj,4) = kfold_M3(jj, 3);
        final_mdl(jj,5) = kfold_M3(jj, 4); % pval - significance
        final_mdl(jj,6) = kfold_M3(jj, 5); % rmse
        final_mdl(jj,7) = kfold_M3(jj, 6); % relative rmse
        final_mdl(jj,8) = kfold_M3(jj, 7); % nse
    end
end































