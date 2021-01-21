%%% Modified Ivan's code
 
function[Y,DQ,ts,tide,pred,pred_all,surge,SK,HW,LW,HWp,LWp,...
     HWpa,LWpa,TCn,TCa,TCp] = Skew_surge_v4(Thour,Whour_detr,Lat)

%% Get DQ to run Ivan's skew surge
Dt = datevec(Thour);
ts = Thour;
tide = Whour_detr;
le = length(tide);
lat = Lat;
wl = Whour_detr;

Y = unique(Dt(:,1));
clear DQ
th = 75; %threshold for percetage of data available

for i = 1:length(Y);
    f = find(Dt(:,1) == Y(i));
    Ll = length(find(~isnan(wl(f))));
    DQ(i,1) = Ll*100/8766; %find how much % of the data is not NaN
    DQ(i,2) = Y(i);
end

% Check enough availability of data
DQr = DQ(end:-1:1,:);
I = find(DQr(:,1)>75);
if isempty(I)  %Dont calculate anything if DQr < 75
    pred = NaN;
    pred_all = NaN;
    surge = NaN;
    SK = NaN;
    HW = NaN;
    LW = NaN;
    HWp = NaN;
    LWp = NaN;
    HWpa = NaN;
    LWpa = NaN;
    TCn = NaN;
    TCa = NaN;
    TCp = NaN;
    return
else
    TCa(1:length(Y),1:67) = NaN;
    TCae(1:length(Y),1:67) = NaN;
    TCp(1:length(Y),1:67) = NaN;
    TCpe(1:length(Y),1:67) = NaN;


    %% 3. Pred  and Surge
    disp('3. Predicting tide')

    %Predict Tide using t-tide
    co = 0;
    for  i = Y';

        %counter
        co = co+1;

        %Check if data percentage is above threshold
        if DQ(co,1)>= th;

            % Determine if year is leap year
            E = eomday(i, 2);

            if E==29
                j = find(ts>=datenum(i,1,1,0,0,0) & ts<datenum(i+1,1,1,0,0,0));
                A = wl(j);
            else

                j = find(ts>=datenum(i,1,1,0,0,0) & ts<datenum(i+1,1,2,0,0,0));
                %Check that last date is greater than 2nd of Jan year +1
                if ts(j(end))<datenum(i+1,1,1,23,45,0)
                    A = wl(j);
                    B(1:24,1) = NaN;
                    A = [A;B];
                else
                    A = tide(j);
                end
                clear B
            end

            %Make prediction and store
            [nameu,fu,Con,pred2,Mean_tide]= t_tide(A, ...
                'interval',1, ...
                'start time',min(ts(j)), ...
                'output', 'temp.txt', ...
                'latitude', lat, ...
                'error','wboot');
            pred2 = pred2 + Mean_tide;
            k = find(ts(j)>datenum(i,12,31,23,45,0));
            pred2(k) = [];
            j(k) = [];

            if length(pred2)>length(j)
                pred(j,1) = pred2(1:length(j));
            else
                pred(j,1) = pred2;
            end
            %Store Tidal constituents
            TCa(co,1:length(Con)) = Con(:,1)';
            TCae(co,1:length(Con)) = Con(:,2)';
            TCp(co,1:length(Con)) = Con(:,3)';
            TCpe(co,1:length(Con)) = Con(:,4)';
            Mt(co,1) = Mean_tide;                
            %clear variables
            TCn = nameu;
            clear A j k E fu nameu Con pred2 Mean_tide B E

        else

            %if DQ is zero don't do anything
            % if DQ(co,1)== 0;

                TCa(co,1:67) = NaN;
                TCae(co,1:67) = NaN;
                TCp(co,1:67) = NaN;
                TCpe(co,1:67) = NaN;
                Mt(co,1) = NaN;

                j = find(ts>=datenum(i,1,1,0,0,0) & ts<datenum(i+1,1,1,0,0,0));
                if isempty(j)
                else
                    pred(j,1) = NaN;
                end
                clear j

        end
    end

    %calculate surge
    surge = wl-pred;
    %---------------------------------

    %% 4. predict tide for the whole period
    disp('4. Predict tide for whole period')

    %work out nearest year with greater than 95%
    %DQr = DQ(end:-1:1,:);
    %I = find(DQr(:,1)>95);
    i = DQr(I(1),2);
    disp(['Using year ',num2str(i)])

    j = find(ts>=datenum(i,1,1,0,0,0) & ts<datenum(i+1,1,2,0,0,0));
    %Check that last date is greater than 2nd of Jan year +1
    if ts(j(end))<datenum(i+1,1,1,23,0,0)
        A = wl(j);
        B(1:24,1) = NaN;
        A = [A;B];
    else
        A = wl(j);
    end
    clear B
    [nameu,fu,Con,pred2,Mean_tide]= t_tide(A, ...
        'interval',1, ...
        'start time',min(ts(j)), ...
        'output', 'temp.txt', ...
        'latitude', lat, ...
        'error','wboot');

    %just use key constiutents
    %s =[12,20,35,41];   %4 main constiutents

    % just use 4 largest constituents
    [m,n] = sort(Con(:,1),'descend');
    s = n(1:4);
    disp(['Using constituents ',nameu(s(1),:),' ',nameu(s(2),:),' ',nameu(s(3),:),' ',nameu(s(4),:)])

    nameu = nameu(s,:);
    Con = Con(s,:);
    fu = fu(s,:);
    clear s
    pred_all(1:le,1) = NaN;
    clear i j

    ts_all = [];
    pred_all = [];
    for i = [Y(1)-1:Y(end)+1];
        ts2 = [datenum(i,1,1,0,0,0):datenum(0,0,0,1,0,0):datenum(i,12,31,23,0,0)]';
        pred2 = t_predic(ts2,nameu,fu,Con,lat);
        pred2 = pred2+Mean_tide;
        ts_all = [ts_all;ts2];
        pred_all = [pred_all;pred2];
        clear ts2 pred2 j
    end
    clear i nameu Con pred2 Mean_tide
    %remove start and end data
    i = find(ts_all<datenum(Y(1)-1,12,31,0,0,0));
    ts_all(i) = [];
    pred_all(i) = [];
    clear i
    i = find(ts_all>datenum(Y(end)+1,1,2,0,0,0));
    ts_all(i) = [];
    pred_all(i) = [];
    clear i
    %---------------------------------

    %% 5. Find simple predicted high and low waters
    disp('5. Find simple predicted high and low waters')
    m = nanmean(pred);
    
    %% Alex's patch .......................................................
    
    ts(isnan(pred))= [];
    wl(isnan(pred))= [];
    pred(isnan(pred))= [];
    
    pred= pred + 100; % to have only positive values

    % differences
    delta= diff((pred));
    delta_nan= delta; delta_nan(isnan(delta))= [];
    
    % The first delta must be positive
    if delta_nan(1)<0 % if it starts with a trough
        fpos= find(delta>0,1,'first');
        pred= pred(fpos:end,:); 
        delta= delta(fpos:end,:);
        ts= ts(fpos:end,:);
        wl= wl(fpos:end,:);
    else
        fpos= 1;
    end
    
    % find change between crest and trough
    fsign= find(diff(sign(delta)))+1;
    
    % only the crests:
    cre_tro= repmat([1;0], round(length(fsign)/2),1);
    crests= fsign(cre_tro== 1); 
    
    % Ivan also wants troughs
    troughs= fsign(cre_tro(1:end-1)== 0); % cause I removed the first trough
    
    pred= pred-100;

    I = crests;
    J = troughs;
        
    %% .....................................................................

    HWpa(:,1) = ts(I); %assign timestamp from ts_all to the HWpa
    HWpa(:,2) = pred(I); %value of the high water in the pred_all
    HWpa(:,3) = I;%index of hw in ts_all
    
    LWpa(:,1) = ts(J);
    LWpa(:,2) = pred(J);
    LWpa(:,3) = J;
    clear I J
    clear i j k

    %creat empty datasets;
    le = length(HWpa(:,1));
    HW(1:le,1:3) = NaN;
    LW(1:le,1:3) = NaN;
    HWp(1:le,1:3) = NaN;
    LWp(1:le,1:3) = NaN;
    SK(1:le,1:4) = NaN;
    %-------------------------

    %% 6. find matching actual and predicted high and low waters
    disp('6. Extracting high and low waters')
    le = length(HWpa(:,1));
    for i = 1:le;
        % progressbar(i/le);
        j = find(ts>=HWpa(i,1)-datenum(0,0,0,3,0,0) & ts<= HWpa(i,1)+datenum(0,0,0,3,0,0)  ); %fo semidurnal tides
        k = find(~isnan(wl(j)));
        if length(k)<1
            HW(i,1:3) = NaN;
        else
            [a,b] = max(wl(j));
            HW(i,1) = ts(j(b));
            HW(i,2) = a;
            HW(i,3) = j(b); % index of the time in the ts vector
            clear a b
        end
        clear k
        k = find(~isnan(pred(j)));
        if length(k)<1
            HWp(i,1:3) = NaN;
        else
            [a,b] = max(pred(j));
            HWp(i,1) = ts(j(b));
            HWp(i,2) = a;
            HWp(i,3) = j(b);
            clear a b
        end
        clear j k
    end
    for i= 1: le-1
        j = find(ts>=LWpa(i,1)-datenum(0,0,0,3,0,0) & ts<= LWpa(i,1)+datenum(0,0,0,3,0,0)  );
        k = find(~isnan(wl(j)));
        if length(k)<1
            LW(i,1:3) = NaN;
        else
            [a,b] = min(wl(j));
            LW(i,1) = ts(j(b));
            LW(i,2) = a;
            LW(i,3) = j(b);
            clear a b
        end
        clear k
        k = find(~isnan(pred(j)));
        if length(k)<1
            LWp(i,1:3) = NaN;
        else
            [a,b] = min(pred(j));
            LWp(i,1) = ts(j(b));
            LWp(i,2) = a;
            LWp(i,3) = j(b);
            clear a b
        end
        clear j k
        
    end
    clear le i
    SK(:,1) = HWp(:,1);
    SK(:,2) = HW(:,2)-HWp(:,2);
    SK(:,3) = HWp(:,3);
    SK(:,4) = (HW(:,1)-HWp(:,1)).*(24*15); %UK gauges
    
    %Check
    i = find(~isnan(HW(:,2)));
    HW2 = HW(i,:);
    HW2(:,4) = wl(HW2(:,3));
    %-------------------------

    %% 7. Removing bad HW and LW values
    disp('7. Removing bad HW and LW values')

    %HW
    clear HW_check
    HW_check(1:length(HW(:,1)),1:6) = NaN;
    HW_check(:,7) = 1:length(HW_check(:,1));
    i = find(~isnan(HW(:,3)));
    HW_check(i,1) = HW(i,3);
    HW_check(i,2) = HW(i,3)-1;
    HW_check(i,3) = HW(i,3)+1;

    %check for first and last values
    l = find(HW_check(:,2)<1);
    HW_check(l,2) = HW_check(l,1);
    clear l
    l = find(HW_check(:,3)>length(wl));
    HW_check(l,3) = HW_check(l,1);
    clear l

    %find wl values just before and after
    HW_check(i,4) = wl(HW_check(i,1),1);
    HW_check(i,5) = wl(HW_check(i,2),1);
    HW_check(i,6) = wl(HW_check(i,3),1);

    clear i
    i = find(isnan(HW_check(:,1)));
    HW_check(i,:) = [];


    clear i j k
    i = find(isnan(HW_check(:,4)));
    j = find(isnan(HW_check(:,5)));
    k = find(isnan(HW_check(:,6)));
    J = HW_check(j,7);
    K = HW_check(k,7);

    %remove high water values
    HW(J,1:3) = NaN;
    HW(K,1:3) = NaN;
    SK(J,1:4) = NaN;
    SK(K,1:4) = NaN;

    %LW
    clear L W_check
    LW_check(1:length(LW(:,1)),1:6) = NaN;
    LW_check(:,7) = 1:length(LW_check(:,1));
    i = find(~isnan(LW(:,3)));
    LW_check(i,1) = LW(i,3);
    LW_check(i,2) = LW(i,3)-1;
    LW_check(i,3) = LW(i,3)+1;

    %check for first and last values
    l = find(LW_check(:,2)<1);
    LW_check(l,2) = LW_check(l,1);
    clear l
    l = find(LW_check(:,3)>length(wl));
    LW_check(l,3) = LW_check(l,1);
    clear l

    %find wl values just before and after
    LW_check(i,4) = wl(LW_check(i,1),1);
    LW_check(i,5) = wl(LW_check(i,2),1);
    LW_check(i,6) = wl(LW_check(i,3),1);

    clear i
    i = find(isnan(LW_check(:,1)));
    LW_check(i,:) = [];

    clear i j k
    i = find(isnan(LW_check(:,4)));
    j = find(isnan(LW_check(:,5)));
    k = find(isnan(LW_check(:,6)));
    J = LW_check(j,7);
    K = LW_check(k,7);

    %remove high water values
    LW(J,1:3) = NaN;
    LW(K,1:3) = NaN;
    
end

