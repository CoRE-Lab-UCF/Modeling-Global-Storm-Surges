function [ TCa, TCae, TCp, TCpe, pred] = Tidemaster_U( t, ts, lat)
% © Sönke Dangendorf, 2012;
% This program is based on a code provided by Dr. Ivan Haigh, Southampton
% tidal analysis with t-tide (Pawlowicz et al. 2002)
% t = time vector, numerical datum
% ts = time series vector
% lat = Latitude of the tide gauge location to be analyzed

vec = datevec(t);
Y = [vec(1,1):vec(end,1)]';

tide = ts;
i = find(tide==-777);
tide(i)= NaN;
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
        t1 = t(j);
    else
        j = find(t>=datenum(i,1,1,0,0,0) & t<datenum(i+1,1,2,0,0,0));
        A = tide(j);
        t1 = t(j);
    end
    
    if i == Y(end);
        A = [A;NaN(24,1)];
        t12 = [datenum(i+1,1,1,0,0,0):1/24:datenum(i+1,1,1,23,0,0)]';
        t1 = [t1;t12];
    end
    %Check data quality
    k = find(~isnan(A));
    DQ(co,1) = (length(k)./length(A)).*100;
    if DQ(co,1) >= 50;
        
        
        coef = ut_solv (t1, A, [], lat, 'auto');
        [ sl_fit, ~ ] = ut_reconstr ( t1, coef );                    
        
%         Mean_tide = nanmean(A);
%         
         pred2 = sl_fit;

        if i == Y(end);
            pred(j,1) = pred2(1:end-24);
        else
            pred(j,1) = pred2(1:end);
        end
            Con = coef.A;
        %Store Tidal constituents
        if length(Con)<67;
            TCa(co,1:length(Con(:,1))) = coef.A;
            TCae(co,1:length(Con(:,1))) = coef.A_ci;
            TCp(co,1:length(Con(:,1))) = coef.g;
            TCpe(co,1:length(Con(:,1))) = coef.g_ci;
            %Mt(co,1:length(Con(:,1))) = Mean_tide;
        else
            TCa(co,:) = coef.A;
            TCae(co,:) = coef.A_ci;
            TCp(co,:) = coef.g;
            TCpe(co,:) = coef.g_ci;
            %Mt(co,1) = Mean_tide;
        end
%     else
%         pred(j,1) = NaN;
%         
%         %Store Tidal constituents
%         TCa(co,1:67) = NaN;
%         TCae(co,1:67) = NaN;
%         TCp(co,1:67) = NaN;
%         TCpe(co,1:67) = NaN;
%         Mt(co,1) = NaN;
%             end
    
    %clear variables
    clear A j k E fu Con pred2 Mean_tide B
    
end


end

