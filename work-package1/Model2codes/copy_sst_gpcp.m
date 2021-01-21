%to copy SST and GPCP predictors to folder for Models 2.5 and 3.5
%development

bas_pth = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\Extracted' % source directory
list_tg = dir(bas_pth);
list_tg(1:2) = []; list_tg(1:3) = []; % removing non-folders
for ii = 1:length(list_tg)
    ii
    bas_pth2 =fullfile(bas_pth, list_tg(ii).name) % specific directory where you want to copy the file to
    name1 = strsplit(list_tg(ii).name, '_4d10x10');
    name2 = name1{1};
    cd(fullfile('F:\OneDrive - Knights - University of Central Florida\Daten\MLR\TG_pct_pcd_17yrs', name2)) %directory where the files are located
    %id_name = strcat(name2, '_daily_new.mat')
    copyfile('GPCP.mat', bas_pth2)
    copyfile('SST.mat', bas_pth2)

    cd(bas_pth)
end
