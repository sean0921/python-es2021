#!/usr/bin/env python3

from hw15_myseismo import read_site_waveform_record, calculate_azimuth, waveform_rotation

### 變數設定
event_info_filename        = 'hw15_material/ev.info'
site_waveform_ENZ_filename = 'hw15_material/MASB.txt'
site_waveform_RTZ_filename = 'hw15_material/MASB_RTZ.txt'

event_info, site_waveform_ENZ = read_site_waveform_record(event_info_filename, site_waveform_ENZ_filename)

azimuth = calculate_azimuth(event_info, site_waveform_ENZ)  ## 計算方位角, azimuth 是 float

site_waveform_RTZ = waveform_rotation(site_waveform_ENZ, azimuth)

with open(site_waveform_RTZ_filename,'w') as f:
    f.write(f'   time          R           T           Z\n')
    for i in site_waveform_RTZ:
        f.write(f'{i}\n')