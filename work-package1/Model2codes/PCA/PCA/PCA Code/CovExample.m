
clc
clear all;
X = [1     1     2     0     5     4     5     3
     3     2     3     3     4     5     5     4];


[r,c]=size(X);

% Compute the mean of the data matrix "The mean of each row" (Equation (10))
m=mean(X')';

% Subtract the mean from each image [Centering the data] (Equation (11))
d=X-repmat(m,1,c);

% Compute the covariance matrix (co) (Equation (12))
co=1 / (c-1)*d*d';

% Compute the eigen values and eigen vectors of the covariance matrix
[eigvector,eigvl]=eig(co);

% Project the data on the first eigenvector
% The first principal component is the second eigenvector
PC1=eigvector(:,2)
% Project the data on the PCa
Yv2=PC1'*d
% The second principal component is the first eigenvector
PC2=eigvector(:,1)
% Project the data on the PCa
Yv1=PC2'*d

% Reconstruct the data from the projected data on PC1
Xhat2= PC1*Yv2+repmat(m,1,c)
%Reconstruct the data from P2
Xhat1= PC2*Yv1+repmat(m,1,c)

Ev1=X-Xhat1
Ev2=X-Xhat2

