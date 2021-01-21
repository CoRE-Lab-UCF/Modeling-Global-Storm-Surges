function call_generic_random_forests()

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Name - call_generic_random_forests
% Creation Date - 7th July 2015
% Author - Soumya Banerjee
% Website - https://sites.google.com/site/neelsoumya/
%
% Description - Function to load data and call generic random forests function
%
% Parameters - 
%	Input	
%
%	Output
%               BaggedEnsemble - ensemble of random forests
%               Plots of out of bag error
%		Example prediction	
%
% Example -
%		call_generic_random_forests()
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


load fisheriris
X = meas;
Y = species;
BaggedEnsemble = generic_random_forests(X,Y,60,'classification')
predict(BaggedEnsemble,[5 3 5 1.8])
