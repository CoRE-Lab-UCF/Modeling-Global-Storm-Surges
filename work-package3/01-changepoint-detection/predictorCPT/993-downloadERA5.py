import os
import cdsapi


dirHome = "G:\\report\\year-3\\07-Fall-2020\\#3Paper\\data\\"\
    "changePointTimeSeries\\mamun-cpt-approach\\era5\\fremantle-data"
os.chdir(dirHome)


c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels-preliminary-back-extension',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'variable': '10m_v_component_of_wind',
        'year': [
            '1950', '1951', '1952',
            '1953', '1954', '1955',
            '1956', '1957', '1958',
            '1959', '1960', '1961',
            '1962',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            -29, 112, -35,
            118,
        ],
    },
    'vwnd_1950_1962.nc')