% To plot QQplots for modeled and observed daily max surges %

bst = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\BestMdl_v2' %source - best model
dst = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\QQplots_v2' %destination

cd(bst)
lst_bst = dir('*mat')
for ii =1:length(lst_bst)
    cd(bst)
    load(lst_bst(ii).name);
    
    close all;
    subplot(2,2,1); qqplot(y_surge(:,2)); % Observed Surge Vs Theoretical normal distribution
    title('QQ Plot of Observed daily max surge versus Standard Normal','FontSize',11 );
    subplot(2,2,2); qqplot(y_rec(:,2)); % modeled surge Vs Theoretical normal distribution
    title('QQ Plot of Modeled daily max surge versus Standard Normal','FontSize',11 );
    subplot(2,2,3); qqplot(y_surge(:,2), y_rec(:,2)); % observed vs modeled surge
    xlabel('Observed Surge Quantiles'); ylabel('Modeled Surge Quantiles');
    title('QQ Plot of Observed Vs Modeled daily max surge','FontSize',11 );
   
    set(gcf,'units','normalized','outerposition',[0 0 1 1]) % to automatically maximize screen
    
    %saving plot
    cd(dst)
    d = sprintf('%s.jpeg', lst_bst(ii).name); %saving title
    saveas(figure(1),d);
end
