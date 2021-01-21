%plotting script for figure 6 - threshold exceedence

%loading figures
cd 'F:\OneDrive - Knights - University of Central Florida\UCF\Projekt.28\Report\Spring 2019\#1 - Paper\Figures\MdlB_GTSR\figure6_modelA'
st = hgload('St_augustine_thres-CECS8CX3VN2-2.fig');
cx = hgload('cuxhaven_thres.fig');
zz = hgload('Zanzibar_mdlB_thres.fig');
vh = hgload('victoriaharbor_thres.fig');
wk = hgload('Wakkanai_thres-CECS8CX3VN2.fig');
pa = hgload('Puerto_armuelles_thres.fig');

figure;
x = (-5:5);
y = (-5:5);
%set(gcf, 'unit', 'normalized', 'position', [0.15, 0.15,0.9,0.7])

h(1) = subplot(2,3,1); 
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(st,'CurrentAxes')),h(1));
title('St. Augustine')
h(1).FontSize = 20
h(1).XLim = [0 1]
h(1).YLim = [0 1]
xlabel('Observed Surge (m)')
ylabel('Model A Surge (m)')

h(2) = subplot(2,3,2); 
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(cx,'CurrentAxes')),h(2));
title('Cuxhaven')
h(2).FontSize = 20
h(2).XLim = [0 4]
h(2).YLim = [0 4]
xlabel('Observed Surge (m)')
ylabel('Model A Surge (m)')

h(3) = subplot(2,3,3); 
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(zz,'CurrentAxes')),h(3));
title('Zanzibar')
h(3).FontSize = 20
h(3).XLim = [0 0.3]
h(3).YLim = [0 0.3]
xlabel('Observed Surge (m)')
ylabel('Model A Surge (m)')


h(4) = subplot(2,3,4); 
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(vh,'CurrentAxes')),h(4));
title('Victoria Harbor')
h(4).FontSize = 20
h(4).XLim = [0 1]
h(4).YLim = [0 1]
xlabel('Observed Surge (m)')
ylabel('Model A Surge (m)')

h(5) = subplot(2,3,5); 
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(wk,'CurrentAxes')),h(5));
title('Wakkanai')
h(5).FontSize = 20
h(5).XLim = [0 0.8]
h(5).YLim = [0 0.8]
xlabel('Observed Surge (m)')
ylabel('Model A Surge (m)')

h(6) = subplot(2,3,6); 
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(pa,'CurrentAxes')),h(6));
title('Puerto Armuelles')
h(6).FontSize = 20
h(6).XLim = [0 1]
h(6).YLim = [0 1]
xlabel('Observed Surge (m)')
ylabel('Model A Surge (m)')