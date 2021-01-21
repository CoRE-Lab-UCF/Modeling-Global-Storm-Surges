%Random Forest application
clearvars -except vars y_surge
rng default
trainData = [vars y_surge];
features = vars; 
classLabels = y_surge;
nTrees = 100; 
B = TreeBagger(nTrees, features, classLabels, 'Method', 'regression');
cc = B.predict(vars);

%Plotting RF results
figure; ss = scatter(y_surge, cc, '+', 'k');
xlabel('Observed Surge(m)'); ylabel('Modelled Surge(m)');
hline = refline([1, 0]); hline.Color = 'r'; set(hline, 'LineWidth', 2);

R = corr(y_surge, cc); R_squared = R^2;
xx = y_surge; yy = cc; zz = yy - xx; zsqr = zz.*zz; zmean = mean(zsqr); sg_rmse = sqrt(zmean);
text(-0.06, 0.18, ['R^2 = ' num2str(R_squared)], 'Color', 'red', 'FontSize', 12);
text(-0.06, 0.15, ['RMSE = ' num2str(sg_rmse*100) 'cm'], 'Color', 'red', 'FontSize', 12);
set(gca, 'Box', 'on', 'XMinorTick', 'on', 'YMinorTick', 'on', 'fontname', 'times');
