%plotting script for figure 6 - threshold exceedence

%loading figures
cd 'F:\OneDrive - Knights - University of Central Florida\UCF\Projekt.28\Report\Spring 2019\#1 - Paper\Figures\MdlB_GTSR\figure12_modelBts_scatter_qq'

f1 = hgload('Boston_comparison.fig')
f2 = hgload('Boston_scatter_mdlb.fig')
f3 = hgload('Boston_scatter_gtsr')
f4 = hgload('Goteborg_Torshamnen_comparison.fig')
f5 = hgload('Goteborg_Torshamnen_scatter_mdlb.fig')
f6 = hgload('Goteborg_Torshamnen_scatter_gtsr.fig')
f7 = hgload('Mar_del_Plata_comparison.fig')
f8 = hgload('Mar_del_Plata_scatter_mdlb.fig')
f9 = hgload('Mar_del_Plata_scatter_gtsr.fig')
f10 = hgload('Bluff_Harbour_comparison.fig')
f11 = hgload('Bluff_Harbour_scatter_mdlb.fig')
f12 = hgload('Bluff_Harbour_gtsr_scatter.fig')
f13 = hgload('Kushiro_comparison.fig')
f14 = hgload('Kushiro_mdlB_scatter_mdlb.fig')
f15 = hgload('Kushiro_mdlB_scatter_gtsr.fig')
f16 = hgload('Zanzibar_comparison.fig')
f17 = hgload('Zanzibar_scatter_mdlB.fig')
f18 = hgload('Zanzibar_gtsr_scatter.fig')



figure;

x = (-5:5);
y = (-5:5);

h(16)=subplot(6,3,16);
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.14,0.65,0.2])
copyobj(allchild(get(f16,'CurrentAxes')),h(16));
% title('e) Zanzibar')
%h(7).YLim = [-1  1.5]
h(16).FontSize = 16
h(16).XLim = [733043 733407]
%xlabel('Observed Surge (m)')
% ylabel('Surge Height (m)')

h(17)=subplot(6,3,17);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f17,'CurrentAxes')),h(17));
%title('Mar del Plata')
h(17).FontSize = 16
%h(8).YLim = [-1  1.0]
h(17).XLim = [-0.2 0.4]
h(17).YLim = [-0.2 0.4]
% xlabel('Observed Surge (m)')
% ylabel('Model B Surge (m)')

h(18)=subplot(6,3,18);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f18,'CurrentAxes')),h(18));
%title('Mar del Plata')
h(18).XLim = [-0.2 0.4]
h(18).YLim = [-0.2 0.4]
h(18).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('GTSR Surge (m)')

%adjusting the subplots
set(h(16), 'Position', [0.05, 0.03, 0.48,0.11])
set(h(17), 'Position', [0.6, 0.03,0.13,0.11])
set(h(18), 'Position', [0.8, 0.03,0.13,0.11])
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
h(13)=subplot(6,3,13);
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.14,0.65,0.2])
copyobj(allchild(get(f13,'CurrentAxes')),h(13));
% title('e) Kushiro')
%h(7).YLim = [-1  1.5]
h(13).FontSize = 16
h(13).XLim = [733043 733407]
%xlabel('Observed Surge (m)')
% ylabel('Surge Height (m)')

h(14)=subplot(6,3,14);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f11,'CurrentAxes')),h(14));
%title('Mar del Plata')
h(14).FontSize = 16
%h(8).YLim = [-1  1.0]
h(14).XLim = [-0.5 0.8]
h(14).YLim = [-0.5 0.8]
% xlabel('Observed Surge (m)')
% ylabel('Model B Surge (m)')

h(15)=subplot(6,3,15);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f15,'CurrentAxes')),h(15));
%title('Mar del Plata')
h(15).XLim = [-0.5 1]
h(15).YLim = [-0.5 1]
h(15).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('GTSR Surge (m)')

%adjusting the subplots
set(h(13), 'Position', [0.05, 0.2, 0.48,0.11])
set(h(14), 'Position', [0.6, 0.2,0.13,0.11])
set(h(15), 'Position', [0.8, 0.2,0.13,0.11])
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

h(10)=subplot(6,3,10);
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.14,0.65,0.2])
copyobj(allchild(get(f10,'CurrentAxes')),h(10));
% title('d) Bluff Harbor')
%h(7).YLim = [-1  1.5]
h(10).FontSize = 16
h(10).XLim = [733043 733407]
%xlabel('Observed Surge (m)')
% ylabel('Surge Height (m)')

h(11)=subplot(6,3,11);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f11,'CurrentAxes')),h(11));
%title('Mar del Plata')
h(11).FontSize = 16
%h(8).YLim = [-1  1.0]
h(11).XLim = [-0.5 1]
h(11).YLim = [-0.5 1]
% xlabel('Observed Surge (m)')
% ylabel('Model B Surge (m)')

h(12)=subplot(6,3,12);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f12,'CurrentAxes')),h(12));
%title('Mar del Plata')
h(12).XLim = [-0.5 1]
h(12).YLim = [-0.5 1]
h(12).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('GTSR Surge (m)')

%adjusting the subplots
set(h(10), 'Position', [0.05, 0.37, 0.48,0.11])
set(h(11), 'Position', [0.6, 0.37,0.13,0.11])
set(h(12), 'Position', [0.8, 0.37,0.13,0.11])
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
h(7)=subplot(6,3,7);
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.14,0.65,0.2])
copyobj(allchild(get(f7,'CurrentAxes')),h(7));
% title('c) Mar del Plata')
%h(7).YLim = [-1  1.5]
h(7).FontSize = 16
h(7).XLim = [733043 733407]
%xlabel('Observed Surge (m)')
% ylabel('Surge Height (m)')

h(8)=subplot(6,3,8);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f8,'CurrentAxes')),h(8));
%title('Mar del Plata')
h(8).FontSize = 16
%h(8).YLim = [-1  1.0]
h(8).XLim = [-1 2]
h(8).YLim = [-1 2]
% xlabel('Observed Surge (m)')
% ylabel('Model B Surge (m)')

h(9)=subplot(6,3,9);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f9,'CurrentAxes')),h(9));
%title('Mar del Plata')
h(9).XLim = [-1 2]
h(9).YLim = [-1 2]
h(9).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('GTSR Surge (m)')

%adjusting the subplots
set(h(7), 'Position', [0.05, 0.54, 0.48,0.11])
set(h(8), 'Position', [0.6, 0.54,0.13,0.11])
set(h(9), 'Position', [0.8, 0.54,0.13,0.11])
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

h(4)=subplot(6,3,4);
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.44,0.65,0.2])
copyobj(allchild(get(f4,'CurrentAxes')),h(4)); 
% title('b) Goteborg-Torshamnen')
h(4).FontSize = 16
h(4).XLim = [733043 733407]
%xlabel('Observed Surge (m)')
% ylabel('Surge Height (m)')
datetick('keeplimits')

h(5)=subplot(6,3,5);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f5,'CurrentAxes')),h(5)); 
%title('Goteborg-Torshamnen')
h(5).XLim = [-.6 1.5]
h(5).YLim = [-.6 1.5]
h(5).XTick = [-0.5000 0.5000  1.5000]
h(5).YTick = [-0.5000 0.5000  1.5000]
h(5).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('Model B Surge (m)')

h(6)=subplot(6,3,6);
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f6,'CurrentAxes')),h(6));
%title('Goteborg-Torshamnen')
h(6).XLim = [-.6 1.5]
h(6).YLim = [-.6 1.5]
h(6).XTick = [-0.5000 0.5000  1.5000]
h(6).YTick = [-0.5000 0.5000  1.5000]
h(6).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('GTSR Surge (m)')

%adjusting the subplots
set(h(4), 'Position', [0.05, 0.71, 0.48,0.11])
set(h(5), 'Position', [0.6, 0.71,0.13,0.11])
set(h(6), 'Position', [0.8, 0.71,0.13,0.11])
%-------------------------------------------------------------------------%
%set(gcf, 'unit', 'normalized', 'position', [0.15, 0.15,0.9,0.7])
h(1) = subplot(6,3,1); 
%set(gca, 'unit', 'normalized', 'position', [0.05, 0.75,0.4,0.2])
copyobj(allchild(get(f1,'CurrentAxes')),h(1));
% title('a) Boston')
h(1).FontSize = 16
h(1).XLim = [733043 733407]
legend('Observation', 'Model-AR', 'GTSR');
%xlabel('Observed Surge (m)')
%ylabel('Surge Height (m)')
%-------------------------------------------------------------------------%

h(2) = subplot(6,3,2);
line(x,y, 'Color','red', 'LineWidth',2)
%set(gca, 'unit', 'normalized', 'position', [0.6,0.75,0.2,0.2])
%t = 1:10;y = 1:10; plot(t,y)
copyobj(allchild(get(f2,'CurrentAxes')),h(2)); 
%title('Bluff Harbour')
h(2).XLim = [-1 2]
h(2).YLim = [-1 2]
h(2).FontSize = 16
%xlabel('Observed Surge (m)')
%ylabel('Model B Surge (m)')
%-------------------------------------------------------------------------%

h(3)=subplot(6,3,3); 
line(x,y, 'Color','red', 'LineWidth',2)
copyobj(allchild(get(f3,'CurrentAxes')),h(3)); 
%title('Bluff Harbour')
h(3).XLim = [-1 2]
h(3).YLim = [-1 2]
h(3).FontSize = 16
% xlabel('Observed Surge (m)')
% ylabel('GTSR Surge (m)')

%adjusting the subplots
set(h(1), 'Position', [0.05, 0.87,0.48,0.11])
set(h(2), 'Position', [0.6, 0.87,0.13,0.11])
set(h(3), 'Position', [0.8, 0.87,0.13,0.11])
datetick(h(1),'keeplimits')

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



