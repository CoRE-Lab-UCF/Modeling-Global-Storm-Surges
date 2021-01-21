% To do PCA on time-lagged predictors
b1 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted'
b2 = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs'

a = dir(b1); b = [a.isdir]; lst1 = a(b); lst1(1:2) = [];
c = dir(b2); d = [c.isdir]; lst2 = c(d); lst2(1:2) = []; 
clearvars -except b1 b2 lst1 lst2 

%Load predictors and predictand
for jj = 1:length(lst1)
    cd(fullfile(b1, lst1(jj).name))
    %Load uwnd
    load('uwnd_lagged.mat')
    clear base_dir fid tg_lst ii
    %Load vwnd
    load('vwnd_lagged.mat')
    clear base_dir fid tg_lst ii
    %Load slp
    load('slp_lagged.mat')
    clear base_dir fid tg_lst ii
    %Load surge_daily
    cd(fullfile(b2, lst2(jj).name))
    load('aasiaat,greenland-001-glossdm-bodc_17yrs_daily_new.mat')
    clear aa base_pt bb cc e1 e2 ll lst nn ss Surge surge_hr Thour tt
    
    %Find common time frame for predictors & predictand
    p1 = datevec(ut0_lag); q1 = datenum(p1(:,1:3));
    p2 = datevec(ut6_lag); q2 = datenum(p2(:,1:3));
    p3 = datevec(ut12_lag); q3 = datenum(p3(:,1:3));
    p4 = datevec(ut18_lag); q4 = datenum(p4(:,1:3));
    p5 = datevec(ut24_lag); q5 = datenum(p5(:,1:3));
    p6 = datevec(ut30_lag); q6 = datenum(p6(:,1:3));
    p7 = datevec(vt0_lag); q7 = datenum(p7(:,1:3));
    p8 = datevec(vt6_lag); q8 = datenum(p8(:,1:3));
    p9 = datevec(vt12_lag); q9 = datenum(p9(:,1:3));
    p10 = datevec(vt18_lag); q10 = datenum(p10(:,1:3));
    p11 = datevec(vt24_lag); q11 = datenum(p11(:,1:3));
    p12 = datevec(vt30_lag); q12 = datenum(p12(:,1:3));
    p13 = datevec(st0_lag); q13 = datenum(p13(:,1:3));
    p14 = datevec(st6_lag); q14 = datenum(p14(:,1:3));
    p15 = datevec(st12_lag); q15 = datenum(p15(:,1:3));
    p16 = datevec(st18_lag); q16 = datenum(p16(:,1:3));
    p17 = datevec(st24_lag); q17 = datenum(p17(:,1:3));
    p18 = datevec(st30_lag); q18 = datenum(p18(:,1:3));
    
    pd = datevec(surge_daily(:,1)); qpd = datenum(pd(:,1:3));
    
    a = [q1(1) q2(1) q3(1) q4(1) q5(1) q6(1) q7(1) q8(1) q9(1) q10(1) q11(1) q12(1) q13(1) q14(1) q15(1) q16(1) q17(1) q18(1)];
    b = [q1(end) q2(end) q3(end) q4(end) q5(end) q6(end) q7(end) q8(end) q9(end) q10(end) q11(end) q12(end) q13(end) q14(end) q15(end) q16(end) q17(end) q18(end)];
    %c = (max(a):min(b))';
    clear p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18
    
    %Subsetting dataset to make matrices of the same size
    
    c = find(q1 == max(a)); d = find(q1 == min(b));
    ut0_lag = ut0_lag(c:d); u0 = u0(:,:,c:d);
    clear c d
    
    c = find(q2 == max(a)); d = find(q2 == min(b));
    ut6_lag = ut6_lag(c:d); u6 = u6(:,:,c:d);
    clear c d

    c = find(q3 == max(a)); d = find(q3 == min(b));
    ut12_lag = ut12_lag(c:d); u12 = u12(:,:,c:d);
    clear c d
    
    c = find(q4 == max(a)); d = find(q4 == min(b));
    ut18_lag = ut18_lag(c:d); u18 = u18(:,:,c:d);
    clear c d
    
    c = find(q5 == max(a)); d = find(q5 == min(b));
    ut24_lag = ut24_lag(c:d); u24 = u24(:,:,c:d);
    clear c d
    
    c = find(q6 == max(a)); d = find(q6 == min(b));
    ut30_lag = ut30_lag(c:d); u30 = u30(:,:,c:d);
    clear c d
    
    
    
    c = find(q7 == max(a)); d = find(q7 == min(b));
    vt0_lag = vt0_lag(c:d); v0 = v0(:,:,c:d);
    clear c d
    
    c = find(q8 == max(a)); d = find(q8 == min(b));
    vt6_lag = vt6_lag(c:d); v6 = v6(:,:,c:d);
    clear c d

    c = find(q9 == max(a)); d = find(q9 == min(b));
    vt12_lag = vt12_lag(c:d); v12 = v12(:,:,c:d);
    clear c d
    
    c = find(q10 == max(a)); d = find(q10 == min(b));
    vt18_lag = vt18_lag(c:d); v18 = v18(:,:,c:d);
    clear c d
    
    c = find(q11 == max(a)); d = find(q11 == min(b));
    vt24_lag = vt24_lag(c:d); v24 = v24(:,:,c:d);
    clear c d
    
    c = find(q12 == max(a)); d = find(q12 == min(b));
    vt30_lag = vt30_lag(c:d); v30 = u30(:,:,c:d);
    clear c d
    
    
    
    c = find(q13 == max(a)); d = find(q13 == min(b));
    st0_lag = st0_lag(c:d); s0 = s0(:,:,c:d);
    clear c d
    
    c = find(q14 == max(a)); d = find(q14 == min(b));
    st6_lag = st6_lag(c:d); s6 = s6(:,:,c:d);
    clear c d

    c = find(q15 == max(a)); d = find(q15 == min(b));
    st12_lag = st12_lag(c:d); s12 = s12(:,:,c:d);
    clear c d
    
    c = find(q16 == max(a)); d = find(q16 == min(b));
    st18_lag = st18_lag(c:d); s18 = s18(:,:,c:d);
    clear c d
    
    c = find(q17 == max(a)); d = find(q17 == min(b));
    st24_lag = st24_lag(c:d); s24 = s24(:,:,c:d);
    clear c d
    
    c = find(q18 == max(a)); d = find(q18 == min(b));
    st30_lag = st30_lag(c:d); s30 = s30(:,:,c:d);
    clear c d
    
    c = find(qpd == max(a)); d = find(qpd == min(b));
    surge_daily_sub = surge_daily(c:d,:);
    clear c d
    
end




























    