% Make a matrix for correlation comparison

jj = 1;
for ii = 1: length(m35)
    if m35(ii,1:2) == m1(jj,1:2)
        DAT(ii,1:2) = m35(ii,1:2);
        DAT(ii,3) = m1(jj,3); % correlation
        DAT(ii,4) = m35(ii,3);
        DAT(ii,5) = m1(jj,6);
        DAT(ii,6) = m35(ii,6); %relative rmse
        jj = jj +1
    else
        continue
    end
end
nn = find(DAT(:,1) == 0);
DAT(nn,:) = [];
save('RF_comp_m35_m1_619TGs.mat')
