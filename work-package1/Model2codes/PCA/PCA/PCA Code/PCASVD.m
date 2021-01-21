function [Newdata,PCASpace,EigValues]=PCASVD(data)
% PCASVD: This function constructs the PCA space using SVD method
% data - MxN matrix of input data
% M is the dimensions or features 
% N is the number of samples or observations
% Newdata is the original data after projection onto the PCA space
% PCASpace is the space of PCA (i.e. eigenvectors)
% EigValues represent the eigenvalues

[r,c]=size(data);

% Compute the mean of the data matrix "The mean of each row" (Equation (10))
m=mean(data')';

% Subtract the mean from each image [Centering the data] (equation (11))
d=data-repmat(m,1,c);

% Construct the matrix Z
Z = d' / sqrt(c-1);

% Calculate SVD
[L,S,R] = svd(Z);

% Calculate the eigenvalues and eigenvectors
S = diag(S);
EigValues = S .* S;
PCASpace=R;

% Project the original data on the PCA space
Newdata=PCASpace'*d;


