#!/usr/bin/env python3

from collections import namedtuple
import numpy as np

### 讀取地震記錄(地震波記錄)
#def read_site_waveform_record(event_info_filename: str, site_waveform_filename: str) -> tuple[str, list]:
def read_site_waveform_record(event_info_filename, site_waveform_filename):
    with open(event_info_filename) as f:
        event_info = f.readline()   ## 只有一行
    with open(site_waveform_filename) as g:
        site_waveform_ENZ = g.readlines()   ## 多行習慣用 readlines()
    return(event_info, site_waveform_ENZ)

### 讀取事件
#def parse_event_info(event_info: str) -> namedtuple:
def parse_event_info(event_info):
    EV_info = namedtuple('EV_info', 'year month day hour min sec lon lat depth mag serial_number') # namedtuple 用不用沒差，總之你欄位不要搞錯就好
    year    = event_info[0:4]
    month   = event_info[5:7]
    day     = event_info[8:10]
    hour    = event_info[11:13]
    minute  = event_info[14:16]
    sec     = event_info[17:23]
    lon     = event_info[24:32]
    lat     = event_info[33:40]
    depth   = event_info[41:47]
    mag     = event_info[48:52]
    sn_info = event_info[53:]
    #print(year,month,day,hour,minute,sec,lon,lat,depth,mag,sn_info,sep=',')
    ev_info = EV_info(year,month,day,hour,minute,sec,lon,lat,depth,mag,sn_info)
    return(ev_info)

### 讀取地震震央、震源深度
#def get_event_location(event_info: str) -> tuple[float, float, float]:
def get_event_location(event_info):
    this_ev_info  = parse_event_info(event_info)
    this_ev_lat   = float(this_ev_info.lat)
    this_ev_lon   = float(this_ev_info.lon)
    this_ev_depth = float(this_ev_info.depth)
    return(this_ev_lat, this_ev_lon, this_ev_depth)

### 讀取測站位置
#def get_site_location(site_waveform_ENZ: list):
def get_site_location(site_waveform_ENZ):
    site_header     = site_waveform_ENZ[0:3]
    site_longitude  = float(site_header[0].split(':')[1])
    site_latitude   = float(site_header[1].split(':')[1])
    #site_elevation = ?????       ## assumed to be km, ignore
    site_elevation  = 0            ## ignore
    return(site_latitude,site_longitude,site_elevation)

### 計算地震方位角
#def calculate_azimuth(event_info: str, site_waveform_ENZ: list) -> float:
def calculate_azimuth(event_info, site_waveform_ENZ):
    event_latitude, event_longitude, event_depth = get_event_location(event_info)
    site_latitude, site_longitude, site_elevation = get_site_location(site_waveform_ENZ)
    azimuth = np.arctan( ( site_longitude - event_longitude ) / ( site_latitude - event_latitude ) )
    return(azimuth)

### 旋轉地震記錄
#def waveform_rotation(site_waveform_ENZ: list, azimuth: float) -> list:
def waveform_rotation(site_waveform_ENZ, azimuth):
    site_waveform_ENZ_content = site_waveform_ENZ[4:]
    wf_data = namedtuple('wf_data','time edata ndata zdata')     # namedtuple 用不用沒差，總之你能把資料轉對，輸出也是對的就好
    wf_rt_data = namedtuple('wf_data','time rdata tdata zdata')
    wf_datalist = []
    for i in site_waveform_ENZ_content:
        time_raw,e_raw,n_raw,z_raw = i.split()
        time_data = float(time_raw)
        e_data = float(e_raw)
        n_data = float(n_raw)
        z_data = float(z_raw)
        wf_datalist.append(wf_data(time_data,e_data,n_data,z_data))
    #rotate_matrix_A = np.matrix([[np.cos(azimuth), np.sin(azimuth)],[(-1)*np.sin(azimuth), np.cos(azimuth)]])
    wf_rt_datalist = []
    for i in wf_datalist:
        e_data = i.edata
        n_data = i.ndata
        #e_n_matrix = np.matrix([[n_data], [e_data]])
        #r_t_matrix = np.matmul(rotate_matrix_A, e_n_matrix)
        radi_data =   np.cos(azimuth) * n_data + np.sin(azimuth) * e_data   #老師都給公式了就直接用這樣
        tran_data = - np.sin(azimuth) * n_data + np.cos(azimuth) * e_data   #老師都給公式了就直接用這樣
        wf_rt_datalist.append(wf_rt_data(i.time, radi_data, tran_data, i.zdata))
    site_waveform_RTZ = []
    for i in wf_rt_datalist:
        site_waveform_RTZ.append(f'{i.time:10.4e} {i.rdata:11.4e} {i.tdata:11.4e} {i.zdata:11.4e}')
    return(site_waveform_RTZ)

if __name__ ==  '__main__':
    pass    ## 讓直接執行程式的人不會看到它做任何事情，它只是個放函式的地方