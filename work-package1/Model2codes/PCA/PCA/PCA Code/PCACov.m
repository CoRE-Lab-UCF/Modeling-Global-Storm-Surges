function [Newdata, PCASpace, EigValues]=PCACov(data)

[r,c]=size(data);

% Compute the mean of the data matrix "The mean of each row" (Equation (10))
m=mean(data')';

% Subtract the mean from each image [Centering the data] (Equation (11))
d=data-repmat(m,1,c);

% Compute the covariance matrix (co) (Equation (12))
co=(1 / (c-1))*d*d';

% Compute the eigen values and eigen vectors of the covariance matrix
[eigvector,EigValues]=eig(co);

PCASpace=eigvector;

% Project the original data on the PCA space
Newdata=PCASpace'*data;