%to copy daily max surge (with it the time of occurence) to folder of
%predictor information

bas_pth = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\4Xdaily_10X10_217_TGs'
list_tg = dir(bas_pth);
list_tg(1:2) = [];
for ii = 764:length(list_tg)
    ii
    bas_pth2 =fullfile(bas_pth, list_tg(ii).name)
    name1 = strsplit(list_tg(ii).name, '_4d10x10');
    name2 = name1{1};
    cd(fullfile('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs', name2))
    id_name = strcat(name2, '_daily_new.mat')
    copyfile(id_name, bas_pth2)
    cd(bas_pth)
end
