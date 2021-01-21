clc
clear all

% The total number of samples in each class is denoted by NSamples
NSamples=10;
% The number of classes
NClasses=40;

%Read the data 
counter=1;
for i=1:NClasses
   Fold=['s' int2str(i)];
   for j=1:NSamples
        FiN=[Fold '\' int2str(j) '.pgm'];
       
       % Read the image file
       I=imread(FiN);
       
       % Resize the image to reduce the computational time
       I=imresize(I,[50,50]);
       
       % Each image is represented by one column
       data(counter,:)=I(:);
       
       % Y is the class label matrix 
       Y(counter,1)=i;
       counter=counter+1;
   end
end

% Divide the samples into training and testing samples
% The number of training samples is denoted by NTrainingSamples
NTrainingSamples=9;

counter=1;
Training=[];   Testing=[];   TrLabels=[];   TestLabels=[];
for i=1:NClasses
   for j=1:NTrainingSamples
       Training(size(Training,1)+1,:)=data(counter,:) ;
       TrLabels(size(TrLabels,1)+1,1)=Y(counter,1);
       counter=counter+1;
   end
   for j=NTrainingSamples+1:NSamples
       Testing(size(Testing,1)+1,:)=data(counter,:) ;
       TestLabels(size(TestLabels,1)+1,:)=Y(counter,1);
       counter=counter+1;
   end
end
clear data Y I;
tic
% Calculate the PCA space, eigenvalues, and eigenvectors
data=Training';

[r,c]=size(data);
% Compute the mean of the data matrix "The mean of each row" (Equation (10))
m=mean(data')';
% Subtract the mean from each image (Equation (11))
d=data-repmat(m,1,c);

% Compute the covariance matrix (co) (Equation (11))
co=(1/c-1)*d*d';

% Compute the eigen values and eigen vectors of the covariance matrix
[eigvector,eigvl]=eig(co);

% Sort the eigen vectors according to the eigen values
eigvalue = diag(eigvl);
[junk, index] = sort(-eigvalue);
eigvalue = eigvalue(index);
eigvector = abs(eigvector(:, index));

% EigenvectorPer is the percentage of the selected eigenvectors
EigenvectorPer=50;
PCASpace=eigvector(:,1:EigenvectorPer*size(eigvector,2)/100);

% Project the training data on the PCA space.
TriningSpace=PCASpace'*d;
clear data;

% Calculate the lower and upper bounds of the class labels
% For example, the first testing sample is correctly classified when its
% label between 1 and 5, because the first testing sample belongs to the
% first class and the number of samples of the first class is 5. In other
% words, the first five samples of the training data belong to the first
% class.
counter=1;
for i=1:NSamples*NClasses-size(Training,1) % number of the tseting images
      l(i,:)=1+(counter-1)*(size(Training,1)/NClasses);
      h(i,:)=counter*(size(Training,1)/NClasses);
       if(rem(i,(NSamples-(size(Training,1)/NClasses)))==0)
           counter=counter+1;
       end
end

% Classification phase
% Each image is projected on the PCA space and then classified using
% minimum distance classifier.

CorrectyClassified_counter=0;
for i=1:size(Testing,1)
   TestingSample=Testing(i,:);
   TestingSample=TestingSample-m';
   TestingSample=PCASpace'*TestingSample';
   
   % Apply minimum distance classifier
   rr(i)=mindist_classifier_type_final(TestingSample,...
       TriningSpace,'Euclidean');
   if(rr(i)>=l(i,1) && rr(i)<=h(i,1))
       CorrectyClassified_counter=CorrectyClassified_counter+1;
   end
end

% The accuracy of the testing samples 
CorrectyClassified_counter*100/size(Testing,1)