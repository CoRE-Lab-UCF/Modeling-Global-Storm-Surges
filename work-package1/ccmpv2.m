%ftpobj = ftp('ftp2.remss.com');
%cd(ftpobj, 'ccmp');
%mget(ftpobj, 'v02.0');

list = dir(ftpobj);
for ii = 1:4
    mget(ftpobj, list(ii).name);
end
