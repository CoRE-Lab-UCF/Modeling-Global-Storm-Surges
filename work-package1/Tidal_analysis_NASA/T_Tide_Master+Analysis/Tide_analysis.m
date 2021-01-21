function [ TCa, TCae, TCp, TCpe, Mt, pred, nameu ] = Tide_analysis( t, ts, lat)
% © Sönke Dangendorf, 2012;
% This program is based on a code provided by Dr. Ivan Haigh, Southampton
% tidal analysis with t-tide (Pawlowicz et al. 2002)
% t = time vector, numerical datum
% ts = time series vector
% lat = Latitude of the tide gauge location to be analyzed

vec = datevec(t);
Y = [vec(1,1):vec(end,1)]';

tide = ts;

%-------------------------

%% Tidal Analsysis
co = 0;
pred(1:length(tide),1)=NaN;
for  i = Y';
    
    %counter
    disp(i);
    
    co = co+1;
    x(co,1) = datenum(i,1,1,0,0,0);
    
    % Determine if year is leap year
    E = eomday(i, 2);
    if E==29
        j = find(t>=datenum(i,1,1,0,0,0) & t<datenum(i+1,1,1,0,0,0));
        A = tide(j);
    else
        j = find(t>=datenum(i,1,1,0,0,0) & t<datenum(i+1,1,2,0,0,0));
        A = tide(j);
    end
    
    if i == Y(end);
        A = [A;NaN(24,1)];
    end
    %Check data quality
    k = find(~isnan(A));
    % DQ(co,1) = (length(k)./length(A)).*100;
    if length(k) >= 8760*0.75;  % we want at least 75% data in order to make a tide prediction
        
        %Make prediction and store
        [nameu,fu,Con,pred2]= t_tide(A, ...
            'interval',1, ...
            'Rayleigh',1,...
            'start time',datevec(min(t(j))), ...
            'output', 'temp.txt', ...
            'latitude', lat, ...
            'error','wboot');
        %         [nameu,fu,Con,pred2,Mean_tide]= t_tide(A, ...
        %             'interval',1, ...
        %             'start time',min(ts(j)), ...
        %             'output', 'temp.txt');
        Mean_tide = nanmean(A);
        
        pred2 = pred2 + Mean_tide;
        if i == Y(end);
            pred(j,1) = pred2(1:end-24);
        else
            pred(j,1) = pred2;
        end
            
        %Store Tidal constituents
        
        TCa(1:length(Y),1:67) = NaN;
        TCae(1:length(Y),1:67) = NaN;
        TCp(1:length(Y),1:67) = NaN;
        TCpe(1:length(Y),1:67) = NaN;
        
        %if length(Con(:,1))<67;
            TCa(co,1:length(Con(:,1))) = Con(:,1)';
            TCae(co,1:length(Con(:,1))) = Con(:,2)';
            TCp(co,1:length(Con(:,1))) = Con(:,3)';
            TCpe(co,1:length(Con(:,1))) = Con(:,4)';
            Mt(co,1:length(Con(:,1))) = Mean_tide;
%         else
%             TCa(co,:) = Con(:,1)';
%             TCae(co,:) = Con(:,2)';
%             TCp(co,:) = Con(:,3)';
%             TCpe(co,:) = Con(:,4)';
%             Mt(co,1) = Mean_tide;
%         end
    else
        pred(j,1) = NaN;
        
        %Store Tidal constituents
        TCa(co,1:67) = NaN;
        TCae(co,1:67) = NaN;
        TCp(co,1:67) = NaN;
        TCpe(co,1:67) = NaN;
        Mt(co,1) = NaN;
        
    end
    
    %clear variables
    clear A j k E fu Con pred2 Mean_tide B
    
end


end

