%% Initialize
delete(instrfindall); close all; clear; clc;

% Discover platform, establish TCP/IP link
% tcp_fd = utility_discover_platform(8257);
tcp_fd = tcpclient('192.168.18.154', 8257);

% open Tx1 and ORx1
tx_enable_mask = [0 0 0 1];
rx_enable_mask = [0 0 0 1 0 0 0 0];
[~] = adrv9026_trx_enable_set(tcp_fd, rx_enable_mask,tx_enable_mask );

% load nr_fr1_tm3.1a_fdd_bw100_scs30_491p52MSps.mat;
% tx_input = waveStruct.waveform * 80;
% tx_input = tx_input .* exp(1i*2*pi*00e6/491.52e6*(1:length(tx_input))).';
fs = 491.52e6;
BW = 100e6;
N=65536;
num_of_sc = round(floor(N* BW / fs)/2) * 2;

x = zeros(N, 1);
x(1:num_of_sc/2) = 1;
x(end-num_of_sc/2+1 : end) = 1;
pha = exp(1i*2*pi*rand(N,1));
x = x.* pha;
tx_input = ifft(x);
tx_input = tx_input ./ max(abs(tx_input)) * 0.95;


[~] = adrv9026_data_download( tcp_fd, tx_input );
figure; pwelch(tx_input); title('feedforward signal');

rx_enable_mask = [0 0 0 0 0 0 0 0];
[~] = adrv9026_trx_enable_set(tcp_fd, rx_enable_mask,tx_enable_mask );

adrv9026_pll_frequency_set(tcp_fd, 'LO2', 2.8e9);
adrv9026_pll_status_get(tcp_fd);

clear tcp_fd; 