% To plot QQplots for modeled and observed daily max surges %

bst = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\BestMdl_v2' %source - best model
dst = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\best_model\QQplots_v3' %destination

cd(bst)
lst_bst = dir('*mat')
for ii =299:299%length(lst_bst)
    ii
    cd(bst)
    load(lst_bst(ii).name);
    
    q1 = quantile(y_surge(:,2), length(y_surge))'; % creating quantiles
    q2 = quantile(y_rec(:,2), length(y_rec))';
    %close all;
    figure; scatter(q1,q2); % plotting quantiles
    hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 1); % 1:1 trend line
    xlabel('Observerd Surge (m)'); ylabel('Simulated Surge (m)')
    %grid on;
    title('Q-Q plot - observed vs simulated surge')
    %set(gcf,'units','normalized','outerposition',[0 0 1 1]) % to automatically maximize screen
    
    %saving plot
%     cd(dst)
%     d = sprintf('%s.jpeg', lst_bst(ii).name); %saving title
%     saveas(figure(1),d);
end
