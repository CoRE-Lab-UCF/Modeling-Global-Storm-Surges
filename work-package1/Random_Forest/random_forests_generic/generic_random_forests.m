function BaggedEnsemble = generic_random_forests(X,Y,iNumBags,str_method)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Name - generic_random_forests
% Creation Date - 6th July 2015
% Author - Soumya Banerjee
% Website - https://sites.google.com/site/neelsoumya/
%
% Description - Function to use random forests
%
% Parameters - 
%	Input	
%		X - matrix
%		Y - matrix of response
%		iNumBags - number of bags to use for boostrapping
%		str_method - 'classification' or 'regression'
%
%	Output
%               BaggedEnsemble - ensemble of random forests
%               Plots of out of bag error
%
% Example -
%
%	 load fisheriris
% 	 X = meas;
%	 Y = species;
%	 BaggedEnsemble = generic_random_forests(X,Y,60,'classification')
%	 predict(BaggedEnsemble,[5 3 5 1.8])
%
%
% Acknowledgements -
%           Dedicated to my mother Kalyani Banerjee, my father Tarakeswar Banerjee
%				and my wife Joyeeta Ghose.
%
% License - BSD
%
% Change History - 
%                   7th July 2015 - Creation by Soumya Banerjee
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


BaggedEnsemble = TreeBagger(iNumBags,X,Y,'OOBPred','On','OOBPredictorImportance', 'On', 'Method',str_method)

% % plot out of bag prediction error
oobErrorBaggedEnsemble = oobError(BaggedEnsemble);
assignin('base', 'err_oob', oobErrorBaggedEnsemble);
% figID = figure;
% plot(oobErrorBaggedEnsemble)
% xlabel 'Number of grown trees';
% ylabel 'Out-of-bag classification error';
% print(figID, '-dpdf', sprintf('randomforest_errorplot_%s.pdf', date));

oobPredict(BaggedEnsemble)

% % view trees
% view(BaggedEnsemble.Trees{1}) % text description
% view(BaggedEnsemble.Trees{1},'mode','graph') % graphic description
