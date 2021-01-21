    %% 5. Find simple predicted high and low waters
    disp('5. Find simple predicted high and low waters')
    m = mean(pred_all);
    i = find(pred_all > m);
    j = diff(i);
    k = find(j > 1);
    for a = 1:length(k)-1; %WHY REDUCE BY 1?    
        %progressbar(a/(length(k)-1));
        [Tmax, I] = max( pred_all( i(k(a)):i(k(a+1)) ) );
        I = I+(i(k(a))-1); % find the index of Tmax in the pred_all matrix
        HWpa(a,1) = ts_all(I); %assign timestamp from ts_all to the HWpa
        HWpa(a,2) = pred_all(I); %value of the high water in the pred_all
        HWpa(a,3) = I;%index of hw in ts_all

        [Tmin, J] = min( pred_all( i(k(a)):i(k(a+1)) ) );
        J = J+(i(k(a))-1);
        LWpa(a,1) = ts_all(J);
        LWpa(a,2) = pred_all(J);
        LWpa(a,3) = J;
        clear I J
    end
    clear i j k

    %creat empty datasets;
    le = length(HWpa(:,1));
    HW(1:le,1:3) = NaN;
    LW(1:le,1:3) = NaN;
    HWp(1:le,1:3) = NaN;
    LWp(1:le,1:3) = NaN;
    SK(1:le,1:4) = NaN;
    %------------------------