[m,n] = size(wt);
for ii = 1:m
    for jj = 1:n
        mag(ii, jj) = sqrt(real(wt(ii,jj))^2 + imag(wt(ii,jj))^2);
    end
end
figure; histogram(mag)

%% for subseted wt
hr_12 = hours(periods)>= 11 & hours(periods) <= 14; %subsetting the period from 11hr - 13hr
hr_24 = hours(periods)>= 23 & hours(periods) <= 25; %subsetting the period from 23hr to 25hr
wt_12 = wt(find(hr_12 == 1), :);
wt_24 = wt(find(hr_24 == 1), :);

[c,d] = size(wt_12); [e,f] = size(wt_24);
for ii = 1:c
    for jj = 1:d
        mag12(ii, jj) = sqrt(real(wt_12(ii,jj))^2 + imag(wt_12(ii,jj))^2); %computing the modulus of the complex numbers
    end
end

for ii = 1:e
    for jj = 1:f
        mag24(ii, jj) = sqrt(real(wt_24(ii,jj))^2 + imag(wt_24(ii,jj))^2);
    end
end

figure; histogram(mag12); figure; histogram(mag24);


%% Check outliers
cutoff12 = mean(mag12(:)) + 5*std(mag12(:)); %applying the five std from the mean as a cut-off 
cutoff24 = mean(mag24(:)) + 5*std(mag24(:));
wt_clr = wt;
for ii = 1:c
    for jj = 1:d
        if mag2(ii, jj) > cutoff
            %out_lier(ii,jj) = 0;
            wt_clr(ii, jj) = 0; 
        end
    end
end
rec_ts =icwt(wt_clr); %reconstructed time series
figure; plot(Thour(isfinite(x)), xx, 'b');
hold on; plot(Thour(isfinite(x)), rec_ts, 'r')
legend('T-Tide', 'Wavelet Transform');
title(['mean + 5*std used as a cutoff'])
datetick('keeplimits');

datestr(cursor_info.Position(1))
