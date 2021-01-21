function [DFLD_Trans]=F_JDLDAPro(TrainData,vNumEachClass); 
%
% Syntax: [DFLD_Trans]=F_JDLDAPro(TrainData,vNumEachClass); 
%
% This function builds a regularized LDA subspace based on Juwei's R-LDA
% method, which presented in the following paper,
% Juwei Lu, K.N. Plataniotis, A.N. Venetsanopoulos, "Regularization Studies 
% of Linear Discriminant Analysis in Small Sample Size Scenarios with Application 
% to Face Recognition", Pattern Recognition Letter, in press.
%
% TrainData: Input training data, should be a matrix, with each column vector being
%   a sample.
% vNumEachClass: the number of the samples per class in [TrainData].
%
% Author: Lu Juwei - Bell Multimedia Lab, Dept. of ECE, U. of Toronto,
% Created in 08 Dec 2003.
%

VERY_SMALL=1e-3;

I=find(vNumEachClass<=2);
sss_rate=sum(vNumEachClass(I))/sum(vNumEachClass);
if sss_rate>=0.5
    % For L=2; L is the number of training samples per subject.
    stRegParam=struct('Eta_Sw',{1},'Threshold_EigVal_Sb',{0.02},'Update_EigVal_Sb',{0.05},'RemainEigVec',{1});
else
    % For L>2;
    stRegParam=struct('Eta_Sw',{1e-3},'Threshold_EigVal_Sb',{0.2},'Update_EigVal_Sb',{0.2},'RemainEigVec',{0.8});
end

% regularization parameter for ill-posed within-class scatter matrix.
% smaller number of training samples per subject need stronger regularizer.
% \eta \in [0,1]. Try different values of eta to find the best one.
% For simplicity, set eta_sw=1e-3 for L>2, while eta_sw=1 for L=2. 
eta_sw=stRegParam.Eta_Sw;

% The threshold is used to determine which small eigenvalues of Sb need to
% be adjusted. For simplicity, set thresh_eigval_sb=0.02 (of the biggest 
% eigenvalue of Sb).
thresh_eigval_sb=stRegParam.Threshold_EigVal_Sb;

% The the new value for those eigvalues of Sb needed to be adjusted.
% For simplicity, set update_eigval_sb=0.2 (of the biggest eigenvalue of
% Sb).
update_eigval_sb=stRegParam.Update_EigVal_Sb;

% The rate of remaining eigenvectors of Sb, others will be thrown away.
% For simplicity, set remain_eigvec=1, i.e. keep all the eigenvectors.
remain_eigvec=stRegParam.RemainEigVec;

[rowTrain,colTrain]=size(TrainData);
sample_num=colTrain;

eachclass_num=vNumEachClass;
class_num=length(eachclass_num);

mean_class=mean(double(TrainData),2);
mean_eachclass=zeros(rowTrain,class_num);
t=1;
for j=1:class_num
    tt=t+eachclass_num(j)-1;
    a=double(TrainData(:,t:tt));
 	mean_eachclass(:,j)=mean(a,2);
    t=tt+1;
end
clear('a');

% The first m_b eigenvectors corresponding to largest eigenvalues will be extracted
% from eigenvectors of Sb
m_b=class_num-1;

% Sw : the within-class scatter conviariance matrix 
% Sw=zeros(rowTrain,rowTrain);
% Sw=Phi_w*Phi_w';
Phi_w=zeros(rowTrain,colTrain);
j=1;
for i=1:class_num
    t=double(TrainData(:,j:j+eachclass_num(i)-1));
    m=kron(mean_eachclass(:,i),ones(1,eachclass_num(i)));
    b=t-m;
    Phi_w(:,j:j+eachclass_num(i)-1)=b;
%  	Sw=Sw+b*b'; 
 	j=j+eachclass_num(i); 
end 
clear('m','b','t'); 
Phi_w=Phi_w/sqrt(sample_num);

% Sb=Phi_b*Phi_b': the between-class scatter conviariance matrix 
% Sb_t=Phi_b'*Phi_b

m=kron(mean_class,ones(1,class_num));
clear('mean_class');
Phi_b=mean_eachclass-m;
clear('m');

for i=1:class_num
   Phi_b(:,i)=Phi_b(:,i)*sqrt(eachclass_num(i)/sample_num);
end

%Sb=Phi_b*Phi_b';
Sb_t=Phi_b'*Phi_b;

[eigvec,eigval]=eig(Sb_t);
clear('Sb_t');
eigval=abs(diag(eigval)');		% changed in 14 May 2001, original: eigval=diag(eigval)';
[eigval,I]=sort(eigval);
eigval_Sb_t=fliplr(eigval); 
eigvec_Sb_t=fliplr(eigvec(:,I));
clear('eigvec','eigval');

% Eigenvalue adjustment method 1: The following is a simple way to throw 
% those eigenvectors of Sb corresponding to those smallest eigenvalues 
% (close to zeros).
m_b=round((class_num-1)*remain_eigvec); 

% Eigenvalue adjustment method 2: increase those smallest eigenvalues to a
% bigger value (update_eigval_sb), so as to reduce their influence.
aa=eigval_Sb_t/eigval_Sb_t(1);
bb=find(aa<thresh_eigval_sb);
eigval_Sb_t(bb)=eigval_Sb_t(1)*update_eigval_sb; % (v1) seems better than (v2).
%vEigval_Sb=vEigval_Sb+vEigval_Sb(1)*update_eigval_sb; % (v2)

% discard those with eigenvalues sufficient close to 0 and 
% extract first m_b eigenvectors corresponding to largest eigenvalues
%alaa
%eigvec_Sb_t=eigvec_Sb_t(:,1:m_b);
%eigval_Sb_t=eigval_Sb_t(:,1:m_b);

% eigenvectors of Sb
eigvec_Sb=Phi_b*eigvec_Sb_t;
clear('Phi_b','eigvec_Sb_t');

D_b=eigval_Sb_t.^(-1);
Z=eigvec_Sb*diag(D_b);

%mU_Sw_U=Z'*Phi_w*Phi_w'*Z;
mT=Z'*Phi_w;
mU_Sw_U=mT*mT';
clear('Phi_w','D_b','eigval_Sb_t','mT');

[eigvec,eigval]=eig(mU_Sw_U);
clear('mU_Sw_U');
eigval=abs(diag(eigval)');		% changed in 14 May 2001, original: eigval=diag(eigval)';
[eigval,I]=sort(eigval);
U_vec=eigvec(:,I);
clear('eigvec');

A=(Z*U_vec)';
clear('Z','U_vec');

% Regularized eigenvalues of Sw
D_w=(eta_sw+eigval).^(-1/2); % or mD_t=mP'*mU_St_U*mP;
DFLD_Trans=diag(D_w)*A;
