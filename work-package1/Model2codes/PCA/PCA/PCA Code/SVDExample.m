clc
clear all;
X = [1     1     2     0     5     4     5     3
     3     2     3     3     4     5     5     4];

[r,c]=size(X);

% Compute the mean of the data matrix "The mean of each row" (Equation (10))
m=mean(X')';

% Subtract the mean from each image [Centering the data] (equation (11))
d=X-repmat(m,1,c);

% Construct the matrix Z
Z = d' / sqrt(c-1);

% Calculate SVD
[L,S,R] = svd(Z);

% Calculate the eigenvalues and eigenvectors
S = diag(S);
EigValues = S .* S;
EigenVectors=R;
