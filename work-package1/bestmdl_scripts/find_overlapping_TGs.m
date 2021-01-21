% To find overapping tide gauges for model A and model B %
 
jj = 1;
for ii = 1: length(mb)
    if mb(ii,1:2) == ma(jj,1:2)
        ma_b(ii,1:2) = mb(ii,1:2);
        ma_b(ii,3) = ma(jj,4); % correlation
        ma_b(ii,4) = mb(ii,4);
        ma_b(ii,5) = ma(jj,6);
        ma_b(ii,6) = mb(ii,6); % rmse
        ma_b(ii,7) = ma(jj,7);
        ma_b(ii,8) = mb(ii,7); % relative rmse
        jj = jj +1
        if jj - 1 == length(ma);
            return
        end
    else
        continue
    end
end
nn = find(ma_b(:,1) == 0);
ma_b(nn,:) = [];
save('RF_comp_m35_m1_619TGs.mat')