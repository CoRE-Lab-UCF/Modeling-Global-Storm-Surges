%remove trend from water level%

%load WL file first

%get unique year values
years = unique(WL(:,1));

%get mean WL for each unique year
meanWL = zeros(length(years), 2);
for ii = 1:length(years)
    currentYear = WL(WL(:,1) == years(ii),:);
    meanWL(ii,:) = [years(ii), mean(currentYear(:,5), 'omitnan')];
end

%subtract the meanWL
for ii = 1:length(WL)
    ii
    yrInd = find(years == WL(ii,1));
    WL(ii,6) = WL(ii,5) - meanWL(yrInd, 2);
end 