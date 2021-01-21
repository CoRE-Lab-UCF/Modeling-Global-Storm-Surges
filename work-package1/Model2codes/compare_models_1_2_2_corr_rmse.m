% Make a matrix for correlation comparison

jj = 1;
for ii = 1: length(m25)
    if m25(ii,1:2) == m1(jj,1:2)
        m123(ii,1:2) = m25(ii,1:2);
        m123(ii,3) = m1(jj,3); % correlation
        m123(ii,4) = m25(ii,3);
        m123(ii,5) = m1(jj,6);
        m123(ii,6) = m25(ii,6); %relative rmse
        jj = jj +1
    else
        continue
    end
end
nn = find(m123(:,1) == 0);
m123(nn,:) = [];
save('cmpr_models_1_2_3_619TGs.mat')

%% for absolute rmse
jj = 1;
for ii = 1: length(m25)
    if m25(ii,1:2) == m1(jj,1:2)
        m123(ii,1:2) = m25(ii,1:2);
        m123(ii,3) = m1(jj,3); % correlation
        m123(ii,4) = m25(ii,3);
        m123(ii,5) = m1(jj,5);
        m123(ii,6) = m25(ii,5); %relative rmse
        jj = jj +1
    else
        continue
    end
end
nn = find(m123(:,1) == 0);
m123(nn,:) = [];
save('abs_rmse_models_1_2_3_619TGs.mat')