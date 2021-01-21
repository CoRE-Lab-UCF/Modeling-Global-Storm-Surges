url = 'https://www.esrl.noaa.gov/psd/cgi-bin/db_search/DBListFiles.pl?did=164&tid=50675&vid=3722';
a = urlread(url);
b = strfind(a, 'uwnd')';
cd 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Reanalysis\20CR\uwnd_4X_sigma0.995'
for ii = 1:length(b) % 19 for sigma, 11 for uwnd 
    filename = a(b(ii):b(ii)+18)
    websave(filename, url);
end