function [Y,DQ,ts,tide,pred,pred_all,surge,SK,HW,LW,HWp,LWp,...
    HWpa,LWpa,TCn,TCa,TCp] = Skew_surge2(Thour,Whour_detr,Lat);

%% Get DQ to run Ivan's skew surge
Dt = datevec(Thour);
ts = Thour;
tide = Whour_detr;
le = length(tide);
lat = Lat;
wl = Whour_detr;

Y = unique(Dt(:,1));
clear DQ
th = 75;

for i = 1:length(Y);
    f = find(Dt(:,1) == Y(i));
    Ll = length(find(~isnan(wl(f))));
    DQ(i,1) = Ll*100/8766;
    DQ(i,2) = Y(i);
end

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
            
%         else
%             
%             %Find nearest year with more than 50% of data and do prediction
%             %with this instead
%             DF = abs(DQ(:,2)-i);
%             DF(:,2) = DQ(:,1);
%             DF(:,3) = DQ(:,2);
%             
%             j = find(DF(:,2)<th);
%             DF(j,:) = [];
%             [a,k] = sort(DF(:,1),'ascend');
%             DF = DF(k,:);
%             Yr = DF(1,3);
%             
%             disp([num2str(i),' replaced with ',num2str(Yr), '; ',num2str(abs(i-Yr))]);
%             
%             %Do tidal prediction for that year
%             % Determine if year is leap year
%             E = eomday(i, 2);
%             if E==29
%                 j = find(ts>=datenum(Yr,1,1,0,0,0) & ts<datenum(Yr+1,1,1,0,0,0));
%                 A = wl(j);
%             else
%                 
%                 j = find(ts>=datenum(Yr,1,1,0,0,0) & ts<datenum(Yr+1,1,2,0,0,0));
%                 %Check that last date is greater than 2nd of Jan year +1
%                 if ts(j(end))<datenum(Yr+1,1,1,23,45,0)
%                     A = wl(j);
%                     B(1:24,1) = NaN;
%                     A = [A;B];
%                 else
%                     A = tide(j);
%                 end
%                 clear B
%             end
%             clear E
%             %Make prediction
%             [nameu,fu,Con,pred2,Mean_tide]= t_tide(A, ...
%                 'interval',1, ...
%                 'start time',min(ts(j)), ...
%                 'output', 'temp.txt', ...
%                 'latitude', lat, ...
%                 'error','wboot');
%             
%             %Use those constituents to predict for missing year
%             ts2 = [datenum(i,1,1,0,0,0):datenum(0,0,0,1,0,0):datenum(i,12,31,23,0,0)]';
%             pred2 = t_predic(ts2,nameu,fu,Con,lat);
%             
%             %Store data
%             TCa(co,1:67) = NaN;
%             TCae(co,1:67) = NaN;
%             TCp(co,1:67) = NaN;
%             TCpe(co,1:67) = NaN;
%             Mt(co,1) = NaN;
%             
%             %Figure
%             clear j
%             j = find(ts>=datenum(i,1,1,0,0,0) & ts<datenum(i+1,1,1,0,0,0) );
%             %Mean_tide = nanmean(tide(j));
%             pred2 = pred2 + Mean_tide;
%             pred(j,1) = pred2;
%             clear j a k
%             
%         end
        
    end
end

%calculate surge
surge = wl-pred;
%---------------------------------

%% 4. predict tide for the whole period
disp('4. Predict tide for whole period')

%work out nearest year with greater than 95%
DQr = DQ(end:-1:1,:);
I = find(DQr(:,1)>95);
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
% for  i = Y';
%     ts2 = [datenum(i,1,1,0,0,0):datenum(0,0,0,1,0,0):datenum(i,12,31,23,0,0)]';
%     pred2 = t_predic(ts2,nameu,fu,Con,lat);
%     pred2 = pred2+Mean_tide;
%     j = find(ts>=datenum(i,1,1,0,0,0) & ts<datenum(i+1,1,1,0,0,0));
%     pred_all(j,1) = pred2;
%     clear ts2 pred2 j
% end
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
m = mean(pred_all);
i = find(pred_all > m);
j = diff(i);
k = find(j > 1);
for a = 1:length(k)-1;
    %progressbar(a/(length(k)-1));
    [Tmax, I] = max( pred_all( i(k(a)):i(k(a+1)) ) );
    I = I+(i(k(a))-1);
    HWpa(a,1) = ts_all(I);
    HWpa(a,2) = pred_all(I);
    HWpa(a,3) = I;
    
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
%-------------------------

%% 6. find matching actual and predicted high and low waters
disp('6. Extracting high and low waters')
le = length(HWpa(:,1));
for i = 1:le;
    % progressbar(i/le);
    j = find(ts>=HWpa(i,1)-datenum(0,0,0,3,0,0) & ts<= HWpa(i,1)+datenum(0,0,0,3,0,0)  );
    k = find(~isnan(wl(j)));
    if length(k)<1
        HW(i,1:3) = NaN;
    else
        [a,b] = max(wl(j));
        HW(i,1) = ts(j(b));
        HW(i,2) = a;
        HW(i,3) = j(b);
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
%%    
%     figure;
%     subplot(311)
%     hold on
%     plot(ts, pred_all,'-','color',[195 10 5]/255);
%     plot(LWpa(i,1), LWpa(i,2),'o','color','g','markerfacecolor','g','markersize',10);
%     plot(ts(j), pred_all(j),'b-');
%     subplot(312)
%     hold on
%     plot(ts, pred,'-','color',[195 10 5]/255);
%     plot(ts(j), pred(j),'b-');
%     plot(LWp(i,1), LWp(i,2),'o','color','g','markerfacecolor','g','markersize',10);
%     subplot(313)
%     hold on
%     plot(ts, tide,'-','color',[195 10 5]/255);
%     plot(ts(j), tide(j),'b-');   
%     plot(LW(i,1), LW(i,2),'o','color','g','markerfacecolor','g','markersize',10);
%     clear j
%%    
end
clear le i
SK(:,1) = HWp(:,1);
SK(:,2) = HW(:,2)-HWp(:,2);
SK(:,3) = HWp(:,3);
SK(:,4) = (HW(:,1)-HWp(:,1)).*(24*15);

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
%-------------------------

%% 8. Save data
% disp('8. Saving data')
% clear TCae TCpe Tmax Tmin a co i m th fid ans lat Mt fu
% % save(['2_MAT_DATA/',SID,'_aa'],'SID','Y','DQ','ts','tide','msl','pred',...
% %     'pred_all','surge','SK','HW','LW','HWp','LWp','HWpa','LWpa','TCn','TCa','TCp')
% disp('---------------------------------')
% %-------------------------

%% 8. Figure tidal all
% switch fig
%     case 'Y'
%         co = 0;
%         for i = 1895:1:2013
%             co = co+1;
%             x(co,1) = datenum(i,1,1,0,0,0);
%         end
%         
%         figure('units','normalized','position',[0.1 0.1 0.6 0.8]);
%         axes('units','normalized','position',[0.07 0.55 0.9 0.4]);
%         hold on
%         plot(ts, wl,'k');
%         % plot(HW(:,1), HW(:,2),'o','color','b','markerfacecolor','b','markersize',4);
%         % plot(LW(:,1), LW(:,2),'o','color','g','markerfacecolor','g','markersize',4);
%         plot(ts_all, pred_all,'r');
%         plot(HWpa(:,1), HWpa(:,2),'o','color','b','markerfacecolor','b','markersize',4);
%         plot(LWpa(:,1), LWpa(:,2),'o','color','g','markerfacecolor','g','markersize',4);
%         plot([ts(1) ts(end)],[mean(pred_all) mean(pred_all)],'m','linewidth',2)
%         set(gca,'fontweight','bold','fontsize',14);
%         set(gca,'xlim',[datenum(1915,1,1,0,0,0) datenum(2013,1,1,0,0,0)],'xtick',x,'xticklabel',datestr(x,11));
%         set(gca,'xgrid','on');
%         %title(SID,'fontweight','bold','fontsize',20);
%         
%         axes('units','normalized','position',[0.07 0.05 0.4 0.4]);
%         hold on
%         plot(ts_all, pred_all,'r');
%         plot(HWpa(:,1), HWpa(:,2),'o','color','b','markerfacecolor','b','markersize',4);
%         plot(LWpa(:,1), LWpa(:,2),'o','color','g','markerfacecolor','g','markersize',4);
%         plot([ts(1) ts(end)],[mean(pred_all) mean(pred_all)],'m','linewidth',2)
%         set(gca,'fontweight','bold','fontsize',14);
%         set(gca,'xlim',[datenum(1915,1,1,0,0,0)-0.01 datenum(1915,1,1,0,0,0)+2],'xtick',x,'xticklabel',datestr(x,11));
%         set(gca,'xgrid','on');
%         %title(SID,'fontweight','bold','fontsize',20);
%         
%         axes('units','normalized','position',[0.55 0.05 0.4 0.4]);
%         hold on
%         plot(ts_all, pred_all,'r');
%         plot(HWpa(:,1), HWpa(:,2),'o','color','b','markerfacecolor','b','markersize',4);
%         plot(LWpa(:,1), LWpa(:,2),'o','color','g','markerfacecolor','g','markersize',4);
%         plot([ts(1) ts(end)],[mean(pred_all) mean(pred_all)],'m','linewidth',2)
%         set(gca,'fontweight','bold','fontsize',14);
%         set(gca,'xlim',[datenum(2013,1,1,0,0,0)-2 datenum(2013,1,1,0,0,0)],'xtick',x,'xticklabel',datestr(x,11));
%         set(gca,'xgrid','on');
%         %title(SID,'fontweight','bold','fontsize',20);
% end
% %-------------------------
% 
% %% 6. Figure
% % switch fig
%     % case 'Y'
%         clear x
%         co = 0;
%         for i = 1895:1:2014
%             co = co+1;
%             x(co,1) = datenum(i,1,1,0,0,0);
%         end
%         clear co i
%         
%         figure('units','normalized','position',[0.1 0.1 0.6 0.8]);
%         %Tide
%         axes('units','normalized','position',[0.07 0.68 0.9 0.27]);
%         hold on
%         plot(ts_all, pred_all,'+-','color',[195 10 5]/255);
%         plot(ts, pred,'-','color',[195 10 5]/255);
%         %plot(ts, tide,'-','color',[195 10 5]/255);
%         plot(ts, wl,'+-','color',[9 70 191]/255);
%         plot(HW(:,1), HW(:,2),'o','color','r','markerfacecolor','r','markersize',4);
%         plot(LW(:,1), LW(:,2),'o','color','g','markerfacecolor','g','markersize',4);
%         set(gca,'fontweight','bold','fontsize',14);
%         set(gca,'xlim',[datenum(1897,1,1,0,0,0) datenum(2015,1,1,0,0,0)],'xtick',x,'xticklabel',datestr(x,11));
%         set(gca,'xgrid','on');
%         ylabel('Level (m)','fontweight','bold','fontsize',16);
%         box on
%         
%         %PRED
%         axes('units','normalized','position',[0.07 0.37 0.9 0.27]);
%         hold on
%         %plot(ts, pred_all,'-','color',[9 70 191]/255);
%         plot(ts, pred,'-','color',[195 10 5]/255);
%         plot(HWp(:,1), HWp(:,2),'o','color','b','markerfacecolor','b','markersize',4);
%         plot(LWp(:,1), LWp(:,2),'o','color','g','markerfacecolor','g','markersize',4);
%         set(gca,'fontweight','bold','fontsize',14);
%         set(gca,'xlim',[datenum(1897,1,1,0,0,0) datenum(2015,1,1,0,0,0)],'xtick',x,'xticklabel',datestr(x,11));
%         set(gca,'xgrid','on');
%         ylabel('Level (m)','fontweight','bold','fontsize',16);
%         box on
%         
%         %surge
%         axes('units','normalized','position',[0.07 0.05 0.9 0.27]);
%         hold on
%         plot(ts, surge,'-','color',[34 166 50]/255);
%         plot(SK(:,1),SK(:,2),'o','color','r','markerfacecolor','r','markersize',4);
%         set(gca,'fontweight','bold','fontsize',14);
%         set(gca,'xlim',[datenum(1897,1,1,0,0,0) datenum(2015,1,1,0,0,0)],'xtick',x,'xticklabel',datestr(x,11));
%         set(gca,'xgrid','on');
%         set(gca,'ylim',[-1 1.5])
%         xlabel('Year','fontweight','bold','fontsize',16);
%         ylabel('Level (m)','fontweight','bold','fontsize',16);
%         box on
% 
%         clear x
% % end
% % -------------------------
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 
% 

