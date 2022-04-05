%correct time problems in Astoria
for ii = 1: length(WL)
    if leftOver(ii) >= 0
        WL(ii,3) = WL(ii,3) + 1;
        WL(ii,4) = leftOver(ii);
    end
end

%get thour
for ii = 1: length(WL)
    ii
    WL(ii,6) = datenum(WL(ii,1),WL(ii,2),WL(ii,3),WL(ii,4),0,0);
end
