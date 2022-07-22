Ns=65536;
channel_num = 2;
Fclk=1;      % Norminal clock Freq. is 1GHz

if channel_num == 1
%%%%%%%%%%%%%%%  below is for one channel signal #############
bin = 131;   % bin /65536 = frequency / 1
db = 0.5;    % -6dBFS
Fsig=(bin/Ns)*Fclk;

tnom=0:1/Fclk:(Ns-1)/Fclk; %Ideal sampling times
%Generate Digital data of SINE signal
omiga=Fsig*2*pi; %unit : Grad/s
rawdati = 65536*0.5*(1+db*sin(omiga*tnom +3));
rawdatq = 65536*0.5*(1+db*cos(omiga*tnom +3));
datini=floor(rawdati);
datinq=floor(rawdatq);

elseif channel_num == 2
%%%%%%%%%%%%%%%  below is for two channel signal #############
bin1 = 133;   %bin = frequency/2.048 * fclkcleear63
db1 = 0.5*0.25;

bin2 = 131;   %bin = frequency/2.048 * fclk
db2 = 0.5*0.25;

Fsig1=(bin1/Ns)*Fclk;
tnom1=0:1/Fclk:(Ns-1)/Fclk; %Ideal sampling times
%Generate Digital data of SINE signal
omiga1=Fsig1*2*pi; %unit : Grad/s
rawdat1i = 65536*0.95*(0.25+db1*sin(omiga1*tnom1+3));
rawdat1q = 65536*0.95*(0.25+db1*cos(omiga1*tnom1+3));

Fsig2=(bin2/Ns)*Fclk;
tnom2=0:1/Fclk:(Ns-1)/Fclk; %Ideal sampling times
%Generate Digital data of SINE signal
omiga2=Fsig2*2*pi; %unit : Grad/s
rawdat2i = 65536*0.95*(0.25+db2*sin(omiga2*tnom2+3));
rawdat2q = 65536*0.95*(0.25+db2*cos(omiga2*tnom2+3));

datini=floor(rawdat1i+rawdat2i);
datinq=floor(rawdat1q+rawdat2q);
end

%write to file

%%%%%% below write i channel%%%%%%%
myfid = fopen('dac_mem_data_in.txt', 'w');
% put first bit to lsb, second to msb.
for i=1:Ns/2
    datin2(i*2-1)=datini(i*2);
    datin2(i*2)=datini(i*2-1);
end


dataout = dec2hex(datin2,4);

for i =1:Ns
    temp = dataout(i,1:4);
    data_a = temp(1:2);
    data_b = temp(3:4);
fprintf(myfid,'0x%s ', data_a);
fprintf(myfid,'0x%s ', data_b);
end
%%%%%% below write q channel%%%%%%%

% put first bit to lsb, second to msb.
for i=1:Ns/2
    datin2(i*2-1)=datinq(i*2);
    datin2(i*2)=datinq(i*2-1);
end

dataout = dec2hex(datin2,4);

for i =1:Ns
    temp = dataout(i,1:4);
    data_a = temp(1:2);
    data_b = temp(3:4);
fprintf(myfid,'0x%s ', data_a);
fprintf(myfid,'0x%s ', data_b);
end
fclose(myfid);

% Calculate Dyanmic Spec.
%[Asignal,SFDR,THD,SNR,ENOB] = snr_thd_lxq2(datin2,Fclk,1,0);