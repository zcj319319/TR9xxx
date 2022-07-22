close all; clear; clc;

% Setting 204b link parameters
l = 8; f = 2; m = 2; n_pie = 16;


% Setting spectrum analysis parameters
dcm = 1;
fs = 2949.12e6/dcm;
para.sideband=300;

para.sideband_sig=3e6;
para.fullscale=1200;
para.Rl=100;
para.num_interleave=4;
para.num_HD=7;
para.window='hann';
para.nyquitst_zone=1;
para.dacOSR=1;
para.plot_range=0;
para.simple_plot=0;
para.dc_1f_noise_cancel=20e6;      %% add cancel dc  and 1/f noise
para.dbc_th_HD=-20;                %% not add color for -70dbc
para.dbc_th_IMD=-20;
para.dbc_th_IL=-20;    
para.dbc_th_SFDR=-20;

% Start serial connection
s = serialport('COM5',115200, "Timeout", 1); configureTerminator(s,"CR");
flush(s);

% write 'F'
string = strcat("set_jesd204_reg=0x020 0x", dec2hex(f-1,2), '\n');
writeline(s,string);
readvalue = readline(s);
% writeline(s,"get_jesd204_reg?0x020\n");
% data = readline(s);

% write 'L'
lane_in_use = 2^l-1;
string = strcat("set_jesd204_reg=0x028 0x", dec2hex(lane_in_use,2), '\n');
writeline(s,string);
readvalue = readline(s);
% writeline(s,"get_jesd204_reg?0x028\n");
% data = readline(s);


% input('Press Enter if ADC chip config is done\n');

% reset jesd204 phy
string = strcat("reset_jesd204_phy=0x01\n");
writeline(s,string);
readvalue = readline(s);
pause(0.1);
string = strcat("reset_jesd204_phy=0x00\n");
writeline(s,string);
readvalue = readline(s);
% reset jesd204 IP
string = strcat("reset_jesd204=0x01\n");
writeline(s,string);
readvalue = readline(s);
pause(0.1);
string = strcat("reset_jesd204=0x00\n");
writeline(s,string);
readvalue = readline(s);

% input('Press Enter if sysref is sent\n');

flush(s);
writeline(s,"get_jesd204_reg?0x038\n");
readvalue = readline(s);
if ( strcmp(readvalue, "JESD204 addr 0x0038=0x01") )
    fprintf("JESD SYNC = 1\n");
else
    fprintf("JESD SYNC = 0\n");
end
clear s;

% Instantiate FPGA Data Capture System object
if ~exist('diqun_jtag','var') || ~isa(diqun_jtag,'f2m') || ~isprop(diqun_jtag,'TimeStamp') || ~strcmpi(diqun_jtag.TimeStamp,'17-May-2021 11:05:08')
    diqun_jtag = f2m;
end

% figure;
figure;


while (1)
pause(3);
[~,sysref,valid,d0,d1,d2,d3,d4,d5,d6,d7,sof]=step(diqun_jtag);
link_data = [double([d0,d1,d2,d3,d4,d5,d6,d7]), double(sof)]';
converter_data = [transport(link_data, l, f, m, n_pie)]';

%adc_data = converter_data(:,1) + 1i * converter_data(:,2);
adc_data = converter_data(:,1);
figure(1); 
plot(converter_data(1:end,:));

%figure(4);
% perf=fft_calc(converter_data(1:4:end,2)',fs/4,15,para);
% perf=fft_calc(converter_data(2:4:end,2)',fs/4,15,para);
% perf=fft_calc(converter_data(3:4:end,2)',fs/4,15,para);
% perf=fft_calc(converter_data(4:4:end,2)',fs/4,15,para);
% figure(1); perf=fft_calc(adc_data',fs,15,para);
% drawnow;
end

release(diqun_jtag);