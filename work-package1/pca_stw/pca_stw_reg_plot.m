
    % Plotting
    % To plot modelled and observed surge
    
    figure; 
    %subplot(4,4,13);
    obs_mdl = [Twind y_surge y_recsurge];
    ss = scatter(obs_mdl(:,2), obs_mdl(:,3), '+', 'k');
    xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
    hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);
    toptitle = sprintf('%s', list_tg(t).name);
    title(toptitle); 
    R = corr(y_surge, y_recsurge); R_squared = R^2;
    xx = y_surge; yy = y_recsurge; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean);
    text(-0.06, 0.18, ['R^2 = ' num2str(R_squared)], 'Color', 'red', 'FontSize', 12);
    text(-0.06, 0.15, ['RMSE = ' num2str(sg_rmse*100) 'cm'], 'Color', 'red', 'FontSize', 12);
    set(gca, 'Box', 'on', 'XMinorTick', 'on', 'YMinorTick', 'on', 'fontname', 'times');
  
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   
    % Plotting
    figure; scatter(y_skew, y_recskew);
    xlabel('Observed Skew Surge(m)'); ylabel('Modelled Skew Surge(m)');
    hline = refline([1, 0]); hline.Color = 'r';
    toptitle = sprintf('%s', list_tg(t).name);
    title(toptitle);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
%% Checking distributions
figure;
subplot(1,2,1); 
hist(y_surge);
title(toptitle); 
subplot(1,2,2);
hist(y_recsurge);
title(toptitle); 
 
    
    
    
    
    
    
    
    

