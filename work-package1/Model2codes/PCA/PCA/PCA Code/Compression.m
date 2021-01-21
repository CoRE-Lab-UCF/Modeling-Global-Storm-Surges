
clc
clear all;

data = imread('cameraman.png');

%If the image is RGB convert it to grayscale as follow
% data=rgb2gray(data);

%Each column represents on sample
[r,c]=size(data);

% Compute the mean of the data matrix "The mean of each row" (Equation (10))
m=mean(data')';

% Subtract the mean from each image [Centering the data] (Equation (11))
d=double(data)-repmat(m,1,c);

% Compute the covariance matrix (co) (Equation(12))
co=1 / (c-1)*d*d';

% Compute the eigen values and eigen vectors of the covariance matrix (Equation (2))
[eigvec,eigvl]=eig(co); 

% Sort the eigenvectors according to the eigenvalues (Descending order)
eigvalue = diag(eigvl);
[junk, index] = sort(-eigvalue);
eigvalue = eigvalue(index);
eigvec = eigvec(:, index);



for i=10:10:100
    % Project the original data (the image) onto the PCA space 
    % The whole PCA space or part of it can be used as folows as in
    % Equation (6)
    Compressed_Image=eigvec(:,1:(i/100)*size(eigvec,2))'*...
    double(d);
    
    % Reconstruct the image as in Equation (7)
    ReConstructed_Image= (eigvec(:,1:(i/100)*size(eigvec,2)))...
    *Compressed_Image;
    ReConstructed_Image=ReConstructed_Image+repmat(m,1,c);
    
    % Show the reconstructed image
    imshow(uint8(ReConstructed_Image))
    pause(0.5)
   
    % Calculate the error as in Equation (8)
    MSE=(1/(size(data,1)*size(data,2)))*...
    sum(sum(abs(ReConstructed_Image-double(data))))
    
    % Calculate the Compression Ratio (CR)= number of elments of the
    % compressed image / number of elements of the original image
    CR=numel(Compressed_Image)/numel(data)
end
