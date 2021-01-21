% To count the number of predictors used after stepwise regression

base_dir = 'F:\OneDrive - Knights - University of Central Florida\Daten\MLR\Model_2\M2.5\mdl2p5_MLR_Kfold_4daily_10X10_17yrs'
cd(base_dir)
dd = dir('*.mat')
pc_stp = [];
for mt = 1:length(dd)
    cd(fullfile(base_dir, dd(mt).name))
    dat = dir('*.mat');
    load(dat.name)
    abc = length(find(inmodel == 1));
    pc_stp = [pc_stp; abc]; 
    clearvars -except base_dir dd pc_stp 
end

 save('numb_PCs_afterstp_449TGs.mat')
