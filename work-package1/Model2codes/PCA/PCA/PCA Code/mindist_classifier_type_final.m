function j=mindist_classifier_type_final(tst,trn,type)
% This function used to calculate the minimum distance between the testing
% image and the training images using many metrics

% This code is edited by Eng. Alaa Tharwat Abd El. Monaaim Othman from Egypt 
% Teaching assistant in El Sorouk Academy for Computer Science And Information Technology
% Please for any help send to me  Engalaatharwat@hotmail.com 
% Please if you used this code please refer this references
% "A novel ear recognition method using features combination" ,Atallah
% Hashad, Gouda I. Salama, Alaa Tharwat, Journal of AEIC, Vol. 10, Dec 2008.
% A version Dec. 2008


% Where : tst is the test image as a column
%         trn is the training images as a columns
%         type is the type of the minimum distance
          
[a1,b1]=size(tst);
[a2,b2]=size(trn);
X=zeros(b1+b2,a1);
X(1,:)=tst';
X(2:b1+b2,:)=trn';


switch  (type)
    case 'Euclidean'
        Y=pdist(X,'Euclidean');
        dif=Y(1,1:b2);
        [p,j]=min(dif);
    
    case 'minkowski1'
        Y=pdist(X,'minkowski',3);
        dif=Y(1,1:b2);
        [p,j]=min(dif);  
    
    case 'minkowski2'
        Y=pdist(X,'minkowski',9);
        dif=Y(1,1:b2);
        [p,j]=min(dif);

    case 'cityblock'
        Y=pdist(X,'cityblock');
        dif=Y(1,1:b2);
        [p,j]=min(dif);

    case 'Hamming'
        Y=pdist(X,'Hamming');
        dif=Y(1,1:b2);
        [p,j]=min(dif);

    case 'Correlation'
        Y=pdist(X,'Correlation');
        dif=Y(1,1:b2);
        [p,j]=min(dif);

    case 'Jaccard'
        Y=pdist(X,'Jaccard');
        dif=Y(1,1:b2);
        [p,j]=min(dif);
    
    case 'Mahal'
        Y=pdist(X,'mahal');
        dif=Y(1,1:b2);
        [p,j]=min(dif);
    
    case 'cosine'
        Y=pdist(X,'cosine');
        dif=Y(1,1:b2);
        [p1,j]=min(dif);

    case 'Chebychev'
        Y=pdist(X,'Chebychev');
        dif=Y(1,1:b2);
        [p1,j]=min(dif);

    case 'seuclidean'
        Y=pdist(X,'seuclidean');
        dif=Y(1,1:b2);
        [p1,j]=min(dif);
end
