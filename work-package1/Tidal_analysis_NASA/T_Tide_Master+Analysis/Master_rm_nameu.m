%% Get list of file names
basepath = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\TG_mat_global_unique';
cd(basepath);

% Get list with file names
list = dir('*.mat');
%list(1:2) = [];

%% Run loop for tidal analysis with T_Tide for all sites seperately

for ii = 1:length(list)
    ii
    cd (basepath);
    fname = list(ii).name; 
    load(fname)
    
    cd('C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Coden\Tidal_analysis_NASA\T_Tide_Master+Analysis')
    
    %Check data quality
    
    
    %Pass on to Tide_analysis
    [ TCa, TCae, TCp, TCpe, Mt, pred] = Tide_analysis(Thour,Whour_detr,Lat);
    Surge = Whour_detr-pred;
    Tide = pred;
    
    %to automatically name the .mat files
    folder = 'C:\Users\mi292519\OneDrive - Knights - University of Central Florida\Daten\Tide_data\Surge_after_T_Tide'
    c = strsplit(list(ii).name, ';'); %I used ; to avoid skipping some seemingly redundant names
    baseFileName = sprintf('%s.mat', c{1});
    %c = strsplit(baseFileName, '_'); %splitting the fname to get the name of the file for saving
    fullMatFileName = fullfile(folder, baseFileName);
    save(fullMatFileName);
    clearvars -except basepath list ii;
end
